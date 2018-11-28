#include "BigNumber.h"

#ifdef __HEAPMANIP__
	#include <windows.h>
#endif

//��̬��Ա��������
#pragma region Static Members Definition

char *CBigNumber::ReaderBuffer = NULL;
int CBigNumber::nReaderBufferSize = 0;

int *CBigNumber::DivBuffer = NULL;
int CBigNumber::nDivBufferSize = 0;

int CBigNumber::nConstrCounts = 0;
int CBigNumber::nInstanceCounts = 0;

int CBigNumber::nBlockSize = 1;

#ifdef __HEAPMANIP__
	HANDLE CBigNumber::hHeap = NULL;
#endif

#pragma endregion

//���캯������������
#pragma region Custructors And Destructor
//����һ���ն���
CBigNumber::CBigNumber()
{
	++nInstanceCounts;
	this->pValueArray = NULL;
	this->nAllocCounts = 0;
	this->CountID = ++nConstrCounts;
}
//����һ�����Դ�СΪ_init_size (����Ϊ ������_init_sizeλ��bDecimal?10:BASE������) �Ķ�����ֵΪ0
CBigNumber::CBigNumber(int _init_size, int bDecimal)
{
	++nInstanceCounts;
	this->pValueArray = NULL;
	this->nAllocCounts = 0;
	this->CountID = ++nConstrCounts;
	
	if (bDecimal) _init_size = (_init_size - 1) / NLEN + 2;
	//this->pValueArray = _malloc(_init_size);
	//this->nAllocCounts = _init_size;
	this->_resize(_init_size);
	this->pValueArray[0] = 0;
}
//����һ��ֵΪarr[]�Ĵ�������
CBigNumber::CBigNumber(int arr[])
{
	++nInstanceCounts;
	this->pValueArray = NULL;
	this->nAllocCounts = 0;
	this->CountID = ++nConstrCounts;

	//this->nAllocCounts = abs(arr[0]) + 1;
	//this->pValueArray = _malloc(this->nAllocCounts);
	this->_resize(abs(arr[0]) + 1);
	memcpy(this->pValueArray, arr, (abs(arr[0]) + 1) * sizeof(int));
}
//������ֵ����һ������
CBigNumber::CBigNumber(int _intValue)
{
	++nInstanceCounts;
	this->pValueArray = NULL;
	this->nAllocCounts = 0;
	this->CountID = ++nConstrCounts;

	*this = _intValue;
}

//������캯��
CBigNumber::CBigNumber(const CBigNumber *_bn, int _reserved)
{
	memcpy(this, _bn, sizeof(CBigNumber));

	++nInstanceCounts;
	this->pValueArray = NULL;
	this->nAllocCounts = 0;
	this->CountID = ++nConstrCounts;

	this->_resize(_bn->nAllocCounts);
	memcpy(this->pValueArray, _bn->pValueArray, this->nAllocCounts * sizeof(int));
}

//ǳ�������캯��
CBigNumber::CBigNumber(const CBigNumber &_bn)
{
	memcpy(this, &_bn, sizeof(CBigNumber));

	++nInstanceCounts;
	this->pValueArray = NULL;
	this->nAllocCounts = 0;
	this->CountID = ++nConstrCounts;

	++ *((this->pValueArray = _bn.pValueArray) - 1);
	this->nAllocCounts = _bn.nAllocCounts;
}

//��������
CBigNumber::~CBigNumber(){
	//_free(this->pValueArray);
	this->_resize(0, 1);

	--nInstanceCounts;
	if (nInstanceCounts == 0){
		BufferAlloc(ReaderBuffer, nReaderBufferSize, 0);
		BufferAlloc(DivBuffer, nDivBufferSize, 0);
	}
}

#pragma endregion 

//�ڴ����
#pragma region Memory Manipulating Functions

void CBigNumber::_init_heap(int _init_size)
{
	#ifdef __HEAPMANIP__
		if (hHeap) HeapDestroy(hHeap);
		hHeap = HeapCreate(HEAP_NO_SERIALIZE|HEAP_GENERATE_EXCEPTIONS, _init_size, 0);
	#endif
}

int *CBigNumber::_malloc(int _nsize)
{
	if (_nsize == 0) return NULL;
#ifndef __HEAPMANIP__
	int *ptr = (int *)malloc((_nsize + 1) * sizeof(int));
#else
	if (!hHeap) _init_heap();
	int *ptr = (int *)HeapAlloc(hHeap, 0, (_nsize + 1) * sizeof(int));
#endif
	*ptr = 1;
	return ptr + 1;
}
int *CBigNumber::_realloc(int* &_ptr, int _newsize, int _orisize, int _preserve)
{
	/*
	if (_ptr == NULL) return NULL;
	map<int *, int>::iterator it = AllocTable.find(_ptr);
	if (it == AllocTable.end()) return NULL;
	int *_oriptr = _ptr;
	_ptr = _malloc(_newsize);
	if (_preserve) memcpy(_ptr, _oriptr, min(_newsize, _orisize) * sizeof(int));
	_free(_oriptr);
	return _ptr;
	*/
	if (_ptr == NULL) return NULL;
	int *_oriptr = _ptr;
	_ptr = _malloc(_newsize);
	if (_preserve) memcpy(_ptr, _oriptr, min(_newsize, _orisize) * sizeof(int));
	_free(_oriptr);
	return _ptr;
}
void CBigNumber::_free(int* &_ptr)
{
	/*if (_ptr == NULL) return;
	map<int *, int>::iterator it = AllocTable.find(_ptr);
	if (it != AllocTable.end()) 
		if (-- it->second == 0) {
		free(_ptr);
		_ptr = NULL;
		AllocTable.erase(it);
	}
	_ptr = NULL;
	*/
	if (_ptr == NULL) return;
	if (-- *(_ptr - 1) == 0){
		#ifndef __HEAPMANIP__
			free(_ptr - 1);
		#else
			if (hHeap) HeapFree(hHeap, 0, _ptr - 1);
		#endif
	}
	_ptr = NULL;
}

int CBigNumber::_resize(int _newsize, int _compact, int _preserve)
{
	_newsize = actAllocSize(_newsize);
	if (this->pValueArray == NULL){
		this->pValueArray = _malloc(_newsize);
		this->nAllocCounts = _newsize;
	}else{
		if (_compact == 0){
			if (_newsize > this->nAllocCounts){
				_realloc(this->pValueArray, _newsize, this->nAllocCounts, _preserve);
				this->nAllocCounts = _newsize;
			}
		}else{
			if (_newsize != this->nAllocCounts){
				_realloc(this->pValueArray, _newsize, this->nAllocCounts, _preserve);
				this->nAllocCounts = _newsize;
			}
		}
	}
	return this->nAllocCounts;
}


void CBigNumber::Instantiate(int reserve_size)
{
	if (this->pValueArray == NULL){
		if (reserve_size > 0) this->_resize(reserve_size);
	}else{
		int *ptr = this->pValueArray;

		if (*(ptr - 1) == 1){
			if (reserve_size > 0) this->_resize(reserve_size, 0, 1);
		}else{
			int _newsize = actAllocSize(max(reserve_size, this->nAllocCounts));
			this->pValueArray = _malloc(_newsize);
			memcpy(this->pValueArray, ptr, this->nAllocCounts * sizeof(int));
			_free(ptr);
			this->nAllocCounts = _newsize;
		}
	}
}

template <typename T>
void CBigNumber::BufferAlloc(T* &BufferPointer, int &nBufferSize, int RequireSize)
{
	if (RequireSize == 0){
		free(BufferPointer);
		BufferPointer = NULL;
		nBufferSize = 0;
	}else
		if (nBufferSize < RequireSize){
			free(BufferPointer);
			BufferPointer = (T *)malloc(RequireSize * sizeof(T));
			if (BufferPointer == NULL) nBufferSize = 0;
			else nBufferSize = RequireSize;
			
		}
}

void CBigNumber::SetBlockSize(int _newsize)
{
	nBlockSize = _newsize;
}

inline int CBigNumber::actAllocSize(int require_size)
{
	if (require_size % nBlockSize == 0)
		return require_size;
	else
		return (require_size / nBlockSize + 1) * nBlockSize;
}

void CBigNumber::Reserve(int _init_size, int bDecimal)
{
	if (bDecimal) _init_size = (_init_size - 1) / NLEN + 2;
	this->_resize(_init_size);
}

#pragma endregion

//����������������
#pragma region Operators (To BigNumber)

CBigNumber CBigNumber::operator + (const CBigNumber &_bn)const
{
	CBigNumber ret(max(abs(this->pValueArray[0]), abs(_bn.pValueArray[0])) + 2, 0);
	add(ret.pValueArray, this->pValueArray, _bn.pValueArray);
	return ret;
}
CBigNumber CBigNumber::operator - (const CBigNumber &_bn)const
{
	CBigNumber ret(max(abs(this->pValueArray[0]), abs(_bn.pValueArray[0])) + 2, 0);
	sub(ret.pValueArray, this->pValueArray, _bn.pValueArray);
	return ret;	
}
CBigNumber CBigNumber::operator * (const CBigNumber &_bn)const
{
	CBigNumber ret(abs(this->pValueArray[0]) + abs(_bn.pValueArray[0]) + 1, 0);
	mult(ret.pValueArray, this->pValueArray, _bn.pValueArray);
	return ret;	
}
CBigNumber CBigNumber::operator / (const CBigNumber &_bn)const
{
	CBigNumber ret(abs(this->pValueArray[0]) + 1, 0);
	//div(ret.pValueArray, this->pValueArray, _bn.pValueArray);
	BufferAlloc(DivBuffer, nDivBufferSize, abs(_bn.pValueArray[0]) + 2);
	div_ex(ret.pValueArray, this->pValueArray, _bn.pValueArray, NULL, 0, 0, DivBuffer, nDivBufferSize, 1);
	return ret;
}
CBigNumber CBigNumber::operator % (const CBigNumber &_bn)const
{
	CBigNumber ret(abs(this->pValueArray[0]) + 1, 0);
	div(NULL, this->pValueArray, _bn.pValueArray, ret.pValueArray);
	return ret;
}

CBigNumber& CBigNumber::operator = (const CBigNumber &_bn)
{
	this->_resize(0, 1);
	//++ AllocTable[this->pValueArray = _bn.pValueArray];
	++ *((this->pValueArray = _bn.pValueArray) - 1);
	this->nAllocCounts = _bn.nAllocCounts;
	return *this;
}

CBigNumber& CBigNumber::operator += (const CBigNumber &_bn)
{
	this->Instantiate(
		max(abs(this->pValueArray[0]), abs(_bn.pValueArray[0])) + 2
	);
	add(this->
		pValueArray, this->pValueArray, _bn.pValueArray);
	return *this;
}

CBigNumber& CBigNumber::operator -= (const CBigNumber &_bn)
{
	this->Instantiate();
	sub_ex(this->pValueArray, this->pValueArray, _bn.pValueArray, 0, 0);
	return *this;
}

#pragma endregion

//���������͵����������
#pragma region Operators (To Integer)

CBigNumber CBigNumber::operator + (const int &_t)const{
	return *this + CBigNumber(_t);
}

CBigNumber CBigNumber::operator - (const int &_t)const{
	return *this - CBigNumber(_t);
}

/*CBigNumber CBigNumber::operator * (const int &_t)const{
	return *this * CBigNumber(_t);
}*/
CBigNumber CBigNumber::operator * (const int &_t)const{
	CBigNumber ret(abs(this->pValueArray[0]) + 2, 0);
	mult(ret.pValueArray, this->pValueArray, _t);
	return ret;
}

/*CBigNumber CBigNumber::operator / (const int &_t)const{
	return *this / CBigNumber(_t);
}*/
CBigNumber CBigNumber::operator / (const int &_t)const{
	CBigNumber ret(abs(this->pValueArray[0]) + 1, 0);
	int r;
	div(ret.pValueArray, this->pValueArray, _t, r);
	return ret;
}

int CBigNumber::operator % (const int &_t)const{
	//div(NULL, this->pValueArray, _t, r);
	return  (int)(*this % CBigNumber(_t));
}

CBigNumber& CBigNumber::operator = (const int &_t)
{
	int n;
	if (_t == 0) n = 0;
	else n = (int)(log10((double)abs(_t)) / NLEN) + 1;
	if (this->nAllocCounts < n + 1){
		//_free(this->pValueArray);
		//this->pValueArray = _malloc(n + 1);
		this->_resize(n + 1);
		//this->nAllocCounts = n + 1;
	}
	conv(this->pValueArray, _t, this->nAllocCounts);
	return *this;
}

CBigNumber& CBigNumber::operator *= (const int &_t)
{
	this->Instantiate(abs(this->pValueArray[0]) + 2);
	mult(this->pValueArray, this->pValueArray, _t);
	return *this;
}

CBigNumber& CBigNumber::operator /= (const int &_t)
{
	int r;
	this->Instantiate();
	div(this->pValueArray, this->pValueArray, _t, r);
	return *this;
}

#pragma endregion


CBigNumber CBigNumber::operator - () const{
	CBigNumber ret(this);
	ret.pValueArray[0] = -ret.pValueArray[0];
	return ret;
}


#pragma region Convertion Functions
CBigNumber::operator int ()const{
	return conv<int>(this->pValueArray);
}
CBigNumber::operator long ()const{
	return conv<long>(this->pValueArray);
}
CBigNumber::operator float ()const{
	return conv<float>(this->pValueArray);
}
CBigNumber::operator double ()const{
	return conv<double>(this->pValueArray);
}
CBigNumber::operator long long ()const{
	return conv<long long>(this->pValueArray);
}
CBigNumber::operator long double ()const{
	return conv<long double>(this->pValueArray);
}
#pragma endregion

#pragma region Comparation Functions
//�Ƚ������߾�����
int CBigNumber::cmp(int a[],int b[])
{
	if (iszero(a) && iszero(b)) return 0;

	int i,t;
	if (a[0] == b[0]){
		t = abs(a[0]);
		i = t;
		while (i > 0 && a[i] == b[i]) --i;
		if (i > 0)
			return (a[i] - b[i]) * sign(a);
		else 
			return 0;
	}else
		return a[0] - b[0];
}
//�Ƚϸ߾�������int(�п��ܴ��ڵ���BASE)
int CBigNumber::cmp(int a[], int b)
{
	if (iszero(a) && iszero(b)) return 0;
	else if (sign(a) != sign(b)) return sign(a) - sign(b);
	int i,tmp = 0;
	int n = abs(a[0]);
	b = abs(b);
	for (i = n; i >= 1; --i){
		tmp = tmp * BASE + a[i];
		if (tmp >= b) break;
	}
	if (i == 1 && tmp == b) return 0;
	else if (i < 1) return - a[0];
	else return a[0];
}
#pragma endregion

#pragma region Addition Functions
//+++++++++++++++++++ �߾����� + �߾����� +++++++++++++++++++++
//֧�� s == t || s �� t == ��
int *CBigNumber::add(int d[], int s[], int t[], int _len)
{
	if (d == NULL) return NULL;
	if (iszero(s) && iszero(t))	return d[0] = 0, d;

	int n1 (abs(s[0])) , n2 (abs(t[0]));
	//�� d[] �Ĵ�С����
	if (_len != 0 && _len < max(n1, n2) + 2) return NULL;
	
	//������Ϊ 0 �����
	else if (iszero(s))
		copy(d, t, _len);
	else if (iszero(t))
		copy(d, s, _len);
	//�����������, ת��Ϊ���������ļ���
	if (s[0] < 0 && t[0] > 0){
		s[0] = -s[0];
		sub(d , t , s);
		s[0] = -s[0];
		return d;
	}else if (s[0] > 0 && t[0] < 0){
		t[0] = -t[0];
		sub (d, s, t);
		t[0] = -t[0];
		return d;
	}

	//=========== ����ͬ�����ļӷ� ===========
	int inverse = (s[0] < 0);
	int *r = t;
	if (n1 > n2){
		r = s;
		int t = n1;
		n1 = n2;
		n2 = t;
	}

	d[0] = n2;

	int carry = 0;
	int i;
	for (i = 1; i <= n1; ++i){
		d[i] = s[i] + t[i] + carry;
		if (d[i] >= BASE){
			d[i] -= BASE;
			carry = 1;
		}else carry = 0;
	}

	for (i = n1 + 1; i <= n2; ++i){
		d[i] = r[i] + carry;
		if (d[i] >= BASE){
			d[i] -= BASE;
			carry = 1;
		}else {
			carry = 0;
			break;
		}
	}

	if (i < n2){
		memcpy(&d[i + 1], &r[i + 1], (n2 - i) * sizeof(int));
	}
	
	if (carry == 1){
		d[++d[0]] = 1;
	}

	if (inverse) d[0] = - d[0];

	return d;
}
#pragma endregion

#pragma region Substraction Functions
//------------------- �߾����� - �߾����� ---------------------
//֧�� s == t || s �� t == ��
int *CBigNumber::sub(int d[], int s[], int t[], int _len)
{
	if (d == NULL) return NULL;

	int cmpret = cmp(s , t);
	if (cmpret == 0 || iszero(s) && iszero(t)) return d[0] = 0, d;

	int n1 = abs(s[0]), n2 = abs(t[0]);
	//�� d[] �Ĵ�С����
	if (_len != 0 && _len < max(n1, n2) + 2) return NULL;
	//������Ϊ 0 �����
	if (iszero(s)){
		memcpy(d + 1, t + 1, n2 * sizeof(int));
		d[0] = -t[0];
		return d;
	}else if (iszero(t)){
		memcpy(d + 1, s + 1, n1 * sizeof(int));
		d[0] = s[0];
		return d;
	}
	//�����������, ת�������������ļӷ�
	if (s[0] > 0 && t[0] < 0){
		t[0] = -t[0];
		add(d, s, t);
		t[0] = -t[0];
		return d;
	}else if (s[0] < 0 && t[0] > 0){
		s[0] = -s[0];
		add(d, s, t);
		s[0] = -s[0];
		d[0] = -d[0];
		return d;
	}

	//============== ����ͬ�����ļ��� ==============
	int inverse = 0;
	if (s[0] < 0 && t[0] < 0){
		inverse = 1;
		s[0] = -s[0];
		t[0] = -t[0];
	}
	if (cmpret < 0){///////////////ò��������////////�μ�sub_ex�е�
		int *tmp = s;
		s = t;
		t = tmp;
	}else if (cmpret == 0){
		d[0] = 0;
		return d;
	}
	//(���� s > t > 0 , ����ֱ�����)
	n1 = s[0], n2 = t[0];

	d[0] = n1;

	int borrow = 0;
	int i;

	for (i = 1; i <= n2 ; ++i){
		d[i] = s[i] - t[i] - borrow;
		if (d[i] < 0){
			d[i] += BASE;
			borrow = 1;
		}else borrow = 0;
	}

	for (i = n2 + 1; i <= n1; ++i){
		d[i] = s[i] - borrow;
		if (d[i] < 0){
			d[i] += BASE;
			borrow = 1;
		}else {
			borrow = 0;
			break;
		}
	}

	if (i < n1){
		memcpy(&d[i + 1], &s[i + 1], (n1 - i) * sizeof(int));
	}

	while (d[d[0]] == 0) --d[0];

	if (cmpret < 0) d[0] = -d[0];
	if (inverse) {
		d[0] = -d[0];
		s[0] = -s[0];
		t[0] = -t[0];
	}

	return d;
}

//set _s_reserve = 0 for d == s
int *CBigNumber::sub_ex(int d[], int s[], int t[], int _len, int _s_reserve)
{
	if (d == NULL) return NULL;

	int cmpret = cmp(s , t);
	if (cmpret == 0 || iszero(s) && iszero(t)) return d[0] = 0, d;

	int n1 = abs(s[0]), n2 = abs(t[0]);
	//�� d[] �Ĵ�С����
	if (_len != 0 && _len < max(n1, n2) + 2) return NULL;
	//������Ϊ 0 �����
	if (iszero(s)){
		memcpy(d + 1, t + 1, n2 * sizeof(int));
		d[0] = -t[0];
		return d;
	}else if (iszero(t)){
		memcpy(d + 1, s + 1, n1 * sizeof(int));
		d[0] = s[0];
		return d;
	}
	//�����������, ת�������������ļӷ�
	if (s[0] > 0 && t[0] < 0){
		t[0] = -t[0];
		add(d, s, t);
		t[0] = -t[0];
		return d;
	}else if (s[0] < 0 && t[0] > 0){
		s[0] = -s[0];
		add(d, s, t);
		if (_s_reserve) s[0] = -s[0];
		d[0] = -d[0];
		return d;
	}

	//============== ����ͬ�����ļ��� ==============
	int inverse = 0;
	if (s[0] < 0 && t[0] < 0){
		inverse = 1;
		s[0] = -s[0];
		t[0] = -t[0];
	}
	if ((inverse) ^ (cmpret < 0)){
		int *tmp = s;
		s = t;
		t = tmp;
	}
	//(���� s > t > 0 , ����ֱ�����)
	n1 = s[0], n2 = t[0];

	d[0] = n1;

	int borrow = 0;
	int i;

	for (i = 1; i <= n2 ; ++i){
		d[i] = s[i] - t[i] - borrow;
		if (d[i] < 0){
			d[i] += BASE;
			borrow = 1;
		}else borrow = 0;
	}

	for (i = n2 + 1; i <= n1; ++i){
		d[i] = s[i] - borrow;
		if (d[i] < 0){
			d[i] += BASE;
			borrow = 1;
		}else {
			borrow = 0;
			break;
		}
	}

	if (i < n1){
		memcpy(&d[i + 1], &s[i + 1], (n1 - i) * sizeof(int));
	}

	while (d[d[0]] == 0) --d[0];

	if (cmpret < 0) d[0] = -d[0];
	if (inverse) {
		d[0] = -d[0];
		if (_s_reserve) s[0] = -s[0];
		t[0] = -t[0];
	}

	return d;
}


////------------------- �߾����� - �������� ---------------------
//int *CBigNumber::sub(int d[], int s[], int t, int _len)
//{
//	int _t[2] = {1 , t};
//	return sub(d, s, _t, _len);
//}

#pragma endregion

#pragma region Multiplication Functions
//******************* �߾����� * �߾����� *********************
//֧�� s �� t �������ϵ
int *CBigNumber::mult(int d[], int s[], int t[], int _len)
{
	if (d == NULL) return NULL;

	int _sign = sign(s) * sign(t);
	if (_sign == 0) return d[0] = 0, d;

	int n1(abs(s[0])), n2(abs(t[0]));
	if (_len != 0 && _len < n1 + n2 + 1) return NULL;

	memset(d + 1, 0 , (n1 + n2) * sizeof(int));
	d[0] = n1 + n2 - 1;

	int i,j;

	for (i = 1; i <= n1; ++i){
		for (j = 1; j <= n2; ++j){
			d[i + j - 1] += s[i] * t[j];
			d[i + j] += d[i + j - 1] / BASE;
			d[i + j - 1] %= BASE;
		}
	}
	if (d[d[0] + 1] > 0) ++d[0];
	d[0] *= _sign;

	return d;
}

//******************* �߾����� * �������� *********************
int *CBigNumber::mult(int d[], int s[], int t, int _len)
{
	if (d == NULL) return NULL;

	int _sign = sign(s) * sign(t);
	if (_sign == 0) return d[0] = 0, d;
	
	int n = abs(s[0]);
	if (_len != 0 && _len < n + 2) return NULL;

	d[0] = n;
	int i = 0;
	int carry = 0;

	for (i = 1; i <= n; ++i){
        d[i] = carry + s[i] * t;
		carry = d[i] / BASE;
		d[i] %= BASE;
	}
	if (carry > 0) d[++d[0]] = carry;
	d[0] *= _sign;

	return d;
}
#pragma endregion

#pragma region Division Functions
//���ڳ������ٵ� �˷�ͬʱ�Ƚ�  cmp (d[] = s[] * t, r)
//�Ѽ��� ������ֵ �� �Ǹ�
int CBigNumber::multcmp(int d[], int s[], int t, int r[], int _len)
{
	if (d == NULL) return BASE;//������Ϣ����Ϊcmp�����Ľ��������>=BASE

	int _sign = sign(s) * sign(t);
	if (_sign == 0) return d[0] = 0, (sign(r) == 0 ? 0 : -1);
	
	int n = abs(s[0]);
	if (_len != 0 && _len < n + 2) return BASE;//������Ϣ

	d[0] = n;
	int i = 0;
	int carry = 0;
	int cmpret = 0;

	for (i = 1; i <= n; ++i){
        d[i] = carry + s[i] * t;
		carry = d[i] / BASE;
		d[i] %= BASE;
		if (d[i] < r[i]) cmpret = -1;
		else if (d[i] > r[i]) cmpret = 1;
	}

	if (carry > 0) {
		d[++d[0]] = carry;
		if (r[0] < d[0]) cmpret = 1;
		else if (r[r[0]] < carry) cmpret = 1;
		else if (r[r[0]] > carry) cmpret = -1;
	}else{
		if (r[0] > d[0]) cmpret = -1;
	}

	d[0] *= _sign;

	return cmpret;
}

///////////////////// �߾����� / �߾�����, d = s / t , r = s % t.
//֧�� s == t || s �� t == ��
int *CBigNumber::div(int d[], int s[], int t[], int r[], int _len, int _len_r)
{
	if (d == NULL && r == NULL) return NULL;
	int bdValid = (d != NULL);

	if (iszero(t)) return NULL;
	if (iszero(s)){
		if (bdValid) d[0] = 0;
		if (r) r[0] = 0;
		return d;
	}

	int _signs = sign(s), _signt = sign(t);
	int _sign = sign(s) * sign(t);
	int n1(s[0] = abs(s[0])), n2(t[0] = abs(t[0]));

	if (bdValid && _len != 0 && _len < n1 + 1) return NULL;

	int *r0 = r;
	if (r == NULL){
		r = (int *)malloc((n1 + 1) * sizeof(int));
	}else 
		if (_len_r != 0 && _len_r < n1 + 1) return NULL;

	if (bdValid) d[0] = 0;

	memcpy(r + 1, s + 1, n1 * sizeof(int));
	r[0] = n1;

	int i,tmp,m = n1;
	int flag = 0;
	int low, high ,mid;
	int tester;//������Сlow��high��ľ���
	int cmpret;

	int *tmparr = (int *)malloc((n2 + 2) * sizeof(int));

	if (bdValid) memset(d, 0, (n1 - n2 + 2) * sizeof(int));

	for (i = n1 - n2 + 1; i >= 1; i = min(i - 1 , m - n2 + 1)){
		tmp = r[i - 1];
		r[i - 1] = m - i + 1;

		cmpret = cmp(&r[i - 1], t);
		if (cmpret == 0){
			if (bdValid){
				d[i] = 1;
				if (!flag){
					d[0] = i;
					flag = 1;
				}
			}
			m = i - 1;
		}else if (cmpret > 0){
			//ȷ�� low �� high �ĳ�ʼֵ
			if (m - i + 1 == n2)
				tester = r[m];
			else
				tester = r[m] * BASE + r[m - 1];

			low = max(1, tester / (t[n2] + 1));
			high = min(BASE - 1, (tester + 1) / t[n2]);

			while (low <= high){
				mult(tmparr , t, mid = (low + high) / 2);
				cmpret = cmp(tmparr , &r[i - 1]);

				if (cmpret < 0){
					low = mid + 1;
				}else if (cmpret > 0){
					high = mid - 1;
				}else
					break;
			}

			if (cmpret > 0){
				if (--mid > 0)
					mult(tmparr , t, mid);
			}

			if (mid > 0){
				sub(&r[i - 1] , &r[i - 1], tmparr); 
				if (bdValid){
					d[i] = mid;
					if (!flag){
						d[0] = i;
						flag = 1;
					}
				}
			}
			if (iszero(r[i - 1])) m = i - 1;

		}

		r[i - 1] = tmp;
		while (r[m] == 0) --m;
	}

	free(tmparr);

	r[0] = m * _signs;
	if (r0 == NULL) free(r);

	s[0] *= _signs;
	if (s != t) t[0] *= _signt;
	if (bdValid) d[0] *= _sign;

	return d;
}

int *CBigNumber::div_ex(int d[], int s[], int t[], int r[], int _len, int _len_r, int tmparr[], int _len_tmparr, int _s_reserve)
{
	if (d == NULL && r == NULL) return NULL;
	int bdValid = (d != NULL);

	if (iszero(t)) return NULL;
	if (iszero(s)){
		if (bdValid) d[0] = 0;
		if (r) r[0] = 0;
		return d;
	}

	int _signs = sign(s), _signt = sign(t);
	int _sign = sign(s) * sign(t);
	int n1(s[0] = abs(s[0])), n2(t[0] = abs(t[0]));

	if (bdValid && _len != 0 && _len < n1 + 1) return NULL;

	int *r0 = r;

	if (_s_reserve){
		if (r == NULL){
			r = (int *)malloc((n1 + 1) * sizeof(int));
		}else if (_len_r != 0 && _len_r < n1 + 1) 
			return NULL;
		memcpy(r + 1, s + 1, n1 * sizeof(int));
		r[0] = n1;
	}else 
		r = s;

	if (bdValid) d[0] = 0;

	int i,tmp,m = n1;
	int flag = 0;
	int low, high ,mid;

	double tester1, tester2;//������Сlow��high��ľ���
	int cmpret;
	int *tmparr0 = tmparr;

	if (tmparr == NULL)
		tmparr = (int *)malloc((n2 + 2) * sizeof(int));
	else if (_len_tmparr != 0 && _len_tmparr < n2 + 2)
		return NULL;

	if (bdValid) memset(d, 0, (n1 - n2 + 2) * sizeof(int));

	for (i = n1 - n2 + 1; i >= 1; i = min(i - 1 , m - n2 + 1)){
		tmp = r[i - 1];
		r[i - 1] = m - i + 1;

		cmpret = cmp(&r[i - 1], t);
		if (cmpret == 0){
			if (bdValid){
				d[i] = 1;
				if (!flag){
					d[0] = i;
					flag = 1;
				}
			}
			m = i - 1;
		}else if (cmpret > 0){
			//ȷ�� low �� high �ĳ�ʼֵ

			if (m - i + 1 == n2){
				tester1 = r[m];
				tester2 = t[n2];
				if (n2 > 1){
					tester1 = tester1 * BASE + r[m - 1];
					tester2 = tester2 * BASE + t[n2 - 1];
				}
			}else{
				tester1 = r[m] * BASE + r[m - 1];
				tester2 = t[n2];
				if (n2 > 1){
					tester1 = tester1 * BASE + r[m - 2];
					tester2 = tester2 * BASE + t[n2 - 1];
				}
			}
			low = (int)max<double>(1, tester1 / (tester2 + 1));
			high = (int)min<double>(BASE - 1, (tester1 + 1) / tester2);

			while (low <= high){
				mult(tmparr , t, mid = (low + high) / 2);
				
				cmpret = cmp(tmparr , &r[i - 1]);
				
				if (cmpret < 0){
					low = mid + 1;
				}else if (cmpret > 0){
					high = mid - 1;
				}else
					break;
			}

			if (cmpret > 0){
				if (--mid > 0)
					mult(tmparr , t, mid);
			}

			if (mid > 0){
				sub(&r[i - 1] , &r[i - 1], tmparr); 
				if (bdValid){
					d[i] = mid;
					if (!flag){
						d[0] = i;
						flag = 1;
					}
				}
			}
			if (iszero(r[i - 1])) m = i - 1;

		}

		r[i - 1] = tmp;
		while (r[m] == 0) --m;
	}

	if (tmparr0 == NULL) free(tmparr);

	r[0] = m * _signs;
	if (_s_reserve && r0 == NULL) free(r);

	if (_s_reserve) s[0] *= _signs;

	if (s != t) t[0] *= _signt;
	if (bdValid) d[0] *= _sign;

	return d;
}


///////////////////// �߾����� / ��������, d = s / t, r = s % t��
//	(r[] != NULL ʱ�ṩ��������ռ�, return_r != NULL ʱ���ص������̵� *return_r).
int *CBigNumber::div(int d[], int s[], int t, int r[], int *return_r, int _len, int _len_r)
{
	if (d == NULL && r == NULL && return_r == NULL) return NULL;
	int bdValid = (d != NULL);

	if (iszero(t)) return NULL;
	if (iszero(s)){
		if (bdValid) d[0] = 0;
		if (r) r[0] = 0;
		return d;
	}

	int _signs = sign(s), _signt = sign(t);
	int _sign = _signs * _signt;
	int n1(s[0] = abs(s[0]));
	t = abs(t);
	
	if (bdValid && _len != 0 && _len < n1 + 1) return NULL;

	int *r0 = r;
	if (r == NULL){
		r = (int *)malloc((n1 + 1) * sizeof(int));
	}else
		if (_len_r != 0 && _len_r < n1 + 1) return NULL;

	memcpy(r + 1, s + 1, n1 * sizeof(int));
	r[0] = n1;

	int i,m = n1,tmp;//m �������� r ��ʣ��λ

	/*for (i = n1; i >= 1; --i){
		if (i == m) tmp = r[i];
		else tmp = r[m] * BASE + r[i];

		if (tmp >= t){
			if (bdValid) d[i] = tmp / t;
			r[i] = tmp % t;
			if (tmp >= BASE) r[i + 1] = 0;
			m = i;
		}else
			if (bdValid) d[i] = 0;
	}*/
	for (i = n1; i >= 1; --i){
		if (i == m) tmp = r[i];
		else{
			tmp = r[m] * BASE + r[i];
			r[m] = 0;
		}
		if (tmp >= t){
			if (bdValid) d[i] = tmp / t;
			if (r[i] = tmp % t) m = i;
			else m = i - 1;
		}else
			if (bdValid) d[i] = 0;
	}

	r[0] = m * _signs;
	if (return_r) {
		if (iszero(r)) *return_r = 0;	
		else *return_r = r[1] * _signs;
	}
	if (r0 == NULL) free(r);
	
	if (bdValid){
		d[0] = n1;
		//if (s[n1] < t) --d[0];
		if (d[n1] == 0) --d[0];
		d[0] *= _sign;
	}

	//s[0] *= _signs;

	return d;
}

///////////////////// �߾����� / �������� (��Ϊ��������, ���ظ� r).
int *CBigNumber::div(int d[], int s[], int t, int &r, int _len){
	return div(d, s, t, NULL, &r);
}
#pragma endregion

#pragma region Assistant Functions

int CBigNumber::_getchar(int push_back)
{
	int c;
	while (1){
		c = getchar();
		if (!(c == ' ' || c == '\n' || c == '\t'))
			break;
	}
	if (push_back) ungetc(c,stdin);
	return c;
}

int CBigNumber::_strlen(const char *s)
{
	if (s == NULL) return 0;
	if (s[0] != '+' && s[0] != '-' && !isdigit(s[0])) return 0;
	int i = 0;	
	while (isdigit(s[++i]));
	return i;
}

//���ַ��� c ת���� �߾�����Array a[].
int *CBigNumber::conv(int a[], const char* s, int _rescan, int *_strlength, int *_maxlen) {

	if (a == NULL) return NULL;
	if (s == NULL) return a[0] = 0, a;

	a[0] = 1;
	if (s[0] == '+') ++s;
	else if (s[0] == '-') a[0] = -1, ++s;
	else if (!isdigit(s[0])) return NULL;

	int i,l,n;

	if (_rescan) l = _strlen(s) - 1;
	else l = (_strlength == NULL ? 0 : *_strlength);
	if (l == 0) l = strlen(s) - 1;
	if (_strlength) *_strlength = l;

	n = l / NLEN + 1;

	if (_maxlen != NULL && *_maxlen < n + 1){
		*_maxlen = n + 1;
		return NULL;
	}

	memset(a + 1, 0, n * sizeof(int));

	for(i = 0; i <= l; ++i)
		a[(l - i) / NLEN + 1] = a[(l - i) / NLEN + 1] * 10 + s[i] - '0';
	
	while (a[n] == 0) --n;

	a[0] *= n;
	return a;
}
//��32λ���� _t ת���ɴ���a[]
int *CBigNumber::conv(int a[], int _t, int _len)
{
	if (a == NULL) return NULL;
	a[0] = 0;
	int _sign = sign(_t);
	_t = abs(_t);
	while (_t > 0){
		++ a[ 0 ];
		if (_len != 0 && a[0] > _len - 1) return NULL;
		a [ a[ 0 ] ] = _t % BASE;
		_t /= BASE;
	}
	if (_sign < 0) a[0] *= -1;
	return a;
}
//����ת���� ��ֵ����
template <typename _Ty>
_Ty CBigNumber::conv(int a[])
{
	_Ty t = 0;
	for (int i = abs(a[0]); i >= 1; --i)	t = t * BASE + a[i];
	return t * sign(a);
}
#pragma endregion

#pragma region IO Functions

//=================== ��׼�ӿ����� ======================
int CBigNumber::read(const char *s, int _rescan)
{
	int n = this->nAllocCounts, l = 0;
	if (n == 0) this->_resize(n = 1);
	if (conv(this->pValueArray, s, _rescan, &l, &n) == NULL){
		this->_resize(n);
		return conv(this->pValueArray, s, 0, &l, &n) != NULL; 
	}else return 1;
}
int CBigNumber::readin(int _max_len, int _rescan){
	BufferAlloc(ReaderBuffer, nReaderBufferSize, _max_len);
	if (scanf("%s", ReaderBuffer) != 1) return 0;
	return read(ReaderBuffer, _rescan);
}

//��ӡ�߾����� s ����׼��� (�� _noleading0 == 0 ʱ ��0��䵽NLEN�ı���).
void CBigNumber::print(int s[], int _noleading0)
{
	if (s == NULL) return ;

	if (iszero(s)) {
		putchar('0');
		return;
	}
	if (s[0] < 0) putchar('-');

	int i = abs(s[0]);
	
	if (_noleading0)
		printf("%d", s[i--]);
	else
		printf("%.*d", NLEN, s[i--]);

	while (i >= 1){
		printf("%.*d",NLEN,s[i--]);
	}
}

istream& operator >> (istream &_is, CBigNumber &_bn)
{
	_is >> noskipws;
	string s;
	char c;
	bool bLeadingSpace = true;
	while (_is >> c){
		if (!isdigit(c)){
			if (bLeadingSpace && isspace(c));
			else break;
		}else{
			bLeadingSpace = false;
			s += c;
		}
	}
	if (_is) _is.putback(c);
	_bn.read(s.c_str());
	_is >> skipws;
	return _is;
}
ostream& operator << (ostream &_os, const CBigNumber &_bn)
{
	if (_bn == 0) {_os << 0; return _os;}
	if (_bn[0] < 0) _os <<'-';
	int i = abs(_bn[0]);
	_os << _bn[i--];
	while (i >= 1) _os << setw(CBigNumber::NLEN) << setfill('0') << _bn[i--];
	return _os;
}

#pragma endregion

//ԭ������������ ������Ҫ��DLL���������Ը�Ϊ������

#pragma region Simple Member Functions
	
	int CBigNumber::operator == (const CBigNumber &_bn)const	{return cmp(this->pValueArray, _bn.pValueArray) == 0;}
	int CBigNumber::operator != (const CBigNumber &_bn)const	{return cmp(this->pValueArray, _bn.pValueArray) != 0;}
	int CBigNumber::operator <  (const CBigNumber &_bn)const	{return cmp(this->pValueArray, _bn.pValueArray)  < 0;}
	int CBigNumber::operator >  (const CBigNumber &_bn)const	{return cmp(this->pValueArray, _bn.pValueArray)  > 0;}
	int CBigNumber::operator <= (const CBigNumber &_bn)const	{return cmp(this->pValueArray, _bn.pValueArray) <= 0;}
	int CBigNumber::operator >= (const CBigNumber &_bn)const	{return cmp(this->pValueArray, _bn.pValueArray) >= 0;}

	int CBigNumber::operator == (const int &_t)const	{return cmp(this->pValueArray, _t) == 0;}
	int CBigNumber::operator != (const int &_t)const	{return cmp(this->pValueArray, _t) != 0;}
	int CBigNumber::operator  < (const int &_t)const	{return cmp(this->pValueArray, _t)  < 0;}
	int CBigNumber::operator  > (const int &_t)const	{return cmp(this->pValueArray, _t)  > 0;}
	int CBigNumber::operator <= (const int &_t)const	{return cmp(this->pValueArray, _t) <= 0;}
	int CBigNumber::operator >= (const int &_t)const	{return cmp(this->pValueArray, _t) >= 0;}


	//�������ݽӿ�
	int* CBigNumber::GetValuePointer()		 const	{return this->pValueArray;}
	int& CBigNumber::operator [] (int _index)const	{return this->pValueArray[_index];}
	int  CBigNumber::NumDigits()			 const	{return decdigits(this->pValueArray);}

	//�������
	void CBigNumber::print	(int _noleading0)const	{print(this->pValueArray, _noleading0);}
	void CBigNumber::println(int _noleading0)const	{print(_noleading0); putchar('\n');}

#pragma endregion 

#include <iostream>
#include <vector>
#include <string>
#include <memory>
#include <algorithm>
using namespace std;

#define ONLINE


typedef __int64 hugeint;

const int Base = 1000000000;
const int Capacity = 1500;

struct xnum
{
	int Len;
	int Data[Capacity];
	xnum() : Len(0) {}
	xnum(const xnum& V) : Len(V.Len) { memcpy(Data, V.Data, Len * sizeof *Data); }
	xnum(int V) : Len(0) { for (; V > 0; V /= Base) Data[Len++] = V % Base; }
	xnum& operator=(const xnum& V) { Len = V.Len; memcpy(Data, V.Data, Len * sizeof *Data); return *this; }
	int& operator[](int Index) { return Data[Index]; }
	int operator[](int Index) const { return Data[Index]; }
}buf1, buf2;

vector<xnum> Input;

int compare(const xnum& A, const xnum& B)
{
	int I;
	if (A.Len != B.Len) return A.Len > B.Len ? 1 : -1;
	for (I = A.Len - 1; I >= 0 && A[I] == B[I]; I--);
	if (I < 0) return 0;
	return A[I] > B[I] ? 1 : -1;
}

xnum operator+(const xnum& A, const xnum& B)
{
	xnum R;
	int I;
	int Carry = 0;
	for (I = 0; I < A.Len || I < B.Len || Carry > 0; I++)
	{
		if (I < A.Len) Carry += A[I];
		if (I < B.Len) Carry += B[I];
		R[I] = Carry % Base;
		Carry /= Base;
	}
	R.Len = I;
	return R;
}

xnum operator-(const xnum& A, const xnum& B)
{
	xnum R;
	int Carry = 0;
	R.Len = A.Len;
	int I;
	for (I = 0; I < R.Len; I++)
	{
		R[I] = A[I] - Carry;
		if (I < B.Len) R[I] -= B[I];
		if (R[I] < 0) Carry = 1, R[I] += Base;
		else Carry = 0;
	}
	while (R.Len > 0 && R[R.Len - 1] == 0) R.Len--;
	return R;
}

xnum operator*(const xnum& A, const int B)
{
	int I;
	if (B == 0) return 0;
	xnum R;
	hugeint Carry = 0;
	for (I = 0; I < A.Len || Carry > 0; I++)
	{
		if (I < A.Len) Carry += hugeint(A[I]) * B;
		R[I] = Carry % Base;
		Carry /= Base;
	}
	R.Len = I;
	return R;
}

xnum operator*(const xnum& A, const xnum& B)
{
	int I;
	if (B.Len == 0) return 0;
	xnum R;
	for (I = 0; I < A.Len; I++)
	{
		hugeint Carry = 0;
		for (int J = 0; J < B.Len || Carry > 0; J++)
		{
			if (J < B.Len) Carry += hugeint(A[I]) * B[J];
			if (I + J < R.Len) Carry += R[I + J];
			if (I + J >= R.Len) R[R.Len++] = Carry % Base;
			else R[I + J] = Carry % Base;
			Carry /= Base;
		} 
	}
	return R;
}

xnum operator/(const xnum& A, const int B)
{
	xnum R;
	int I;
	hugeint C = 0;
	for (I = A.Len - 1; I >= 0; I--)
	{
		C = C * Base + A[I];
		R[I] = C / B;
		C %= B;
	}
	R.Len = A.Len;
	while (R.Len > 0 && R[R.Len - 1] == 0) R.Len--;
	return R;
}

xnum operator/(const xnum& A, const xnum& B)
{
	int I;
	xnum R, Carry = 0;
	int Left, Right, Mid;
	for (I = A.Len - 1; I >= 0; I--)
	{
		Carry = Carry * Base + A[I];
		Left = 0;
		Right = Base - 1;
		while (Left < Right)
		{
			Mid = (Left + Right + 1) / 2;
			if (compare(B * Mid, Carry) <= 0) Left = Mid;
			else Right = Mid - 1;
		}
		R[I] = Left;
		Carry = Carry - B * Left;
	}
	R.Len = A.Len;
	while (R.Len > 0 && R[R.Len - 1] == 0) R.Len--;
	return R;
}
xnum operator%(const xnum& A, const xnum& B)
{
	int I;
	xnum R, Carry = 0;
	int Left, Right, Mid;
	for (I = A.Len - 1; I >= 0; I--)
	{
		Carry = Carry * Base + A[I];
		Left = 0;
		Right = Base - 1;
		while (Left < Right)
		{
			Mid = (Left + Right + 1) / 2;
			if (compare(B * Mid, Carry) <= 0) Left = Mid;
			else Right = Mid - 1;
		}
		R[I] = Left;
		Carry = Carry - B * Left;
	}
	R.Len = A.Len;
	while (R.Len > 0 && R[R.Len - 1] == 0) R.Len--;
	return Carry;
}

istream & operator>>(istream& In, xnum& V)
{
	char Ch;
	for (V = 0; In >> Ch;)
	{
		V = V * 10 + (Ch - '0');
		if (cin.peek() <= ' ') break;
	}
	return In;
}

ostream& operator<<(ostream& Out, const xnum& V)
{
	int I;
	Out << (V.Len == 0 ? 0 : V[V.Len - 1]);
	for (I = V.Len - 2; I >= 0; I--) for (int J = Base / 10; J > 0; J /= 10) printf("%d", V[I] / J % 10);
	return Out;
}


vector<xnum> vec1;

bool cmp(xnum a, xnum b)
{
	if(compare(a, b) > 0) return true;
	return false;
}

xnum GCD(xnum a, xnum b)
{
	xnum w = a, u = b, r;
	do
	{
		r = w % u;
		w = u;
		u = r;
	}while(compare(r, 0) != 0);
	
	return w;
}

int main()
{
#ifdef ONLINE
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
#endif

	int iCaseTimes, i, j, iNum;

	//scanf("%d", &iCaseTimes);
	cin >> iCaseTimes;

	for(int k = 0; k < iCaseTimes; k++)
	{
		cin >> iNum;
		Input.clear();
		for(int i = 0; i < iNum; i++)
		{
			cin >> buf1;
			Input.push_back(buf1);
		}
		vec1.clear();
		sort(Input.begin(), Input.end(), cmp);
		

		for(int i = 1; i < Input.size(); i++)
			vec1.push_back(Input[i - 1] - Input[i]);

		//for(int i = 0; i < Input.size(); i++)
		//	cout << Input[i] << endl;
		//for(int i = 0; i < vec1.size(); i++)
			//cout << vec1[i] << endl;

		xnum T = vec1[0];
		//cout << "*****" << T << endl;
		for(int i = 0; i < vec1.size(); i++)
		{
			T = GCD(T, vec1[i]);
			//cout << T << endl;
		}


		xnum Y, A1(Input[0]), A2(Input[1]);

		if(compare(A1 % T, 0) == 0) cout << "Case #"<< k + 1 << ": " << 0 << endl;
		else
			cout << "Case #"<< k + 1 << ": " << T - A1 % T << endl;
		//cout << T - A2 % T << endl;

		//cout << Y << endl;

		//cout << T << endl;
	}
	return 0;
}
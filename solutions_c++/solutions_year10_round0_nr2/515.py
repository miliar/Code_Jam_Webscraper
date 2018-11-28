/*
	大数模版 xnum.cpp
	功能 : 大数加减，大数比较，大数乘小数，大数乘大数，大数除小数，大数除大数，大数模运算，大数gcd
	注意 : 此模版不支持负数！！！
	全局变量 ： Base 进制
				Capacity 数组容量，至少应为 大数最大长度 / (Base长度 － 1)
				DLEN 每个元素的最大长度，与 Base 相对应

*/
#include <iostream>
using namespace std;
typedef int hugeint;

const int Base = 10000; //定义进制，应不大于10000，否则乘法可能溢出
const int Capacity = 1000; //定义数组容量
const int DLEN = 4;

struct xnum
{
	int Len;
	int Data[Capacity];
	xnum() : Len(0) {}
	xnum(const xnum& V) : Len(V.Len) { memcpy(Data, V.Data, Len * sizeof *Data); }
	xnum(int V) : Len(0) { for (; V > 0; V /= Base) Data[Len++] = V % Base; }
	xnum(char *str) ;
	xnum& operator=(const xnum& V) 
	{ 
		Len = V.Len; 
		memcpy(Data, V.Data, Len * sizeof *Data);
		return *this; 
	}
	int& operator[](int Index) { return Data[Index]; }
	int operator[](int Index) const { return Data[Index]; }
	void print()
	{ 
		int i,j;
		printf("%d",Len==0?0:Data[Len-1]);
		for(i=Len-2;i>=0;i--)
			for(j=Base/10;j>0;j/=10)
				printf("%d",Data[i]/j%10);
		printf("\n");
	}
};

int compare(const xnum& A, const xnum& B)
{
	int i;
	if (A.Len != B.Len) return A.Len > B.Len ? 1 : -1;
	for (i = A.Len - 1; i >= 0 && A[i] == B[i]; i--);
	if (i < 0) return 0;
	return A[i] > B[i] ? 1 : -1;
}

xnum operator+(const xnum& A, const xnum& B)
{
	xnum R;
	int i;
	int Carry = 0;
	for (i = 0; i < A.Len || i < B.Len || Carry > 0; i++)
	{
		if (i < A.Len) Carry += A[i];
		if (i < B.Len) Carry += B[i];
		R[i] = Carry % Base;
		Carry /= Base;
	}
	R.Len = i;
	return R;
}

xnum operator-(const xnum& A, const xnum& B)
{
	xnum R;
	int Carry = 0;
	R.Len = A.Len;
	int i;
	for (i = 0; i < R.Len; i++)
	{
		R[i] = A[i] - Carry;
		if (i < B.Len) R[i] -= B[i];
		if (R[i] < 0) Carry = 1, R[i] += Base;
		else Carry = 0;
	}
	while (R.Len > 0 && R[R.Len - 1] == 0) R.Len--;
	return R;
}

xnum operator*(const xnum& A, const int B)
{
	int i;
	if (B == 0) return 0;
	xnum R;
	hugeint Carry = 0;
	for (i = 0; i < A.Len || Carry > 0; i++)
	{
		if (i < A.Len) Carry += hugeint(A[i]) * B;
		R[i] = Carry % Base;
		Carry /= Base;
	}
	R.Len = i;
	return R;
}

xnum::xnum(char *str)
{
	int i, j;
	int lst[] = {1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000};
	j = Len = 0;
	memset(Data, 0, sizeof(Data));
	for(i = strlen(str) - 1; i >= 0; --i, ++j)
	{
		if(j >= DLEN)
		{
			j = 0;
			Len++;
		}
		Data[Len] += lst[j] * (str[i] - '0');
	}
	Len++;
	// to process strings such as "0000000001101001"
	while(Len > 1 && Data[Len - 1] == 0) Len--;
}

xnum operator*(const xnum& A, const xnum& B)
{
	int i , j;
	if (B.Len == 0) return 0;
	xnum R;
	for (i = 0; i < A.Len; i++)
	{
		hugeint Carry = 0;
		for (j = 0; j < B.Len || Carry > 0; j++)
		{
			if (j < B.Len) Carry += hugeint(A[i]) * B[j];
			if (i + j < R.Len) Carry += R[i + j];
			if (i + j >= R.Len) R[R.Len++] = Carry % Base;
			else R[i + j] = Carry % Base;
			Carry /= Base;
		}   
	}
	return R;
}

xnum operator/(const xnum& A, const int B)
{
	xnum R;
	int i;
	hugeint C = 0;
	for (i = A.Len - 1; i >= 0; i--)
	{
		C = C * Base + A[i];
		R[i] = C / B;
		C %= B;
	}
	R.Len = A.Len;
	while (R.Len > 0 && R[R.Len - 1] == 0) R.Len--;
	return R;
}

xnum operator/(const xnum& A, const xnum& B)
{
	int i;
	xnum R, Carry = 0;
	int Left, Right, Mid;
	for (i = A.Len - 1; i >= 0; i--)
	{
		Carry = Carry * Base + A[i];
		Left = 0;
		Right = Base - 1;
		while (Left < Right)
		{
			Mid = (Left + Right + 1) / 2;
			if (compare(B * Mid, Carry) <= 0) Left = Mid;
			else Right = Mid - 1;
		}
		R[i] = Left;
		Carry = Carry - B * Left;
	}
	R.Len = A.Len;
	while (R.Len > 0 && R[R.Len - 1] == 0) R.Len--;
	return R;
}

xnum operator%(const xnum& A, const xnum& B)
{
	int i;
	xnum R, Carry = 0;
	int Left, Right, Mid;
	for (i = A.Len - 1; i >= 0; i--)
	{
		Carry = Carry * Base + A[i];
		Left = 0;
		Right = Base - 1;
		while (Left < Right)
		{
			Mid = (Left + Right + 1) / 2;
			if (compare(B * Mid, Carry) <= 0) Left = Mid;
			else Right = Mid - 1;
		}
		R[i] = Left;
		Carry = Carry - B * Left;
	}
	R.Len = A.Len;
	while (R.Len > 0 && R[R.Len - 1] == 0) R.Len--;
	return Carry;
}

xnum gcd(xnum a,xnum b)
{
	if(compare(b,0)==0) return a;
	else return gcd(b,a%b); 
}

void swap(xnum &a,xnum &b)
{
    xnum t=a;
    a=b;
    b=t;
}

char s[10000];
xnum a,b,ans,d;

int main()
{
    int t,cs,n,i;
    freopen("C:\\Users\\LL\\Desktop\\B-small-attempt0.in","r",stdin);
    freopen("C:\\Users\\LL\\Desktop\\2.out","w",stdout);
    scanf("%d",&t);
    for(cs=1;cs<=t;cs++)
    {
        printf("Case #%d: ",cs);
        scanf("%d",&n);
        scanf("%s",s);
        b=xnum(s);
        for(i=1;i<n;i++)
        {
            scanf("%s",s);
            a=xnum(s);
            if(compare(a,b)>0)
                d=a-b;
            else
                d=b-a;
            if(i==1)
                ans=d;
            else
                ans=gcd(d,ans);
            swap(a,b);
        }
        a=b%ans;
        if(compare(a,0)!=0)
            ans=ans-a;
        else
            ans=0;
        ans.print();
    }
}
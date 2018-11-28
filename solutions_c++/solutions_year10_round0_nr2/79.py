#include<iostream>
#include<algorithm>

using namespace std;
#define Base 1000000000
#define Cap 200
typedef long long hugeint;

struct bignum
{
    int Len;
    int Data[Cap];
    bignum() : Len(0) {}
    bignum(const bignum& V) : Len(V.Len){ memcpy(Data, V.Data, Len * sizeof *Data);}
    bignum(int V) : Len(0) { for (; V > 0; V /= Base) Data[Len++] = V % Base; }
    bignum& operator=(const bignum& V) { Len = V.Len;
                  memcpy(Data, V.Data, Len * sizeof *Data); return *this; }
    int& operator[](int Index) { return Data[Index]; }
    int operator[](int Index) const { return Data[Index]; }
};


int compare(const bignum& A, const bignum& B)
{
    int I;
    if (A.Len != B.Len) return A.Len > B.Len ? 1 : -1;
    for (I = A.Len - 1; I >= 0 && A[I] == B[I]; I--);
    if (I < 0) return 0;
    return A[I] > B[I] ? 1 : -1;
}

bignum operator+(const bignum& A, const bignum& B)
{
    bignum R;
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

bignum operator-(const bignum& A, const bignum& B)
{
    bignum R;
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

bignum operator*(const bignum& A, const int B)
{
    int I;
    if (B == 0) return 0;
    bignum R;
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

bignum operator*(const bignum& A, const bignum& B)
{
    int I;
    if (B.Len == 0) return 0;
    bignum R;
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

bignum operator/(const bignum& A, const int B)
{
    bignum R;
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

bignum operator/(const bignum& A, const bignum& B)
{
    int I;
    bignum R, Carry = 0;
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

bool operator==(const bignum& A, const bignum& B)
{
    int i;
    if(A.Len != B.Len)return 0;
    for(i=0;i<A.Len;i++)
    if(A.Data[i]!=B.Data[i])return 0;
    return 1;
}

bignum operator%(const bignum& A, const bignum& B)
{
    int I;
    bignum R, Carry = 0;
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

bignum pow(bignum a,int n)
{
    bignum tmp = a;
    while(--n)
       tmp = tmp * a;
    return tmp; 
}

istream& operator>>(istream& In, bignum& V)
{
    char Ch;
    for (V = 0; In >> Ch;)
    {
       V = V * 10 + (Ch - '0');
       if (cin.peek() <= ' ') break;
    }
    return In;
}

ostream& operator<<(ostream& Out, const bignum& V)
{
    int I;
    Out << (V.Len == 0 ? 0 : V[V.Len - 1]);
    for (I = V.Len - 2; I >= 0; I--)
    for (int J = Base / 10; J > 0; J /= 10)
        Out << V[I] / J % 10;
    return Out;
}

int n;
bignum a[1001];
bignum x[1001];

bignum GCD(bignum& x,bignum& y)
{
	bignum zero(0),tmp;
	if (compare(x,y)<0)
	{
		tmp = x;
		x = y;
		y = tmp;
	}
	while (compare(x % y,zero)!=0)
	{
		tmp = x;
		x = y;
		y = tmp % y;
	}
	return y;
}

int main()
{
	int T,Case;
	int i,j;
	scanf("%d",&T);
	for(Case = 1;Case <= T; Case++) {
		printf("Case #%d: ",Case);
		scanf("%d",&n);
		for(i=0;i<n;i++) {
			cin >> a[i];
		}
		int k = 0;
		for(i=0;i<n-1;i++) {
				if(compare(a[i],a[i+1])>0) x[i] = a[i] - a[i+1];
				else x[i] = a[i+1] - a[i];
			}
		bignum ngcd;
		if(n>=3) {
			ngcd = GCD(x[0],x[1]);
			for(i=2;i<n-1;i++) {
				ngcd = GCD(ngcd,x[i]);
			}
		} else {
			ngcd = x[0];
		}
		if(ngcd == 1) {
			printf("0\n");
		} else {
			if(compare(a[0]%ngcd,0)==0) cout << 0 << endl;
			else cout << ngcd - a[0]%ngcd << endl;
		}
	}
	return 0;	
}

#define _CRT_SECURE_NO_DEPRECATE
#pragma warning(disable: 4018)
#ifdef NDEBUG
	#define _SECURE_SCL 0
#endif
#include <iostream>
#include <memory>
#include <vector>
#include <algorithm>
#include <string>
#include <map>
#include <set>
#include <sstream>
#include <utility>
#include <functional>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cassert>

using namespace std;

typedef long long hugeint;

const int Base = 1000000000;
const int Capacity = 20;

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
};

int compare(const xnum& A, const xnum& B)
{
	if (A.Len != B.Len) return A.Len > B.Len ? 1 : -1;
	int I;
	for (I = A.Len - 1; I >= 0 && A[I] == B[I]; I--);
	if (I < 0) return 0;
	return A[I] > B[I] ? 1 : -1;
}

xnum operator+(const xnum& A, const xnum& B)
{
	xnum R;
	int I, Carry = 0;
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
	for (int I = 0; I < R.Len; I++)
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
	if (B == 0) return 0;
	xnum R;
	hugeint Carry = 0;
	int I;
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
	if (B.Len == 0) return 0;
	xnum R;
	for (int I = 0; I < A.Len; I++)
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
	hugeint C = 0;
	for (int I = A.Len - 1; I >= 0; I--)
	{
		C = C * Base + A[I];
		R[I] = int(C / B);
		C %= B;
	}
	R.Len = A.Len;
	while (R.Len > 0 && R[R.Len - 1] == 0) R.Len--;
	return R;
}

xnum operator/(const xnum& A, const xnum& B)
{
	xnum R, Carry = 0;
	int Left, Right, Mid;
	for (int I = A.Len - 1; I >= 0; I--)
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

istream& operator>>(istream& In, xnum& V)
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
	Out << (V.Len == 0 ? 0 : V[V.Len - 1]);
	for (int I = V.Len - 2; I >= 0; I--) for (int J = Base / 10; J > 0; J /= 10) Out << V[I] / J % 10;
	return Out;
}

int NN, TT;
int N;
xnum P[1000];

xnum gcd(xnum A, xnum B)
{
	while (compare(A, 0) != 0)
	{
		xnum C = B - B / A * A;
		B = A;
		A = C;
	}
	return B;
}

int main()
{
	cin >> NN;
	for (TT = 1; TT <= NN; TT++)
	{
		cin >> N;
		for (int I = 0; I < N; I++) cin >> P[I];
		xnum M = 0;
		for (int I = 0; I < N - 1; I++)
		{
			xnum Temp;
			if (compare(P[I], P[I + 1]) < 0) Temp = P[I + 1] - P[I];
			else Temp = P[I] - P[I + 1];
			if (I == 0) M = Temp;
			else M = gcd(M, Temp);
		}
		xnum Temp = P[0] - P[0] / M * M;
		if (compare(Temp, 0) != 0) Temp = M - Temp;
		cout << "Case #" << TT << ": " << Temp << endl;
	}
	return 0;
}
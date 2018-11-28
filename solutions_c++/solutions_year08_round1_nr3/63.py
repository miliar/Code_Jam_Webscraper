#define _CRT_SECURE_NO_DEPRECATE
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <utility>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>

using namespace std;

const int Base = 1000000000;
const int Capacity = 1000;

struct xnum
{
	int Len;
	int Data[Capacity];
	xnum() : Len(0) {}
	xnum(const xnum& V) : Len(V.Len) { memcpy(Data, V.Data, Len * sizeof *Data); }
	xnum(long long V) : Len(0) { for (; V > 0; V /= Base) Data[Len++] = V % Base; }
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
	long long Carry = 0;
	int I;
	for (I = 0; I < A.Len || Carry > 0; I++)
	{
		if (I < A.Len) Carry += long long(A[I]) * B;
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
		long long Carry = 0;
		for (int J = 0; J < B.Len || Carry > 0; J++)
		{
			if (J < B.Len) Carry += long long(A[I]) * B[J];
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
	long long C = 0;
	for (int I = A.Len - 1; I >= 0; I--)
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

int TT, NN;
int N;

int main()
{
	//5.236067977 499789696 409173668 7313
	xnum Base;
	Base.Len = 5;
	Base[4] = 5;
	Base[3] = 236067977;
	Base[2] = 499789696;
	Base[1] = 409173668;
	Base[0] = 7313;
	cin >> TT;
	for (NN = 1; NN <= TT; NN++)
	{
		cin >> N;
		xnum V = Base;
		for (int I = 0; I < N - 1; I++) V = V * Base;
		printf("Case #%d: %03d\n", NN, V[4 * N] % 1000);
	}
	return 0;
}

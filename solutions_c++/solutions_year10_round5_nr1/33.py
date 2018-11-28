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

int NN, TT;
const int MaxPrime = 1100000;
bool IsPrimes[MaxPrime + 1];
int N, D;
int P[100];

int power_mod(int A, int B, int C) // return A^B mod C
{
	int R = 1, D = A % C;
	while (B > 0)
	{
		if (B % 2 == 1) R = (long long)(R) * D % C;
		D = (long long)(D) * D % C;
		B /= 2;
	}
	return R;
}

int adjust(int A, int Prime)
{
	while (A < 0) A += Prime;
	while (A >= Prime) A -= Prime;
	return A;
}

void solve(int X1, int X2, int X3, int Prime, int& A, int& B)
{
	if (X1 == X2 || X2 == X3)
	{
		A = 1;
		B = 0;
		return;
	}
	A = int((long long)adjust(X3 - X2, Prime) * power_mod(adjust(X2 - X1, Prime), Prime - 2, Prime) % Prime);
	B = adjust(int(X2 - (long long)A * X1 % Prime), Prime);
}

int try_prime(int Prime)
{
	int A, B;
	for (int I = 0; I < N; I++) if (P[I] >= Prime) return -1;
	solve(P[0], P[1], P[2], Prime, A, B);
	for (int I = 0; I < N - 1; I++)
	{
		int Temp = int(((long long)A * P[I] + B) % Prime);
		if (P[I + 1] != Temp) return -1;
	}
	return int(((long long)A * P[N - 1] + B) % Prime);
}

void output(int TT, int Ans)
{
	cout << "Case #" << TT << ": ";
	if (Ans >= 0) cout << Ans;
	else cout << "I don't know.";
	cout << endl;
}

int main()
{
	cin >> NN;
	memset(IsPrimes, 1, sizeof(IsPrimes));
	IsPrimes[0] = IsPrimes[1] = false;
	for (int I = 2; I * I <= MaxPrime; I++) if (IsPrimes[I])
		for (int J = I * I; J <= MaxPrime; J += I)
			IsPrimes[J] = false;
	for (TT = 1; TT <= NN; TT++)
	{
		cin >> D >> N;
		for (int I = 0; I < N; I++) cin >> P[I];
		if (N == 1)
		{
			output(TT, -1);
			continue;
		}
		if (P[N - 1] == P[N - 2])
		{
			output(TT, P[N - 1]);
			continue;
		}
		if (N == 2)
		{
			output(TT, -1);
			continue;
		}
		bool NoAns = false;
		int Ans = -1;
		int Bound = 1;
		for (int I = 0; I < D; I++) Bound *= 10;
		for (int Prime = 2; Prime <= Bound; Prime++) if (IsPrimes[Prime])
		{
			int Temp = try_prime(Prime);
			if (Temp < 0) continue;
			if (Ans < 0)
				Ans = Temp;
			else if (Temp != Ans)
				NoAns = true;
		}
		if (Ans < 0 || NoAns) output(TT, -1);
		else output(TT, Ans);
	}
	return 0;
}
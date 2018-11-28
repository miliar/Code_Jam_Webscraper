#define _CRT_SECURE_NO_DEPRECATE
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <utility>
#include <functional>
#include <cstdio>
#include <cstdlib>
#include <cstring>

using namespace std;

long long NN, TT;
long long N, M;
bool Swapped;
long long Area;

long long gcd(long long A, long long B, long long& S, long long& T)
{
	if (A == 0)
	{
		S = 0;
		T = 1;
		return B;
	}
	long long R = gcd(B % A, A, T, S);
	S -= B / A * T;
	return R;
}

int main()
{
	cin >> NN;
	for (TT = 1; TT <= NN; TT++)
	{
		cin >> N >> M >> Area;
		cout << "Case #" << TT << ": ";
		bool Found = false;
		for (long long X1 = 1; X1 <= N && !Found; X1++)
			for (long long X2 = 0; X2 <= N && !Found; X2++)
				for (long long Y1 = 0; Y1 <= M && !Found; Y1++)
			{
				long long Temp = Area + X2 * Y1;
				if (Temp % X1 != 0) continue;
				long long Y2 = Temp / X1;
				if (Y2 > M) continue;
				cout << "0 0 " << X1 << " " << Y1 << " " << X2 << " " << Y2 << endl;
				Found = true;
			}
		if (!Found) cout << "IMPOSSIBLE" << endl;
	}
	return 0;
}

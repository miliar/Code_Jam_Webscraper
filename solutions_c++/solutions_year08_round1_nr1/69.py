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

int TT, NN;
int N;
int P1[1000], P2[1000];

int main()
{
	cin >> TT;
	for (NN = 1; NN <= TT; NN++)
	{
		cin >> N;
		for (int I = 0; I < N; I++) cin >> P1[I];
		for (int I = 0; I < N; I++) cin >> P2[I];
		sort(P1, P1 + N);
		sort(P2, P2 + N, greater<int>());
		long long Result = 0;
		for (int I = 0; I < N; I++) Result += (long long)P1[I] * P2[I];
		cout << "Case #" << NN << ": " << Result << endl;
	}
	return 0;
}

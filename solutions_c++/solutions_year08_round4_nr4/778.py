#include <string>
#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;

const int inf = 500000000;
int a[10];

string S, nS;

int main()
{
	int N;
	cin >> N;
	for (int _N = 1; _N <= N; _N ++)
	{
		int D;
		cin >> D >> S;
		nS = S;
		int L = S.size(); int M = L / D;
		for (int i = 0; i < D; i ++) a[i] = i;
		int ans = inf;
		while (1)
		{
			for (int i = 0; i < M; i ++)
				for (int j = 0; j < D; j ++)
					nS[i * D + j] = S[i * D + a[j]];
			int cnt = 1;
			for (int i = 1; i < L; i ++)
				if (nS[i] != nS[i - 1]) cnt ++;
			ans = min(ans, cnt);
			if (!next_permutation(a, a + D)) break; 
		}
		printf("Case #%d: %d\n", _N, ans);
	}
}

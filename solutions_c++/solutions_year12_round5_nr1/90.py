#include <stdio.h>
#include <iostream>
#include <vector>
#include <algorithm>
#include <math.h>
#include <queue>
#include <string>
#include <memory.h>



using namespace std;
struct S
{
	long long P, L, I;
};

bool operator < (S & a, S & b)
{
	long long x = a.P * b.L;
	long long y = a.L * b.P;
	if (x < y)
		return true;
	if (x == y && a.I > b.I)
		return true;
	return false;
}

int main()
{
	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);

	int T;
	scanf("%d", &T);
	for (int t = 0; t < T; t++)
	{
		int N;
		scanf("%d", &N);
		vector<S> v(N);
		for (int i = 0; i < N; i++)
		{
			int l;
			scanf("%d", &l);
			v[i].L = l;
			v[i].I = i;
		}
		for (int i = 0; i < N; i++)
		{
			int p;
			scanf("%d", &p);
			v[i].P = p;
		}
		sort(v.begin(), v.end());
		//Case #1: 0 2 3 1
		printf("Case #%d:", t+1);
		for (int i = N - 1; i >= 0; i--)
			printf(" %lld", v[i].I);
		printf("\n");
	}

	fclose(stdin);
	fclose(stdout);

	return 0;
}
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <assert.h>
#include <time.h>
#include <math.h>

#include <algorithm>
#include <vector>
#include <stack>
#include <queue>
#include <functional>
#include <string>
#include <set>
#include <map>
#include <iostream>


using namespace std;
const int inf = 0x7fffffff;
const double eps = 10e-5;

const int MAX_N = 1000;
int n;
vector<int> V[1000]; // veze
int U[1000]; // koliko ide u njega
int P[1000][1000]; // pamti

int rek(int poc, int tre)
{
	int i;
	if (P[poc][tre] == 1) return 1;
	P[poc][tre] = 1;
	
	for (i = 0; i < (int)V[tre].size(); i++) {
		if (rek(poc, V[tre][i])) return 1;
	}
	return 0;
}

int main()
{
	int t;
	int i;
	scanf("%d", &t);
	for (int tt = 0; tt < t; tt++)
	{
		// reset all vars
		memset(U, 0, sizeof U);
		memset(P, 0, sizeof P);
		for (i = 0; i < 1000; i++) V[i].clear();
		
		scanf("%d", &n);
		for (i = 0; i < n; i++)
		{
			int l, v;
			scanf("%d", &l);
			for (int j = 0; j < l; j++)
			{
				scanf("%d", &v); v--;
				V[i].push_back(v);
				U[v]++;
			}
		}
		for (i = 0; i < n; i++)
		{
			if (U[i] > 0) continue;
			if (rek(i, i)) {
				printf("Case #%d: Yes\n", tt+1);
				break;
			}
		}
		if (i == n) printf("Case #%d: No\n", tt+1);
	}
	
	return 0;
}


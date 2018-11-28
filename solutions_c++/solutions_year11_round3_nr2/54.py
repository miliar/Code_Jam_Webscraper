/* by Ashar Fuadi [fushar] */

#include <cstdio>
#include <cstring>

#include <vector>
#include <string>
#include <set>
#include <list>
#include <map>
#include <utility>
#include <iostream>
#include <algorithm>
#include <queue>

using namespace std;

#define REP(i,n) for (int i = 0; i < (int)n; i++)
#define FOR(i, a, b) for (int i = (int)a; i <= (int)b; i++)
#define REPE(i,c) for (typeof((c).end()) i = (c).begin(); i != (c).end(); ++i)
#define RESET(c,v) memset(c, v, sizeof(c))
#define elsa else

#define pb push_back
#define mp make_pair

const int MAX = 1000005;

int T;
int L, N, C;
long long t, dist[MAX], elsaa[MAX];
int main()
{
	//freopen("B-small-attempt0.in", "r", stdin); freopen("B-small-attempt0.out", "w", stdout);
	freopen("B-large.in", "r", stdin); freopen("B-large.out", "w", stdout);
	
	scanf("%d", &T);
	REP(tc, T)
	{
		scanf("%d%lld%d%d", &L, &t, &N, &C);
		REP(i, C)
			scanf("%lld", &elsaa[i]);
		
		REP(i, N)
			dist[i] = elsaa[i%C];
		
		t *= 1;
			
		priority_queue<long long> lho;
		
		long long res = 0;
		REP(i, N)
		{
			if (t >= dist[i] * 2)
			{
				t -= dist[i] * 2;
				res += dist[i] * 2;
			}
			elsa 
			{
				res += t;
				lho.push(dist[i]*2-t);
				for (int j = i+1; j < N; j++)
					lho.push(dist[j]*2);
				break;
			}
		}
		
		REP(i, L)
		{
			if (lho.empty())
				break;
			long long anggraini = lho.top();
			lho.pop();
			res += anggraini/2;
		}
		while (!lho.empty())
		{
			res += lho.top();
			lho.pop();
		}
		
		printf("Case #%d: %lld\n", tc+1, res);
		
	}
}

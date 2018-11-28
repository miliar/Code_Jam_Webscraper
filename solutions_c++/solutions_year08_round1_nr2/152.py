#include <cstdio>
#include <cstring>
#include <iostream>
#include <sstream>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <vector>
#include <string>
using namespace std;

#define FR(i,a,n) for(int (i) = (a); (i)<(n); (i)++)
#define RF(i,a,n) for(int (i) = int(n)-1; (i)>=(a); (i)--)
#define FOR(i,n) FR(i,0,n)
#define ROF(i,n) RF(i,0,n)

typedef long long ll;
typedef long double ld;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;
typedef vector<int> vi;

int dr[4] = {-1,0,1,0};
int dc[4] = {0,1,0,-1};
int malted[2000];
vector<int> unmalted[2000];
int val[2000];
int main()
{
	int T;
	scanf("%d", &T);
	FOR(t,T)
	{
		int N, M;
		scanf("%d%d", &N, &M);
		FOR(i,M)
		{
			malted[i] = -1;
			unmalted[i].clear();
			int p;
			scanf("%d", &p);
			FOR(j,p)
			{
				int a, b;
				scanf("%d%d", &a, &b);
				a--;
				if(b)
					malted[i] = a;
				else
					unmalted[i].push_back(a);
			}
		}
		memset(val, 0, sizeof(val));
		bool change = true;
		while(change)
		{
			change = false;
			FOR(i,M)
			{
				if(malted[i]!=-1 && val[malted[i]] == 1)
					continue;
				bool found = false;
				FOR(j,unmalted[i].size())
					if(val[unmalted[i][j]]==0)
						found = true;
				if(found)
					continue;
				if(malted[i]==-1)
					goto IMPOSSIBLE;
				val[malted[i]] = 1;
				change = true;
			}
		}
		printf("Case #%d:", t+1);
		FOR(i,N)
			printf(" %d", val[i]);
		putchar('\n');
		continue;
		IMPOSSIBLE:
		printf("Case #%d: IMPOSSIBLE\n", t+1);
	}
	return 0;
}

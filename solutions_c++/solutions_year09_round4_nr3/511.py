#include <iostream>
#include <algorithm>
#include <cstdio>
#include <map>
#include <set>
#include <list>
#include <cmath>

using namespace std;

#define FOR(i,a,b) for(int i(a), _n(b); i<=_n; i++)
#define FR(i,b) FOR(i,0,b-1)
#define REP(i,a,b) for(int i(a), _n(b); i >= _n; i--)
#define _M(a) memset(a,0,sizeof(a))
#define IN scanf
#define OUT printf
#define sqr(q) ((q)*(q))
#define ll long long
#define ul unsigned ll
#define INF 1000000000

int KT;
int ans;
bool M[101][101];
int L[101][50];
int n,k;

int main()
{
	freopen("test.in","r",stdin);
	freopen("test.out","w",stdout);
	IN("%d", &KT);
	
	FOR(test, 1, KT)
	{
		IN("%d%d", &n, &k);
		FR(i,n) FR(j,k) IN("%d", &L[i][j]);
		FR(i,n) FR(j,n)
		{
			M[i][j] = 0;
			FR(t,k-1) if (L[i][t] == L[j][t] || L[i][t+1] == L[j][t+1] || 
							(L[i][t] > L[j][t] && L[i][t+1] < L[j][t+1]) ||
							(L[j][t] > L[i][t] && L[j][t+1] < L[i][t+1]))
						{ M[i][j] = 1; break; }
		} 
		
		int li = (1 << n) -1;
		ans = 0;
		FOR(i,1,li)
		{
			int c = 1;
			bool f = 1;
			while (c <= li && f)
			{
				if ((c & i) && f)
				{
					int x = c << 1;
					while ((x <= li) && f)
					{
						if (x & i)
						{
							int t = c;
							int p = x;
							int a(0),b(0);
							while (t) a++,t = t >> 1;
							while (p) b++,p = p >> 1;
							f = M[a-1][b-1];
						}
						x = x << 1;
					}
				}
				c = c << 1;
			}
			if (!f) continue;
			int b = 0;
			int t = i;
			while (t) b+=(t & 1), t = t >> 1;
			if (ans < b) ans = b;
		}
		
		OUT("Case #%d: %d\n", test, ans);
	}
	

	return 0;
}

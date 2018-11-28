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
int n;
int f[100];
int ans;

int main()
{
	freopen("test.in","r",stdin);
	freopen("test.out","w",stdout);
	IN("%d", &KT);
	
	FOR(test, 1, KT)
	{
		IN("%d\n", &n);
		ans = 0;
		_M(f);
		FR(i,n)
		{
			char c;
			FR(j,n) 
			{
				IN("%c", &c);
				if (c == '1') f[i] = j; 
			}
			IN("\n");
		}
		
		FR(i,n)
		{
			int c = i;
			while (f[c] > i) c++;
			ans += c-i;
			while (c != i) swap(f[c], f[c-1]), c--;
		}
		
		OUT("Case #%d: %d\n", test, ans);

	}
	

	return 0;
}

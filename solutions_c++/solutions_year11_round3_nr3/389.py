#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>

#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <queue>
#include <list>
#include <stack>
#include <map>
#include <set>
using namespace std;
 
#define DEBUG(x) //x
#define REP(i,a) for(int i=0;i<int(a);i++)
#define FOR(i,a,b) for(int i=a;i<int(b);i++)
#define VI vector<int>
#define size(x) int((x).size())
#define all(x) (x).begin(), (x).end()
#define MK(x, y) make_pair(x, y)
#define PB push_back
 
typedef pair<int, int> pii;
typedef long long ll;

int v[100000];

ll gcd(ll a, ll b)
{
	return b == 0 ? a : gcd(b, a % b);
}

ll lcm(ll a, ll b)
{
	ll g = gcd(a, b);
	ll r = a / g;
	r *= b;
	return r;
}

int solve()
{
	int n, l, h;
	scanf("%d %d %d\n", &n, &l, &h);
	
	REP(i, n)
		scanf("%d", &v[i]);
	sort(v, v + n);

	bool ok;
	int i;
	for (i = l; i <= h; i++)
	{
		ok = true;
		for (int j = 0; j < n; j++)
		{
			if (v[j] < i)
			{
				if (i % v[j] != 0)
					ok = false;
			}
			else
			{
				if (v[j] % i != 0)
					ok = false;
			}
			if (!ok)
				break;		
		}
		if (ok)
			break;
	}
	if (ok)
		printf("%d\n", i);
	else
		printf("NO\n");
}


/*********/

int main(void){
	int T,t;
	scanf("%d",&T);
	REP(t,T){
		printf("Case #%d: ",t+1);
		solve();
	}
	return 0;
}


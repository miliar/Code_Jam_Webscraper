#include <cstdio>
#include <cmath>
#include <algorithm>
#include <map>
#include <iostream>
#include <string>
#include <cstring>
#include <vector>
#include <set>
#include <map>
#include <list>
#include <queue>
#include <bitset>
#include <cstdlib>
using namespace std;

#define rep(i,a,b) for(int i=(a); i<(b); ++i)
#define trav(it, v) for(typeof((v).begin()) it = (v).begin();it!=(v).end(); ++it)

typedef long long ll;
typedef pair<int,int> pii;
typedef vector<int> vi;
typedef double fl;

int a[1000+10];
int N;
bool check[1000+10];

void solve(int tc)
{
	scanf("%d", &N);
	rep(i,0,N)
	{
		scanf("%d", a+i);
		--a[i];
	}
	rep(i,0,N)
		check[i] = false;
	ll ans = 0;
	rep(s,0,N)
	{
		if(!check[s])
		{
			int p = s;
			int l = 0;
			do
			{
				check[p] = true;
				++l;
				p = a[p];
			} while(p != s);
			ans += (l==1?0:l);
		}
	}
	cout << "Case #" << tc << ": " << ans << endl;
}

int main() 
{
	int T;
	scanf("%d", &T);
	rep(i,0,T)
		solve(i+1);
  return 0;
}

#include <vector>
#include <string>
#include <iostream>
#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <fstream>
#include <sstream>
#include <map>
#include <set>
using namespace std;

#define sz(x) int((x).size())
#define FOR(i,a,b) for(int (i) = (a); (i) <= (b); ++(i))
#define ROF(i,a,b) for(int (i) = (a); (i) >= (b); --(i))
#define rep(i,n) for (int (i) = 0; (i) < (n); ++(i))
#define fe(i,a) for (int (i) = 0; (i) < int((a).size()); ++(i))
#define C(a) memset((a),0,sizeof(a))
#define inf 1000000000
#define pb push_back
#define ppb pop_back
#define all(c) (c).begin(), (c).end()
#define pi 2*acos(0.0)
#define sqr(a) (a)*(a)
#define mp(a,b) make_pair((a), (b))
#define X first
#define Y second

typedef vector<int> vint;
typedef long long ll;
typedef pair<int, int> pii;



int main()
{
	freopen("C-large.in","r",stdin);
	freopen("output.txt","w",stdout);

	int TS;
	scanf("%d",&TS);
	rep(T,TS)
	{
		int n,mn,sum,x,t;
		sum = 0;
		mn = inf;
		x = 0;
		scanf("%d",&n);
		rep(i,n)
		{
			scanf("%d",&t);
			sum += t;
			if (mn > t) mn = t;
			x ^= t;
		}
		printf("Case #%d: ",T+1);
		if (x != 0) printf("NO\n");
		else printf("%d\n",sum-mn);
	}

	return 0;
}

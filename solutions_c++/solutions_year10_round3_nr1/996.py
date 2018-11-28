#include <iostream>
#include <cstdio>
#include <vector>
#include <cmath>
#include <algorithm>
#include <queue>
#include <cstring>
#include <list>
#include <set>

using namespace std;

#define pb push_back
#define pint pair<int, int>
#define lint long long int
#define mp make_pair
#define fi first
#define se second
#define dbg 0
#define qwe if(dbg)
#define f(I, N) for(int (I) = 0;(I) < (N);(I) ++)
#define vi vector<int>


int main(int argc, char* argv[])
{
	int t;
	scanf("%d", &t);
	
	for(int u = 1;u <= t;u ++)
	{
		int n;
		lint gres = 0;
		scanf("%d", &n);
		vector<pint> v;
		while(n --)
		{
			int a, b;
			scanf("%d%d", &a, &b);
			v.pb( mp(a, b) );
		}
		sort(v.begin(), v.end() );
		qwe f(i, v.size() ) cout << v[i].fi << "  " << v[i].se << endl;
		f(i, v.size() )
		{
			pint tmp = v[i];
			qwe cout << " tmp = " << tmp.fi << "  " << tmp.se << endl;
			int j = i + 1;
			int res = 0;
			while(j < v.size()/* && v[j].se < tmp.se*/) {qwe cout << " j = " << j << "  " << v[j].fi << " " << v[j].se << endl;
			if(v[j].se < tmp.se)res++;
			j++; }
			gres += res;
		}
		printf("Case #%d: %lld\n", u, gres);
	}
return 0;
}

#include<iostream>
#include<cstdio>
#include<vector>
#include<map>
#include<set>
#include<algorithm>
#include<cmath>
#include<sstream>
#include<deque>
#include<queue>
#include<stack>
#include<string>
#include<cstring>
#ifdef _MSC_VER
#include <hash_set>
#include <hash_map>
using namespace stdext;
#else
#if __GNUC__ > 2
#include <ext/hash_set>
#include <ext/hash_map>
using namespace __gnu_cxx;
#else
#include <hash_set>
#include <hash_map>
#endif
#endif

using namespace std;

#define eps 1e-12
#define oo (int)1e9
#define foreach(i,c) for(__typeof((c).begin()) i = (c).begin() ; i != (c).end() ; i++)

typedef unsigned long long ull;
typedef long long ll;

int main()
{
#ifndef ONLINE_JUDGE
	freopen("in.in","rt",stdin);
	freopen("out.out","w",stdout);
#endif

	int test;

	scanf("%d",&test);

	for( int tt = 1 ; tt <= test ; tt++ )
	{
		char c;
		int n,x;
		vector<pair<char,int> > v,o,b;

		scanf("%d", &n);

		for( int i = 0 ; i < n ; i++ )
		{
			scanf(" %c%d",&c,&x);
			c = tolower(c);

			v.push_back(make_pair(c,x));

			if( c == 'o' )
				o.push_back(make_pair(c,x));
			else
				b.push_back(make_pair(c,x));
		}

		int ind, oi, bi,res,oc,bc;

		res = ind = bi = oi = 0;
		oc = bc = 1;

		for( int i = 0 ; i < n ; i++ )
		{
			if( v[i].first == 'o' )
			{
				x = abs(v[i].second-oc)+1;
				oc = v[i].second;
				res += x;
				oi++;

				if( bi < b.size() )
				{
					int y = abs(bc-b[bi].second);
					bc = y < x ? b[bi].second : bc < b[bi].second ? bc+x : bc-x;
				}
			}
			else
			{
				x = abs(v[i].second-bc)+1;
				bc = v[i].second;
				res += x;
				bi++;

				if( oi < o.size() )
				{
					int y = abs(oc-o[oi].second);
					oc = y < x ? o[oi].second : oc < o[oi].second ? oc+x : oc-x;
				}
			}
		}

		printf("Case #%d: %d\n",tt,res);
	}

	return 0;
}

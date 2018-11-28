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

int xd[] = {0,0,1,1};
int yd[] = {0,1,0,1};
string s = "/\\\\/";
bool convert(vector<string>& v)
{
	for( int i = 0 ; i < v.size() ; i++ )
	{
		for( int j = 0 ; j < v[i].size() ; j++ )
		{
			if( v[i][j] != '#')
				continue;

			for( int d = 0 ; d < 4 ; d++ )
			{
				int ni = i + xd[d];
				int nj = j + yd[d];

				if( ni >= v.size() || nj >= v[i].size() || v[ni][nj] != '#' )
					return false;

				v[ni][nj] = s[d];
			}
		}
	}

	return true;
}

int main()
{
#ifndef ONLINE_JUDGE
	freopen("in.in","rt",stdin);
	freopen("out.txt","w",stdout);
#endif

	int test,r,c;

	scanf("%d", &test);

	for( int tt = 1 ; tt <= test ; tt++ )
	{
		scanf("%d%d", &r, &c);
		vector<string> v(r,string(c,' '));

		for( int i = 0 ; i < r ; i++ )
			for( int j = 0 ; j < c ; j++ )
				scanf(" %c", &v[i][j]);

		printf("Case #%d:\n", tt);

		if( convert(v) )
		{
			for( int i = 0 ; i < r ; i++ )
				printf("%s\n", v[i].c_str());
		}
		else
		{
			printf("Impossible\n");
		}
	}
	return 0;
}

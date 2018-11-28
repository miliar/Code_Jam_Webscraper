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
	freopen("out.txt","w",stdout);
#endif

	int test;
	int n,x;

	scanf("%d",&test);

	for( int tt = 1 ; tt <= test ; tt++ )
	{
		scanf("%d",&n);
		int sum = 0;

		for( int i = 0 ; i < n ; i++ )
		{
			scanf("%d",&x);
			sum += x!=i+1;
		}

		printf("Case #%d: %d\n",tt,sum);
	}
	return 0;
}

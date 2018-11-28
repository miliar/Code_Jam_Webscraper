#include<iostream>
#include<cstdio>
#include<vector>
#include<map>
#include<set>
#include<algorithm>
#include<cmath>
#include<sstream>
#include<deque>
#include<stack>
#include<string>
#include<cstring>

using namespace std;

#define eps 1e-12
#define oo (int)1e9
#define foreach(i,c) for(__typeof((c).begin()) i = (c).begin() ; i != (c).end() ; i++)

int x[1001];
int y[1001];

int main()
{
	#ifndef ONLINE_JUDGE
	freopen("in.in", "rt", stdin);
	freopen("out.out", "w", stdout);
	#endif

	int test,n;

	scanf("%d",&test);

	for( int tt = 0 ; tt < test ; tt++ )
	{
		scanf("%d",&n);

		for( int i = 0 ; i < n ; i++ )
		{
			scanf("%d%d",x+i,y+i);
		}

		int cnt = 0;

		for( int i = 0 ; i < n ; i++ )
			for( int j = i+1 ; j < n ; j++ )
				if( (x[i] <= x[j] && y[i] >= y[j]) ||
					(x[i] >= x[j] && y[i] <= y[j]) )
					cnt++;

		printf("Case #%d: %d\n",tt+1,cnt);
	}
	return 0;
}

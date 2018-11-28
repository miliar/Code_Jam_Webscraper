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

int main()
{
	#ifndef ONLINE_JUDGE
	freopen("in.in", "rt", stdin);
	freopen("out.out", "w", stdout);
	#endif
	int test,n,k,x;

	scanf("%d",&test);

	for( int tt = 0 ; tt < test ; tt++ )
	{
		scanf("%d%d",&n,&k);

		x = 1<<n;
		k = k%x;

		printf("Case #%d: %s\n",tt+1,k == x-1 ? "ON":"OFF");
	}

	return 0;
}

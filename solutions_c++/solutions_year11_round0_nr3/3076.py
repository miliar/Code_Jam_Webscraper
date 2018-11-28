#include <map>
#include <set>
#include <list>
#include <cmath>
#include <queue>
#include <stack>
#include <bitset>
#include <vector>
#include <cstdio>
#include <string>
#include <sstream>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;

int N;
int a[1005];

inline void Readin()
{
	scanf("%d",&N);
	for (int i=1;i<=N;++i)
		scanf("%d",a+i);
}

inline void Solve()
{
	int x = 0 , sum = 0, Min = 1<<30;
	for (int i=1; i<=N;++i)
	{
		x ^= a[i];
		sum += a[i];
		Min = min(Min , a[i]);
	}
	
	if (x ==0) printf("%d\n",sum - Min);
	else printf("NO\n");
}

int main()
{
	freopen( "C-large.in" , "r" , stdin ) ;
	freopen( "C-large.out" , "w" , stdout ) ;
	int Test,Case=0;
	for (scanf("%d",&Test);Test--;)
	{
		printf("Case #%d: ",++Case);
		
		Readin();
		Solve();
	}
	
	return 0;
}

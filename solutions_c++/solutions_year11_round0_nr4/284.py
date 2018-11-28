#include<vector>
#include<list>
#include<map>
#include<set>
#include<deque>
#include<queue>
#include<stack>
#include<bitset>
#include<algorithm>
#include<functional>
#include<numeric>
#include<utility>
#include<iostream>
#include<sstream>
#include<iomanip>
#include<cstdio>
#include<cmath>
#include<cstdlib>
#include<cctype>
#include<string>
#include<cstring>
#include<cstdio>
#include<cmath>
#include<cstdlib>
#include<ctime>
#include<climits>
#include<complex>
#define mp make_pair
#define pb push_back
using namespace std;
int n;
int main()
{
	freopen("C:\\Users\\daizhy\\Downloads\\D-large.in","r",stdin);
	freopen("C:\\Users\\daizhy\\Documents\\output.txt","w",stdout);
	int i,j,k,cas,cc=0;
	scanf("%d",&cas);
	while (cas--)
	{
		scanf("%d",&n);
		for (j=0,i=1;i<=n;i++)
		{
			scanf("%d",&k);
			j+=i!=k;
		}
		printf("Case #%d: %lf\n",++cc,j*1.0);
	}
	return 0; 
}
	

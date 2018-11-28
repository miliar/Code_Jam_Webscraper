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
int n,a[1000];
int main()
{
	freopen("C:\\Users\\daizhy\\Downloads\\C-large (4).in","r",stdin);
	freopen("C:\\Users\\daizhy\\Documents\\output.txt","w",stdout);
	int i,j,k,cas,cc=0;
	scanf("%d",&cas);
	while (cas--)
	{
		scanf("%d",&n);
		j=1<<29;
		int sum=0;
		for (k=i=0;i<n;i++)
		{
			scanf("%d",a+i);
			j=min(j,a[i]);
			k^=a[i];
			sum+=a[i];
		}
		if (k)printf("Case #%d: NO\n",++cc);
		else printf("Case #%d: %d\n",++cc,sum-j);
	}
	return 0;
}

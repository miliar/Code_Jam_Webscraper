#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include<fstream>
using namespace std;
int f[20000];
int a[20000][5];
int main()
{

    freopen("A-large.in","r",stdin);freopen("2.txt","w",stdout);
    int ii,i,j,n,tt,t,t1;
	bool d;
	scanf("%d",&t);
	for(ii=1;ii<=t;ii++)
	{
		scanf("%d",&n);
		for(i=1;i<=n;i++)
			scanf("%d%d",&a[i][0],&a[i][1]);
		scanf("%d",&tt);
		for(i=1;i<=n;i++)
			f[i]=0;
		f[1]=a[1][0];
		for(i=1;i<=n;i++)
		{
			for(j=i+1;j<=n;j++)
				if (a[j][0]-a[i][0]>f[i]) break;
				else
				{
					if (a[j][0]-a[i][0]>a[j][1]) t1=a[j][1];
					else
						t1=a[j][0]-a[i][0];
					if (f[j]<t1) f[j]=t1;
				}
		}
		d=false;
		for(i=1;i<=n;i++)
			if (a[i][0]+f[i]>=tt)
			{
				d=true;
				break;
			}
		if (d) printf("Case #%d: YES\n",ii);
		else
			printf("Case #%d: NO\n",ii);
	}

	return 0;

}
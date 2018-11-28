#include <cstdio>
#include <string>
#include <vector>
#include <algorithm>
#include <cmath>
#include <memory.h>
using namespace std;
int main(void)
{
	int t,q,n,i,j,k,ma,x,sum;
	freopen("r2.in","r",stdin);
	freopen("r2.out","w",stdout);
	vector<vector<int>> a(50);
	scanf("%d",&t);
	for (q=1;q<=t;q++)
	{
		scanf("%d",&n);
		for (i=0;i<n;i++)
			a[i].clear();
		for (i=0;i<n;i++)
		{
			ma=0;
			for (j=0;j<n;j++)
			{
				scanf("%1d",&x);
				if (x==1)
					ma=j;
			}
			for (j=ma;j<n;j++)
				a[j].push_back(i);
		}
		for (i=0;i<n;i++)
			sort(a[i].begin(),a[i].end());
		sum=0;
		for (i=0;i<n;i++)
		{
			sum+=a[i][0]-i;
			for (j=i+1;j<n;j++)
			{
					for (k=0;k<a[j].size();k++)
					{
						if (a[j][k]<a[i][0])
							a[j][k]++; else
						if (a[j][k]==a[i][0])
						{
							a[j].erase(a[j].begin()+k);
							break;
						} else
							break;
					}
			}
		}
		printf("Case #%d: %d\n",q,sum);
	}
	fclose(stdout);
	return 0;
}

	

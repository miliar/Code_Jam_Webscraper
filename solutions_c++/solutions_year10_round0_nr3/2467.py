#include <iostream>
#include <algorithm>
#include <string>
using namespace std;
int group[20];
int main()
{
	freopen("D://C-small-attempt0.in","r",stdin);
	freopen("D://21.out","w",stdout);
	int T;
	scanf("%d",&T);
	for(int i=0;i<T;i++)
	{
		int r,k,n;
		int p=0;
		int res=0;
		memset(group,0,sizeof(group));
		scanf("%d%d%d",&r,&k,&n);
		for(int j=0;j<n;j++)
			scanf("%d",&group[j]);
		for(int j=0;j<r;j++)
		{
			int kk=k;
			int cnt=0;
			while( kk >= group[p] && cnt < n)
			{
				kk-=group[p];
				res+=group[p];
				p++;
				p=p%n;
				cnt++;
			}
		}
		printf("Case #%d: %d \n",i+1,res);
	}
	return 0;
}
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <queue>
#include <cmath>

using namespace std;


int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	int T;
	scanf("%d",&T);
	for(int t=1;t<=T;t++)
	{
		printf("Case #%d: ",t);
		int n,k,i,j,l;
		scanf("%d%d",&n,&k);
		int y[100][25];
		for(i=0;i<n;i++)
			for(j=0;j<k;j++) scanf("%d",&y[i][j]);
		int mask[100]={0};
		for(i=0;i<n;i++) mask[i]=1<<i;
		for(i=0;i<n;i++)
			for(j=i+1;j<n;j++)
			{
				int a=0,b=0,c=0;
				for(l=0;l<k;l++)
				{
					if (y[i][l]<y[j][l]) ++a;
					if (y[i][l]==y[j][l]) ++b;
					if (y[i][l]>y[j][l]) ++c;
				}
				if (b>0 || a>0 && c>0)
				{
					mask[i]|=1<<j;
					mask[j]|=1<<i;
				}
			}
		int ans=0;
		for(i=1;i<(1<<n);i++)
		{
			int m,k;
			k=0;
			m=(1<<n)-1;
			for(j=0;j<n;j++) 
				if (i&(1<<j)) 
				{
					m&=mask[j];
					k++;
				}
			if ((m&i)==i) ans=max(ans,k);
		}
		printf("%d\n",ans);
	}

	return 0;
}
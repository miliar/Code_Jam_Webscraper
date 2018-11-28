#include<iostream>
#include<algorithm>
#include<cstring>
#include<stdio.h> 
#include<memory.h>
#include<math.h>
using namespace std;
#define maxnum 0x7fffffff
int g[1001],a[1001],b[1001];
int r,k,n;
int main()
{
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	int cas,tt,i,j;
	long long take;
	scanf("%d",&cas);
	for(tt=1;tt<=cas;tt++)
	{
		scanf("%d %d %d",&r,&k,&n);
		for(i=0;i<n;i++)
		    scanf("%d",g+i);
		for(i=0;i<n;i++)
		{
			take=0;
			int cnt=0;
			j=i;
			while(take+g[j]<=k && cnt<n)
			{
				take+=g[j];
				j=(j+1)%n;
				cnt++;
			} 
			a[i]=j;//從i開始能到達的位置
			b[i]=take; //從i開始能裝的人數 
			
		}    
		//for(i=0;i<n;i++) printf("%d ",a[i]); puts("");
		//for(i=0;i<n;i++) printf("%d ",b[i]); puts("");
		long long sum=0;
		i=0;
		while(r--)
		{
			sum+=b[i];
			i=a[i];
		}
		printf("Case #%d: ",tt);
		cout<<sum<<endl;
	}
	return 0;
}

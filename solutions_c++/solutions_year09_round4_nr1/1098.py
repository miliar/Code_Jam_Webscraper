#include<stdio.h>
#include<iostream>
#include<algorithm>
#include<memory.h>
using namespace std;
char a[50][50];
int num[50];
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-out.txt","w",stdout);
	int cas,i,j,n,t;
	scanf("%d",&t);
	for(cas=1;cas<=t;cas++)
	{
		memset(a,NULL,sizeof(a));
		memset(num,-1,sizeof(num));
		scanf("%d",&n);
		for(i=0;i<n;i++)
		   scanf("%s",&a[i]);
   		for(i=0;i<n;i++)
		{
		   int ok=0;
		   for(j=n-1;j>=0 && ok==0;j--)
		   {
		   	   if(a[i][j]=='1')
		   	   {
		   	   	   num[i]=j;
		   	   	   ok=1;
			   }
		   }
		}
		//for(i=0;i<n;i++) printf("%d  ",num[i]);printf("\n");
		int cnt=0;
		for(i=0;i<n;i++)
		{
          if(num[i]>i)
		  {
			int ok=0;
			for(j=i;j<n && ok==0;j++)
			{
				if(num[j]<=i)
				{
					int k;
					for(k=j-1;k>=i;k--)
					{
						int tmp=num[k+1];
						num[k+1]=num[k];
						num[k]=tmp;
						cnt++;
						//for(int l=0;l<n;l++)
						//   printf("%d  ",num[l]);
			            //printf("\n");
					}
					ok=1;
				}
			}
		  }
		}
		printf("Case #%d: %d\n",cas,cnt);
	}
	return 0;
}

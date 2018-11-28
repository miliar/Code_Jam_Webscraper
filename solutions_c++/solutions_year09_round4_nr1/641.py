#include<iostream>
using namespace std;
int main()
{
	int p,i,j,k,cnt,t;
	scanf("%d",&p);
	for(t=1;t<=p;t++)
	{
		int n;
		scanf("%d",&n);
		char *arr[n];
		
		for(i=0;i<n;i++)
		{
			arr[i]=new char[n];
			scanf("\n");
			for(j=0;j<n;j++)
				scanf("%c",&arr[i][j]);
		}
		int *a=new int[n];
		for(i=0;i<n;i++)
		{
			for(j=n-1;j>=0;j--)
			{
				if(arr[i][j]=='1')
					break;
			}
			a[i]=j;
		}
		cnt=0;
		for(i=0;i<n;i++)
		{
			for(j=i;j<n;j++)
			{
				if(a[j]<=i)
					break;
			}
			for(k=j;k>i;k--)
			{
				a[k]=a[k-1];
				cnt++;
			}
		}
		printf("Case #%d: %d\n",t,cnt);
	}
}
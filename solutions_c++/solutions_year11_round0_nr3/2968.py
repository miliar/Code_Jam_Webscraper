#include<iostream>
#include<stdio.h>
#define N 1010
using namespace std;
int a[N],sel[N],unsel[N];
void check(int s,int us,int *ans)
{
	int val1=0,val2=0;
	for(int i=0;i<s;i++) val1+=sel[i];
	for(int i=0;i<us;i++) val2+=unsel[i];
	for(int i=1;i<s;i++)
		sel[0]=sel[0]^sel[i];
	for(int i=1;i<us;i++)
		unsel[0]=unsel[0]^unsel[i];
	if(sel[0]==unsel[0]) 
	{
		val1=(val1>val2)?val1:val2;
		if(*ans<val1)
			*ans=val1;
	}
	return;
}
int main()
{
	int total,n,tc,ans,s,us;
	scanf("%d",&tc);
	for(int t=0;t<tc;t++)
	{
		scanf("%d",&n);
		for(int i=0;i<n;i++) scanf("%d",&a[i]);
		ans=-1;
		total=1<<n;
		for(int i=1;i<total-1;i++)
		{
			s=us=0;
			for(int j=0;j<n;j++)
			{
				if((i>>j) & 1) 
					sel[s++]=a[j];
				else 
					unsel[us++]=a[j];
			}
			check(s,us,&ans);
		}
		if(ans==-1)
			printf("Case #%d: NO\n",(t+1));
		else		
			printf("Case #%d: %d\n",(t+1),ans);
	}
	return 0;
}

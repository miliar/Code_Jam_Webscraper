#include<iostream>
#include<stdio.h>
using namespace std;

int main()
{
	freopen("in.in","r",stdin);
	freopen("out.txt","w",stdout);
	int t;
	scanf("%d",&t);
	for(int cas=1;cas<=t;cas++)
	{
		int n,s,p;
		int score[102];
		scanf("%d%d%d",&n,&s,&p);
		int a1=0,a2=0;
		for(int i=0;i<n;i++)
		{
			scanf("%d",&score[i]);
			if(score[i]>=3*p-2)
			{
				a1++;
			}
			else if(score[i]>=3*p-4&&score[i]>=2)
			{
				a2++;
			}
		}
		int ans=a1+(a2>s?s:a2);
		printf("Case #%d: %d\n",cas,ans);
	}	
	return 0;
}

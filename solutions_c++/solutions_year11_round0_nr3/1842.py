#include <iostream>
#include <stdlib.h>
#include <stdio.h>
#include <cstdio>
#include <string>

using namespace std;

int t,n,c;

int main()
{
	freopen("C-large.in","r",stdin);
	freopen("ansc.txt","w",stdout);
	scanf("%d",&t);
	for(int ii=1;ii<=t;ii++)
	{
		int s,ans=0,sum=0,minNum=1000001;
		scanf("%d",&n);
		for(int i=0;i<n;i++)
		{
			scanf("%d",&s);
			sum+=s;
			ans^=s;
			if(minNum>s) minNum=s;
		}
		if(ans!=0)
			printf("Case #%d: NO\n",ii);
		else printf("Case #%d: %d\n",ii,sum-minNum);
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}
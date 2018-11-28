/*
author:cydorniaknight@gmail.com
blog:http://hi.baidu.com/cydorniaknight
*/

#include<iostream>
using namespace std;

int t,n,c[2000];

int main()
{
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	int ti,i,xor,sum,mini;
	scanf("%d",&t);
	for(ti=1;ti<=t;++ti)
	{
		scanf("%d",&n);
		mini=10000000;
		sum=xor=0;
		for(i=0;i<n;++i)
		{
			scanf("%d",&c[i]);
			if(c[i]<mini)mini=c[i];
			sum+=c[i];
			xor=xor^c[i];
		}
		printf("Case #%d: ",ti);
		if(xor) printf("NO\n");
		else printf("%d\n",sum-mini);
	}
	//system("pause");
	return 0;
}
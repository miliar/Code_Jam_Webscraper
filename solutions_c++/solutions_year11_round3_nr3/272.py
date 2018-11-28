#include<cstdio>
#include<iostream>
#include<algorithm>
#include<cstring>
using namespace std;

int main()
{
	int T;
	cin>>T;
	for(int tc=1;tc<=T;tc++)
	{
		int n,l,h,i,j;
		int fq[10009]={0};
		scanf("%d%d%d",&n,&l,&h);
		for(i=0;i<n;i++)
			scanf("%d",&fq[i]);
		bool pos;
		for(i=l;i<=h;i++)
		{
			pos=true;
			for(j=0;j<n;j++)
			{
				if(fq[j]%i !=0 && i%fq[j]!=0)
				{
					pos=false;
					break;
				}
			}
			if(pos)break;
		}
		printf("Case #%d: ",tc);
		if(pos)
		{
			printf("%d\n",i);
		}
		else
			puts("NO");
	}
	return 0;
}

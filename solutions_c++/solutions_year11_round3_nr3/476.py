#include<stdio.h>
#include<stdlib.h>
#include<iostream>
#include<algorithm>
#include<vector>

using namespace std;


int main(int argc,char* argv[])
{
	freopen("C-small.in","r",stdin);
	freopen("C-small.out","w",stdout);
	//freopen("B-large.in","r",stdin);
	//freopen("B-large.out","w",stdout);
	
	int T;
	int n,l,h;
	int cas=1;
	scanf("%d",&T);
	int num[110];
	while(T--)
	{
		scanf("%d%d%d",&n,&l,&h);
		for(int i=0;i<n;i++)
			scanf("%d",&num[i]);
		
		bool tag=false;
		int p;
		for(int i=l;i<=h;i++)
		{
			bool flag=true;
			for(int j=0;j<n;j++)
			{
				if(num[j]%i==0||i%num[j]==0)
					flag=true;
				else
				{
					flag=false;
					break;
				}
			}
			if(flag)
			{
				tag=flag;
				p=i;
				break;
			}
		}
		printf("Case #%d: ",cas++);
		if(tag)
			printf("%d\n",p);
		else
			printf("NO\n");


	}

	return 0;
}

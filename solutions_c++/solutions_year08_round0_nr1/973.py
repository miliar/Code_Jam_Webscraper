#include <stdio.h>
#include <string.h>
#include <string>
#include <algorithm>
#include <iostream>

using namespace std;

char * engine[101];
char t[101];
int flag[101];
int n,s,q,ans,num;

bool cmp(char * s,char * t)
{
	return strcmp(s,t)<0;
}

int locate(char * t)
{
	int left=0,
		right=s-1,
		middle=(left+right)/2;
	while(left<=right)
	{
		if(strcmp(engine[middle],t)==0)
			return middle;
		if(strcmp(engine[middle],t)>0)
			right=middle-1;
		else
			left=middle+1;
		middle=(left+right)/2;
	}
	return -1;
}

int main()
{
//	freopen("small.txt","w",stdout);
	freopen("large.txt","w",stdout);
	int i,j,k;
	for(i=0;i<101;i++)
		engine[i]=(char *)malloc(sizeof(char)*101);
	scanf("%d",&n);
	for(int N=1;N<=n;N++)
	{
		ans=0;
		scanf("%d ",&s);
		for(i=0;i<s;i++)
		{
			gets(engine[i]);
			flag[i]=0;
		}
		num=s;
		sort(engine,engine+s,cmp);
		scanf("%d ",&q);
		for(i=0;i<q;i++)
		{
			gets(t);
			for(j=0;j<s;j++)
			{
				int pos=locate(t);
				if(pos==-1) continue;
				if(!flag[pos])
				{
					flag[pos]=1;
					if(num>1)
						num--;
					else
					{
						ans++;
						for(k=0;k<s;k++)
							if(k!=pos)
								flag[k]=0;
						num=s-1;
					}
				}
			}
		}
		printf("Case #%d: %d\n",N,ans);
	}
	return 0;
}

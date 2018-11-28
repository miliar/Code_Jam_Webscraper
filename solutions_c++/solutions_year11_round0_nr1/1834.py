#include <iostream>
#include <stdlib.h>
#include <stdio.h>
#include <cstdio>

using namespace std;

int p,t,n;

typedef struct
{
	int y;
	char x;
}NODE;

NODE node[101];

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("e.txt","w",stdout);
	scanf("%d",&p);
	for(int ii=1;ii<=p;ii++)
	{
		int time=0,s=0,now=0,p[27];
		p['B'-'A']=1,p['O'-'A']=1;
		scanf("%d",&n);
		for(int i=0;i<n;i++)
			scanf(" %c %d",&node[i].x,&node[i].y);
		time=node[0].y;s=node[0].y;now=0;p[node[0].x-'A']=node[0].y;
		for(int i=1;i<n;i++)
		{
			if(node[i].x==node[i-1].x)
			{
				time+=abs(node[i].y-p[node[i].x-'A'])+1;
				s+=abs(node[i].y-p[node[i].x-'A'])+1;
				p[node[i].x-'A']=node[i].y;
			}
			else
			{
				if(s>=abs(node[i].y-p[node[i].x-'A'])+1)
					time+=1,s=1;
				else
					{
						time+=abs(node[i].y-p[node[i].x-'A'])-s+1;
						s=abs(node[i].y-p[node[i].x-'A'])-s+1;
					}
				p[node[i].x-'A']=node[i].y;
			}
		}
		printf("Case #%d: %d\n",ii,time);
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}
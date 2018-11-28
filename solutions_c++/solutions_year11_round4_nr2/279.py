#include<stdio.h>
#include<string>
#include <string.h>
#include<math.h>
#include<utility>
#include<algorithm>
#include<vector>
#include<ctype.h>
#include<map>
#include <iostream>
using namespace std;

#define MAXN 510

int G[MAXN][MAXN];
int R,C,D;

bool isLegal(int x,int y,int K)
{
	return !((x==0&&y==0)||(x==0&&y==K-1)||(x==K-1&&y==0)||(x==K-1&&y==K-1));
}

bool JudgeOdd(int ox,int oy,int K)
{
	if(ox+K-1>=R||oy+K-1>=C)return false;
	int HK=K/2;

	int xMass=0,yMass=0;

	for(int i=0;i<K;i++)
	{
		for(int j=0;j<K;j++)
		{
			if(!isLegal(i,j,K))continue;
			xMass+=(i-HK)*G[i+ox][j+oy];
			yMass+=(j-HK)*G[i+ox][j+oy];
		}
	}
	return xMass==0&&yMass==0;
}

bool JudgeEven(int ox,int oy,int K)
{
	if(ox+K-1>=R||oy+K-1>=C)return false;
	int HK=K/2;
	int xMass=0,yMass=0;

	for(int i=0;i<K;i++)
	{
		for(int j=0;j<K;j++)
		{
			if(!isLegal(i,j,K))continue;
			if(i<HK)
				xMass+=(i-HK)*G[i+ox][j+oy];
			else
				xMass+=(i-HK+1)*G[i+ox][j+oy];

			if(j<HK)
				yMass+=(j-HK)*G[i+ox][j+oy];
			else
				yMass+=(j-HK+1)*G[i+ox][j+oy];
		}
	}
	return xMass==0&&yMass==0;
}

int main()
{
	freopen("in.txt","r",stdin);
	int T,ct=1;
	scanf("%d",&T);
	while(T--)
	{
		scanf("%d %d %d\n",&R,&C,&D);
		for(int i=0;i<R;i++)
		{
			char tmp;
			for(int j=0;j<C;j++)
			{
				scanf("%c",&tmp);
				G[i][j]=tmp+D-'0';
			}
			scanf("%c",&tmp);
		}

		int K=min(R,C);
		bool solved=false;
		while(K>=3)
		{
			for(int i=0;i<R;i++)
			{
				for(int j=0;j<C;j++)
				{
					if(K%2==1)
					{
						solved|=JudgeOdd(i,j,K);
					}
					else
					{
						solved|=JudgeEven(i,j,K);
					}
				}
			}
			if(solved)break;
			K--;
		}
		printf("Case #%d: ",ct++);
		if(solved)
		{
			printf("%d\n",K);
		}
		else
		{
			printf("IMPOSSIBLE\n");
		}
	}
		

	return 0;
}

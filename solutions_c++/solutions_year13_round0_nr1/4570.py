//Abhishek Paliwal
#include<iostream>
#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<malloc.h>
#include<string.h>
#include<algorithm>
#include<vector>
#include<queue>
#include<utility>
#include<climits>
#include<map>

#define FOR(i,s,n) for(i=s;i<n;i++)
#define FORD(i,s,n) for(i=s;i>n;i--)
#define LL long long

using namespace std;

int main()
{
	int t;
	scanf("%d",&t);
	int p=0;
	while(t--)
	{
		p++;
		printf("Case #%d: ",p);
		char a[5][5];
		int i,j;
		for(i=0;i<4;i++)
			scanf("%s",a[i]);
		int flag=0;
		int colx[5]={0},colo[5]={0},colt[5]={0};
		int rowt[5]={0},rowx[5]={0},rowo[5]={0};
		int dgnlx[2]={0};
		int dgnlo[2]={0};
		int dgnlt[2]={0};
		int dot=0;
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
				if(a[i][j]=='X')
				{
					rowx[i]++;
					colx[j]++;
					if(i==j)
						dgnlx[0]++;
					if(i==3-j)
						dgnlx[1]++;
				}
				if(a[i][j]=='O')
				{
					rowo[i]++;
					colo[j]++;
					if(i==j)
						dgnlo[0]++;
					if(i==3-j)
						dgnlo[1]++;

				}
				if(a[i][j]=='T')
				{
					rowt[i]++;
					colt[j]++;
					if(i==j)
						dgnlt[0]++;
					if(i==3-j)
						dgnlt[1]++;

				}
				if(a[i][j]=='.')
					dot=1;
			}
		}
		for(i=0;i<4;i++)
		{
			if(rowx[i]==4 || colx[i]==4)
				flag=1;
			if(rowo[i]==4 || colo[i]==4)
				flag=2;
			if(rowt[i]==1)
			{
				if(rowx[i]==3)
					flag=1;
				if(rowo[i]==3)
					flag=2;
			}
			if(colt[i]==1)
			{
				if(colx[i]==3)
					flag=1;
				if(colo[i]==3)
					flag=2;
			}
		}
		if(dgnlx[0]==4 ||(dgnlx[0]==3 && dgnlt[0]==1))
			flag=1;
		if(dgnlo[0]==4 ||(dgnlo[0]==3 && dgnlt[0]==1))
			flag=2;
		if(dgnlx[1]==4 ||(dgnlx[1]==3 && dgnlt[1]==1))
			flag=1;
		if(dgnlo[1]==4 ||(dgnlo[1]==3 && dgnlt[1]==1))
			flag=2;

		if(flag==1)
			printf("X won\n");
		else if(flag==2)
			printf("O won\n");
		else if(dot==1)
			printf("Game has not completed\n");
		else
			puts("Draw");

	}
	return 0;
}

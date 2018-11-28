#include <stdio.h>
using namespace std;

int main()
{
	int t;
	int a[4][4];
	scanf("%d",&t);
	for (int i1 = 1; i1 <= t; ++i1)
	{
		char ch;
		bool flag=false;
		for (int i = 0; i < 4; ++i)
		{
			scanf("\n%c",&ch);
			if(ch=='X') a[i][0]=1;
			else if(ch=='T') a[i][0]=50;
			else if(ch=='O')a[i][0]=100;
			else {a[i][0]=0; flag=true;}
			for (int j = 1; j < 4; ++j)
			{
				scanf("\n%c",&ch);
				if(ch=='X') a[i][j]=1;
				else if(ch=='T') a[i][j]=50;
				else if(ch=='O')a[i][j]=100;
				else {a[i][j]=0; flag=true;}
			}
		}
		int i=0;
		for (i = 0; i < 4; ++i)
		{
			int sum=a[i][0];
			for (int j = 1; j < 4; ++j)
				sum+=a[i][j];
			if(sum==4 || sum==53 ||sum==350 || sum==400)
				break;
		}
		if(i!=4)
		{
			printf("Case #%d: ",i1);
			if(a[i][0]==1 || a[i][1]==1)
				printf("X won\n");
			else if(a[i][0]==100 || a[i][1]==100)
				printf("O won\n");
			continue;
		}
		for (i = 0; i < 4; ++i)
		{
			int sum=a[0][i];
			for (int j = 1; j < 4; ++j)
				sum+=a[j][i];
			if(sum==4 || sum==53 ||sum==350 || sum==400)
				break;
		}
		if(i!=4)
		{
			printf("Case #%d: ",i1);
			if(a[0][i]==1 || a[1][i]==1)
				printf("X won\n");
			else if(a[0][i]==100 || a[1][i]==100)
				printf("O won\n");
			continue;
		}
		int sum=0;
		for (i = 0; i < 4; ++i)
			sum+=a[i][i];
		if(sum==4 || sum==53 ||sum==350 || sum==400)
		{
			printf("Case #%d: ",i1);
			if(a[0][0]==1 || a[1][1]==1)
				printf("X won\n");
			else if(a[0][0]==100 || a[1][1]==100)
				printf("O won\n");
			continue;
		}
		sum=0;
		for (i = 0; i < 4; ++i)
			sum+=a[i][3-i];
		if(sum==4 || sum==53 ||sum==350 || sum==400)
		{
			printf("Case #%d: ",i1);
			if(a[0][3]==1 || a[1][2]==1)
				printf("X won\n");
			else if(a[0][3]==100 || a[1][2]==100)
				printf("O won\n");
			continue;
		}
		if(flag) printf("Case #%d: Game has not completed\n",i1);
		else printf("Case #%d: Draw\n",i1);
			
	}
}
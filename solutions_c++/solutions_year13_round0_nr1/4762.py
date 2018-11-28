#include<iostream>
#include<stdio.h>
using namespace std;
int main()
{
	int t,u;
	scanf("%d ",&t);
	int a[4][4];
	char c;
	for(u=0;u<t;u++)
	{
		char s[100];
		for(int i=0;i<4;i++)
		{
			gets(s);
			for(int j=0;j<4;j++)
			{
				a[i][j]=s[j]-'A';
			}
		}
		int winA=0,winB=0;
		int countA=0;
		int countB=0;
		int countT=0;
		int countNo=0;
		for(int i=0;i<4 && winA==0 && winB==0 ;i++)
		{
			for(int j=0;j<4;j++)
			{
				if(a[i][j]==23)
					countA++;
				if(a[i][j]==19)
					countT++;
				if(a[i][j]==14)
					countB++;
				if(a[i][j]==-19)
					countNo++;

			}
			if(countA==4)
					winA=1;
			if(countB==4)
					winB=1;

			if(countT==1 && countA==3)
			{
					winA=1;
			}
			else if(countT==1 && countB==3)
			{
					winB=1;
			}

		countA=0;
		countB=0;
		countT=0;
		}
		for(int j=0;j<4 && winA==0 && winB==0 ;j++)
		{
			for(int i=0;i<4;i++)
			{
				if(a[i][j]==23)
					countA++;
				if(a[i][j]==19)
					countT++;
				if(a[i][j]==14)
					countB++;
				if(a[i][j]==-19)
					countNo++;

			}
			if(countA==4)
					winA=1;
			if(countB==4)
					winB=1;
			if(countT==1 && countA==3)
			{
					winA=1;
			}
			else if(countT==1 && countB==3)
			{
					winB=1;
			}

		countA=0;
		countB=0;
		countT=0;
		}
		for(int i=0;i<4 && winA==0 && winB==0 ;i++)
		{
			if(a[i][i]==23)
					countA++;
				if(a[i][i]==19)
					countT++;
				if(a[i][i]==14)
					countB++;
				if(a[i][i]==-19)
					countNo++;
			if(countA==4)
					winA=1;
			if(countB==4)
					winB=1;

			if(countT==1 && countA==3)
			{
					winA=1;
			}
			else if(countT==1 && countB==3)
			{
					winB=1;
			}

		}
		countA=0;
		countB=0;
		countT=0;
		for(int i=0;i<4 && winA==0 && winB==0 ;i++)
		{
			if(a[i][3-i]==23)
					countA++;
				if(a[i][3-i]==19)
					countT++;
				if(a[i][3-i]==14)
					countB++;
				if(a[i][3-i]==-19)
					countNo++;

			if(countA==4)
					winA=1;
			if(countB==4)
					winB=1;
			if(countT==1 && countA==3)
			{
					winA=1;
			}
			else if(countT==1 && countB==3)
			{
					winB=1;
			}

		}
		if(winA==1)
			printf("Case #%d: X won\n",u+1);
		else if(winB==1)
			printf("Case #%d: O won\n",u+1);
		else if(countNo>0)
			printf("Case #%d: Game has not completed\n",u+1);
		else

			printf("Case #%d: Draw\n",u+1);
		getchar();
	}
	return 0;
}

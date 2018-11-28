#include<iostream>
#include<stdio.h>
using namespace std;

int main()
{
	int test,i,j,times;
	bool np,drawImpossible,noResult;
	scanf("%d",&times);
	
	string s[4];
	int a[4];//a[0] for O a[1] for X a[2] for T a[3] for .
	for(test=1;test<=times;test++)
	{
		getchar();
		for(i=0;i<4;i++)
			getline(cin,s[i]);

			drawImpossible=false;
			noResult=true;
		for(i=0;i<4;i++)
		{
				a[0]=a[1]=a[2]=0;
				np=false;
			for(j=0;j<4;j++)
			{
				if(s[i][j]=='O')
					a[0]++;
				else if(s[i][j]=='X')
					a[1]++;
				else if(s[i][j]=='T')
					a[2]++;
				else
					np=true;
			}
			if(np)
			{
				drawImpossible=true;
				continue;
			}
			if(a[0]==4 || (a[0]==3 && a[2]==1))
			{
				printf("Case #%d: O won\n",test);
				noResult=false;
				break;
			}
			else if(a[1]==4 || (a[1]==3 && a[2]==1))
			{
				printf("Case #%d: X won\n",test);
				noResult=false;
				break;
			}
		
		}
		if(!noResult)
			continue;
		
		noResult=true;
		for(j=0;j<4;j++)
		{
				a[0]=a[1]=a[2]=0;
				np=false;
			for(i=0;i<4;i++)
			{
				if(s[i][j]=='O')
					a[0]++;
				else if(s[i][j]=='X')
					a[1]++;
				else if(s[i][j]=='T')
					a[2]++;
				else
					np=true;
			}
			if(np)
				continue;
			if(a[0]==4 || (a[0]==3 && a[2]==1))
			{
				printf("Case #%d: O won\n",test);
				noResult=false;
				break;
			}
			else if(a[1]==4 || (a[1]==3 && a[2]==1))
			{
				printf("Case #%d: X won\n",test);
				noResult=false;
				break;
			}

		}
		if(!noResult)
			continue;
			
		np=false;
		a[0]=a[1]=a[2]=0;
		for(i=0;i<4;i++)
		{
			if(s[i][i]=='O')
				a[0]++;
			else if(s[i][i]=='X')
				a[1]++;
			else if(s[i][i]=='T')
				a[2]++;
			else
				np=true;
		}
		if(!np)
		{
			if(a[0]==4 || (a[0]==3 && a[2]==1))
			{
				printf("Case #%d: O won\n",test);
				continue;
			}
			else if(a[1]==4 || (a[1]==3 && a[2]==1))
			{
				printf("Case #%d: X won\n",test);
				continue;
			}
		}
		
		
		np=false;
		a[0]=a[1]=a[2]=0;
		for(i=0;i<4;i++)
		{
			if(s[i][3-i]=='O')
				a[0]++;
			else if(s[i][3-i]=='X')
				a[1]++;
			else if(s[i][3-i]=='T')
				a[2]++;
			else
				np=true;
		}
		if(!np)
		{
			if(a[0]==4 || (a[0]==3 && a[2]==1))
			{
				printf("Case #%d: O won\n",test);
				continue;
			}
			else if(a[1]==4 || (a[1]==3 && a[2]==1))
			{
				printf("Case #%d: X won\n",test);
				continue;
			}
		}
		
		if(drawImpossible)
		printf("Case #%d: Game has not completed\n",test);
		else
  		printf("Case #%d: Draw\n",test);
	}
	return 0;
}


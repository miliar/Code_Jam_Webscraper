#include<iostream>
#include<stdio.h>
#include<string.h>
#include<cstdlib>

using namespace std;
int main()
{
	int t=0;
	scanf("%d",&t);
	int n=0;
	char arrey[4][4];
	for(n=0;n<t;)
	{
		n++;
		int k=0;
		for(;k<4;k++)
		{
			scanf("%s",arrey[k]);
		}
		int flag=0;
		int no_of_dot=0;
		for(k=0;k<4;k++)
		{
			if(arrey[k][0]!='.')
			{
				if((arrey[k][0]=='X'||arrey[k][0]=='T') && (arrey[k][1]=='X'||arrey[k][1]=='T') && (arrey[k][2]=='X'||arrey[k][2]=='T') && (arrey[k][3]=='X'||arrey[k][3]=='T'))
				{
					printf("Case #%d: X won\n",n);
					flag=1;
					break;
					perror("break");
				}

				if((arrey[k][0]=='O'||arrey[k][0]=='T') && (arrey[k][1]=='O'||arrey[k][1]=='T') && (arrey[k][2]=='O'||arrey[k][2]=='T') && (arrey[k][3]=='O'||arrey[k][3]=='T'))
				{
					printf("Case #%d: O won\n",n);
					flag=1;
					break;
				}
			}
			if(arrey[0][k]!='.')
			{
				if((arrey[0][k]=='X'||arrey[0][k]=='T') && (arrey[1][k]=='X'||arrey[1][k]=='T') && (arrey[2][k]=='X'||arrey[2][k]=='T') && (arrey[3][k]=='X'||arrey[3][k]=='T'))
				{
					printf("Case #%d: X won\n",n);
					flag=1;
					break;
				}

				if((arrey[0][k]=='O'||arrey[0][k]=='T') && (arrey[1][k]=='O'||arrey[1][k]=='T') && (arrey[2][k]=='O'||arrey[2][k]=='T') && (arrey[3][k]=='O'||arrey[3][k]=='T'))
				{
					printf("Case #%d: O won\n",n);
					flag=1;
					break;
				}
			}
			if(flag==0)
				{
					int fltu=0;
					for(;fltu<4;fltu++)
						if(arrey[k][fltu]=='.')
							no_of_dot++;
				}
			if(flag==1)
				{k=4;}
		}
		if(flag==0)
		{
			if(arrey[0][0]!='.')
			{
				if((arrey[0][0]=='X'||arrey[0][0]=='T') && (arrey[1][1]=='X'||arrey[1][1]=='T') && (arrey[2][2]=='X'||arrey[2][2]=='T') && (arrey[3][3]=='X'||arrey[3][3]=='T'))
				{
					printf("Case #%d: X won\n",n);
					flag=1;
				}

				else if((arrey[0][0]=='O'||arrey[0][0]=='T') && (arrey[1][1]=='O'||arrey[1][1]=='T') && (arrey[2][2]=='O'||arrey[2][2]=='T') && (arrey[3][3]=='O'||arrey[3][3]=='T'))
				{
					printf("Case #%d: O won\n",n);
					flag=1;
				}
			}

			if(flag==0 && arrey[0][3]!='.')
			{
				if((arrey[0][3]=='X'||arrey[0][3]=='T') && (arrey[1][2]=='X'||arrey[1][2]=='T') && (arrey[2][1]=='X'||arrey[2][1]=='T') && (arrey[3][0]=='X'||arrey[3][0]=='T'))
				{
					printf("Case #%d: X won\n",n);
					flag=1;
				}

				else if((arrey[0][3]=='O'||arrey[0][3]=='T') && (arrey[1][2]=='O'||arrey[1][2]=='T') && (arrey[2][1]=='O'||arrey[2][1]=='T') && (arrey[3][0]=='O'||arrey[3][0]=='T'))
				{
					printf("Case #%d: O won\n",n);
					flag=1;
				}
			}
		}

		if(flag==0)
		{
			if(no_of_dot==0)
				printf("Case #%d: Draw\n",n);
			else if(no_of_dot>0)
				printf("Case #%d: Game has not completed\n",n);
		}
	}
	return 0;
}
#include<iostream>
#include<stdio.h>
#include<string.h>

using namespace std;
int main()
{
	int t=0;
	scanf("%d",&t);
	int n=0;


	while(n<t)
	{
		char arr[4][4];
		n++;
		int k=0;
		for(;k<4;k++)
		{
			scanf("%s",arr[k]);
		}
		int flag=0;
		int dots=0;
		//for each row and column
		for(k=0;k<4;k++)
		{
				if((arr[k][0]=='X'||arr[k][0]=='T') && (arr[k][1]=='X'||arr[k][1]=='T') && (arr[k][2]=='X'||arr[k][2]=='T') && (arr[k][3]=='X'||arr[k][3]=='T'))
				{
					printf("Case #%d: X won\n",n);
					flag=1;
					//break;
				}

				if(flag==0 && (arr[k][0]=='O'||arr[k][0]=='T') && (arr[k][1]=='O'||arr[k][1]=='T') && (arr[k][2]=='O'||arr[k][2]=='T') && (arr[k][3]=='O'||arr[k][3]=='T'))
				{
					printf("Case #%d: O won\n",n);
					flag=1;
					//break;
				}
				if(flag==0 && ((arr[0][k]=='X'||arr[0][k]=='T') && (arr[1][k]=='X'||arr[1][k]=='T') && (arr[2][k]=='X'||arr[2][k]=='T') && (arr[3][k]=='X'||arr[3][k]=='T')))
				{
					printf("Case #%d: X won\n",n);
					flag=1;
					//break;
				}

				if(flag==0 && (arr[0][k]=='O'||arr[0][k]=='T') && (arr[1][k]=='O'||arr[1][k]=='T') && (arr[2][k]=='O'||arr[2][k]=='T') && (arr[3][k]=='O'||arr[3][k]=='T'))
				{
					printf("Case #%d: O won\n",n);
					flag=1;
					//break;
				}
			for(int i=0;i<4;i++){
				if(arr[k][i]=='.')
					dots++;
			}
			if(flag==1)
			{
				break;
			}
		}

		//check for 1st diagnols
		if(flag==0 && arr[0][0]!='.')
		{
			if((arr[0][0]=='X'||arr[0][0]=='T') && (arr[1][1]=='X'||arr[1][1]=='T') && (arr[2][2]=='X'||arr[2][2]=='T') && (arr[3][3]=='X'||arr[3][3]=='T'))
			{
				printf("Case #%d: X won\n",n);
				flag=1;
			}

			else if((arr[0][0]=='O'||arr[0][0]=='T') && (arr[1][1]=='O'||arr[1][1]=='T') && (arr[2][2]=='O'||arr[2][2]=='T') && (arr[3][3]=='O'||arr[3][3]=='T'))
			{
				printf("Case #%d: O won\n",n);
				flag=1;
			}
		}
		//check for 2nd diagnols
		if(flag==0 && arr[0][3]!='.')
		{
			if((arr[0][3]=='X'||arr[0][3]=='T') && (arr[1][2]=='X'||arr[1][2]=='T') && (arr[2][1]=='X'||arr[2][1]=='T') && (arr[3][0]=='X'||arr[3][0]=='T'))
			{
				printf("Case #%d: X won\n",n);
				flag=1;
			}

			else if((arr[0][3]=='O'||arr[0][3]=='T') && (arr[1][2]=='O'||arr[1][2]=='T') && (arr[2][1]=='O'||arr[2][1]=='T') && (arr[3][0]=='O'||arr[3][0]=='T'))
			{
				printf("Case #%d: O won\n",n);
				flag=1;
			}

		}
		if(flag==0)
		{
			if(dots==0)
				printf("Case #%d: Draw\n",n);
			else if(dots>0)
				printf("Case #%d: Game has not completed\n",n);
		}
	}
	return 0;
}

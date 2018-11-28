#include<stdio.h>
#include<cstdio>
#include<iostream>
#include<cstdlib>
#include<cmath>
#include<cstring>
#include<limits.h>
#include<string.h>
#include<algorithm>
#include<vector>
#include<string>
#include<set>
#include<map>
#include<utility>
#include<stack>
#include<queue>
#define tr(c,i)    for(typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)
using namespace std;
int main()
{
	int T;
	scanf("%d",&T);
	int i, j, flag=0;
	int Case=1;
	while(T--)
	{
		flag=0;
		char arr[4][4];
		for(i=0;i<4;i++)
		{
			scanf("%s",arr[i]);
		}
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
				if(arr[i][j]=='.')
				{
					flag=4;
					break;
				}
			}
			if(flag==4)
				break;
		}


		for(i=0;i<4;i++)
		{
			if(((arr[i][0]=='X' || arr[i][0]=='T') && (arr[i][1]=='X' || arr[i][1]=='T') && (arr[i][2]=='X' || arr[i][2]=='T')&&(arr[i][3]=='X' || arr[i][3]=='T')) || ((arr[0][0]=='X' || arr[0][0]=='T') && (arr[1][1]=='X' || arr[1][1]=='T') && (arr[2][2]=='X' || arr[2][2]=='T')&&(arr[3][3]=='X' || arr[3][3]=='T')) || ((arr[0][i]=='X' || arr[0][i]=='T') && (arr[1][i]=='X' || arr[1][i]=='T') && (arr[2][i]=='X' || arr[2][i]=='T')&&(arr[3][i]=='X' || arr[3][i]=='T')) || ((arr[0][3]=='X' || arr[0][3]=='T') && (arr[1][2]=='X' || arr[1][2]=='T') && (arr[2][1]=='X' || arr[2][1]=='T')&&(arr[3][0]=='X' || arr[3][0]=='T')))
			{
				flag=1;
				break;
			}
			else if(((arr[i][0]=='O' || arr[i][0]=='T') && (arr[i][1]=='O' || arr[i][1]=='T') && (arr[i][2]=='O' || arr[i][2]=='T')&&(arr[i][3]=='O' || arr[i][3]=='T')) || ((arr[0][0]=='O' || arr[0][0]=='T') && (arr[1][1]=='O' || arr[1][1]=='T') && (arr[2][2]=='O' || arr[2][2]=='T')&&(arr[3][3]=='O' || arr[3][3]=='T')) || ((arr[0][i]=='O' || arr[0][i]=='T') && (arr[1][i]=='O' || arr[1][i]=='T') && (arr[2][i]=='O' || arr[2][i]=='T')&&(arr[3][i]=='O' || arr[3][i]=='T')) || ((arr[0][3]=='O' || arr[0][3]=='T') && (arr[1][2]=='O' || arr[1][2]=='T') && (arr[2][1]=='O' || arr[2][1]=='T')&&(arr[3][0]=='O' || arr[3][0]=='T')))
			{
				flag=2;
				break;
			}

		}
		if( flag == 1 )
		{
			printf("Case #%d: X won\n",Case);
		}
		else if(flag==2)
		{
			printf("Case #%d: O won\n",Case);
		}
		else if(flag==4)
		{
			printf("Case #%d: Game has not completed\n",Case);
		}
		else
		{
			printf("Case #%d: Draw\n",Case);
		}
		Case++;
	}
	return 0;
}


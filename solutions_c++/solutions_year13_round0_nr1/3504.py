#include <stdio.h>     
#include <iostream>
#include <string.h>     
#include <cstdio>
#include <set>
#include <map>
#include <vector>
#include <algorithm>
#include <stack>
#include <fstream>
#include <sstream>
using namespace std;
char a[7][7];
void clear()
{
	for ( int i = 0 ; i < 7 ; i ++)
	{
		for ( int j =  0 ; j < 7 ;  j++)
		{
			a[i][j] = '.';
		}
	}
}
void ans(int Num , int i)
{
	printf("Case #%d: ",i);
	if ( Num==1)
	{
		printf("X won\n");
	}
	else
		if ( Num==2)
		{
			printf("O won\n");
		}
		else if ( Num==3)
		{
			printf("Draw\n");
		}
		else if ( Num==4)
		{
			printf("Game has not completed\n");
		}
}
int main()
{
	//#ifndef _DEBUG
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
//#endif
	int T;
	scanf("%d",&T);
	for ( int k = 1 ; k <= T; k++)
	{
		clear();
		bool flag = false;
		for ( int i = 0 ; i < 4; i ++)
		{
			for ( int j = 0 ; j < 4; j ++)
			{
				cin >> a[i][j];
				if ( a[i][j]=='.')
					flag = true;
			}
		}
		bool Ans = false;
		for ( int i = 0; i < 4; i ++)
		{
			if (Ans)
				break;
			for ( int j = 0 ; j < 4; j ++)
			{
				if ( i==3 && j==0)
				{
					if ( (a[i][j]=='T' || a[i][j]=='X') && 
					(a[i-1][j+1]=='T' || a[i-1][j+1]=='X') &&	
					(a[i-2][j+2]=='T' || a[i-2][j+2]=='X')&&
					(a[i-3][j+3]=='T' || a[i-3][j+3]=='X') )
				{
					Ans = true;
					ans(1,k);
					break;
				}

				}
				if ( (a[i][j]=='T' || a[i][j]=='X') && 
					(a[i+1][j+1]=='T' || a[i+1][j+1]=='X') &&	
					(a[i+2][j+2]=='T' || a[i+2][j+2]=='X')&&
					(a[i+3][j+3]=='T' || a[i+3][j+3]=='X') )
				{
					Ans = true;
					ans(1,k);
					break;
				}
				if ( (a[i][j]=='T' || a[i][j]=='X') && 
					(a[i+1][j]=='T' || a[i+1][j]=='X') &&	
					(a[i+2][j]=='T' || a[i+2][j]=='X')&&
					(a[i+3][j]=='T' || a[i+3][j]=='X') )
				{
					Ans = true;
					ans(1,k);
					break;
				}
				if ( (a[i][j]=='T' || a[i][j]=='X') && 
					(a[i][j+1]=='T' || a[i][j+1]=='X') &&	
					(a[i][j+2]=='T' || a[i][j+2]=='X')&&
					(a[i][j+3]=='T' || a[i][j+3]=='X') )
				{
					Ans = true;
					ans(1,k);
					break;
				}
			}
		}
		for ( int i = 0; i < 4; i ++)
		{
			if (Ans)
				break;
			for ( int j = 0 ; j < 4; j ++)
			{
				if ( i==3 && j==0)
				{
					if ( (a[i][j]=='T' || a[i][j]=='O') && 
					(a[i-1][j+1]=='T' || a[i-1][j+1]=='O') &&	
					(a[i-2][j+2]=='T' || a[i-2][j+2]=='O')&&
					(a[i-3][j+3]=='T' || a[i-3][j+3]=='O') )
				{
					Ans = true;
					ans(2,k);
					break;
				}
				}
				if ( (a[i][j]=='T' || a[i][j]=='O') && 
					(a[i+1][j+1]=='T' || a[i+1][j+1]=='O') &&	
					(a[i+2][j+2]=='T' || a[i+2][j+2]=='O')&&
					(a[i+3][j+3]=='T' || a[i+3][j+3]=='O') )
				{
					Ans = true;
					ans(2,k);
					break;
				}
				if ( (a[i][j]=='T' || a[i][j]=='O') && 
					(a[i+1][j]=='T' || a[i+1][j]=='O') &&	
					(a[i+2][j]=='T' || a[i+2][j]=='O')&&
					(a[i+3][j]=='T' || a[i+3][j]=='O') )
				{
					Ans = true;
					ans(2,k);
					break;
				}
				if ( (a[i][j]=='T' || a[i][j]=='O') && 
					(a[i][j+1]=='T' || a[i][j+1]=='O') &&	
					(a[i][j+2]=='T' || a[i][j+2]=='O')&&
					(a[i][j+3]=='T' || a[i][j+3]=='O') )
				{
					Ans = true;
					ans(2,k);
					break;
				}
			}
		}
		if ( !Ans)
		{
			if ( flag)
			{
				ans(4,k);
			}
			else
			{
				ans(3,k);
			}
		}
	}
	return 0;	
}
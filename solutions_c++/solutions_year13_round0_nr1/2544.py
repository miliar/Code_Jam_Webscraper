#include <algorithm>
#include <cstdlib>
#include <iostream>
#include <iterator>
#include <set>
#include <vector>
#include<map>
#include<cstdio>
#include<stack>
#include<cstring>
#include<climits>
#include<cmath>
#include<queue>
#include<string>

using namespace std;


bool testDiagonal(char mat[4][4], char p)
{
	if((mat[0][0]=='T' || mat[0][0]==p) && (mat[1][1]=='T' || mat[1][1]==p) && (mat[2][2]=='T' || mat[2][2]==p) && (mat[3][3]=='T' || mat[3][3]==p))
	{
		return true;
	}
	else if((mat[0][3]=='T' || mat[0][3]==p) && (mat[1][2]=='T' || mat[1][2]==p) && (mat[2][1]=='T' || mat[2][1]==p) && (mat[3][0]=='T' || mat[3][0]==p))
	{
		return true;
	}
	return false;
}


bool testrow(char mat[4][4],int m,char &p)
{
	p = mat[m][m];
	if(p=='.')
		return false;
	for(int i=0;i<4;i++)
	{
		if(mat[m][i]!='T' && mat[m][i]!=p)
		{
			return false;
		}
	}
	return true;
}

bool testcol(char mat[4][4],int m,char &p)
{
	p = mat[0][m];
	if(p=='.')
		return false;
	for(int i=0;i<4;i++)
	{
		if(mat[i][m]!='T' && mat[i][m]!=p)
		{
			return false;
		}
	}
	return true;
}

int process(char mat[4][4])
{
	int n = 4;

	if(testDiagonal(mat,'X'))
		return 2;
	else if(testDiagonal(mat,'O'))
		return 1;

	for(int i=0;i<4;i++)
	{
		char ch;
		if(testcol(mat,i,ch))
		{
			return ((ch=='X')?2:1);
		}
		if(testrow(mat,i,ch))
		{
			return ((ch=='X')?2:1);
		}
	}

	return 3;
}

int main()
{
	int t;
	scanf("%d",&t);
	for(int cur=1; cur<=t; cur++)
	{
		char matrix[4][4];
		bool isBlank = false;

		for(int i=0;i<4;i++)
		{
			getchar();
			for(int j=0;j<4;j++)
			{
				scanf("%c",&matrix[i][j]);
				if(matrix[i][j]=='.')
					isBlank = true;
			}
		}
		getchar();

		/*
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				cout<<matrix[i][j];
			}
			cout<<endl;
		}*/


		int result = process(matrix);

		printf("Case #%d: ",cur);
		if(result==1)
		{
			printf("O won\n");
		}
		else if(result==2)
		{
			printf("X won\n");
		}
		else if(result == 3 && !isBlank)
		{
			printf("Draw\n");
		}
		else
		{
			printf("Game has not completed\n");
		}

	}
	return 0;
}



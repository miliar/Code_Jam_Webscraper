#include <cstdio>
#include <iostream>
#include <set>
#include <map>
#include <vector>
#include <algorithm>
#include <fstream>
#include <cstring>
#include <cmath>
#include <string>
#include <queue>
#include <cassert>
using namespace std;
#define PB push_back
#define LL long long
#define ULL unsigned LL
#define LD long double

#define MR 1000
#define ADD 100

int t[MR][MR], R, X1, X2, Y1, Y2, t1[MR][MR];

int main()
{
	freopen("C-small-attempt1.in", "r", stdin);
	freopen("C-small-attempt1.out", "w", stdout);
	int tests;
	scanf("%d", &tests);
	for(int c = 0; c < tests; c++)
	{
		int res = 0;
		scanf("%d", &R);
		int mxX = 0, mxY = 0;
		int mnX = MR, mnY = MR;
		for(int i = 0; i < R; i++)
		{
			scanf("%d%d%d%d", &X1, &Y1, &X2, &Y2);
			mxX = max(mxX, X2);
			mxY = max(mxY, Y2);
			mnX = min(mnX, X1);
			mnY = min(mnY, Y1);
			for(int j = X1; j <= X2; j++)
				for(int l = Y1; l <= Y2; l++)
					t[j][l] = 1;			
		}		
		while(mnX <= mxX && mnY <= mxY)
		{			
			for(int i = mnX; i <= mxX; i++)
				for(int j = mnY; j <= mxY; j++)
					t1[i][j] = t[i][j];
			for(int i = mnX; i <= mxX; i++)
				for(int j = mnY; j <= mxY; j++)
					if(!t[i-1][j] && !t[i][j-1])
						t1[i][j] = 0;
					else if(t[i-1][j] && t[i][j-1])
						t1[i][j] = 1;
			int nmnY = mnY, nmnX = mnX, nmxY = mxY+1, nmxX = mxX+1;
			while(nmnY <= nmxY)
			{				
				bool jest = 0;
				for(int i = mnX; i <= mxX+1; i++)
					if(t1[i][nmnY])
					{
						jest = 1;
						break;
					}
				if(jest)
					break;
				nmnY++;				
			}
			while(nmnX <= nmxX)
			{				
				bool jest = 0;
				for(int i = mnY; i <= mxY+1; i++)
					if(t1[nmnX][i])
					{
						jest = 1;
						break;
					}
				if(jest)
					break;
				nmnX++;				
			}
			while(nmnY <= nmxY)
			{				
				bool jest = 0;
				for(int i = mnX; i <= mxX+1; i++)
					if(t1[i][nmxY])
					{
						jest = 1;
						break;
					}
				if(jest)
					break;
				nmxY--;				
			}
			while(nmnX <= nmxX)
			{				
				bool jest = 0;
				for(int i = mnY; i <= mxY+1; i++)
					if(t1[nmxX][i])
					{
						jest = 1;
						break;
					}
				if(jest)
					break;
				nmxX--;				
			}
			for(int i = mnX; i <= mxX; i++)
				for(int j = mnY; j <= mxY; j++)
					t[i][j] = 0;
			for(int i = nmnX; i <= nmxX; i++)
				for(int j = nmnY; j <= nmxY; j++)
				{
					t[i][j] = t1[i][j];
					t1[i][j] = 0;
				}
			mnX = nmnX; mnY = nmnY; mxX = nmxX; mxY = nmxY;
			res++;
		}
		printf("Case #%d: %d\n", c+1, res);
	}
	return 0;
}
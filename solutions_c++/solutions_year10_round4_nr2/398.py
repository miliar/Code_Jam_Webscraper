#include <iostream>
#include "stdafx.h"
#include <stdlib.h>
#include <memory.h>
//using namespace std;

#include <iostream>
using namespace std;

void testcase(int ncase);

const int maxP = 11;
int M[1 << maxP];
int price[1 << maxP];
int f[1 << (maxP + 1)][maxP + 1];

int main() {
	freopen("B-large.in", "r", stdin);
	freopen("output.txt", "w+", stdout);
	int T;
	scanf("%d", &T);
	for (int i = 0; i < T; ++ i) {
		testcase(i + 1);
	}
	return 0;
}

void testcase(int ncase) {
	int P;
	scanf("%d", &P);
	for (int i = 0; i < (1 << P); ++ i)
		scanf("%d", &M[i]);
	memset(price, 0, sizeof(price));
	for (int i = 0; i < P; ++ i) 
		for (int j = 0; j < (1 << (P - i - 1)); ++ j) 
			// level (P - i - 1), the j-th node
			scanf("%d", &price[(1 << (P - i - 1)) + j - 1]);
	/*
	for (int i = 0; i < (1 << P); ++ i)
	printf("M[%d] = %d\n", i, M[i]);*/
	memset(f, -1, sizeof(f));
	for (int i = 0; i < (1 << P); ++ i) 
		for (int c = 0; c <= M[i]; ++ c) 
			f[(1 << P) + i - 1][c] = 0;
	for (int i = (1 << P) - 1; i >= 0; -- i) {
		int k1 = i * 2 + 1;
		int k2 = i * 2 + 2;
		//printf("price[%d] = %d\n", i, price[i]);
		for (int c = P; c >= 0; -- c) {
			if (f[k1][c] != -1 && f[k2][c] != -1)
				if (f[i][c] == -1 || price[i] + f[k1][c] + f[k2][c] < f[i][c])
					f[i][c] = price[i] + f[k1][c] + f[k2][c];
			if (c != P && f[k1][c + 1] != -1 && f[k2][c + 1] != -1)
				if (f[i][c] == -1 || f[k1][c + 1] + f[k2][c + 1] < f[i][c])
					f[i][c] = f[k1][c + 1] + f[k2][c + 1];
			if (c != P && f[i][c + 1] != -1 && f[i][c + 1] < f[i][c])
				f[i][c] = f[i][c + 1];
			//printf("f[%d][%d] = %d\n", i, c, f[i][c]);
		}
	}
	printf("Case #%d: %d\n", ncase, f[0][0]);
}

// 1.cpp : Defines the entry point for the console application.


//#include "stdafx.h"
//#include <stdio.h>
//#include <map>
//#include <set>
//#include <algorithm>
//#include <string>
//#include <string.h>
//#include <memory.h>
//#include <stdlib.h>
//#include <vector>
//#include <queue>
//#include <math.h>
//using namespace std;
//int T,R;
//bool grid[150][150];
//bool _grid[150][150];
//bool check(int M_X,int N_X,int M_Y,int N_Y)
//{
//	for(int i = M_X; i <= N_X; ++ i)
//		for(int d = M_Y; d <= N_Y; ++ d)
//			if(grid[i][d]) return false;
//	return true;
//}
//int main()
//{
//	scanf("%d",&T);
//	int X1,X2,Y1,Y2;
//	for(int i = 1; i <= T; ++ i)
//	{
//		int Z  = 0;
//		memset(grid,false,sizeof grid);
//		scanf("%d",&R);
//		int M_X = 105,N_X = -1,M_Y = 105,N_Y = -1;
//		for(int k = 0; k < R; ++ k)
//		{
//			scanf("%d%d%d%d",&X1,&Y1,&X2,&Y2);
//			if(X1 < M_X) M_X = X1;
//			if(X2 > N_X) N_X = X2;
//			if(Y1 < M_Y) M_Y = Y1;
//			if(Y2 > N_Y) N_Y = Y2;
//			for(int d = X1;d <=X2; ++ d)
//				for(int z = Y1; z <= Y2; ++ z)
//				{
//					grid[d][z] = true;
//				}
//		}
//		int dir[] = {-1,0};
//		while(true)
//		{
//			for(int d = M_X; d <= N_X; ++ d)
//			{
//				for(int z = M_Y; z <= N_Y; ++ z)
//				{
//					printf("%d ",grid[d][z]);
//					if(grid[d][z] == true)
//					{
//						int M = 0;
//						for(int k = 0; k < 2; ++ k)
//						{
//							X1 = d + dir[k];
//							Y1 = z + dir[1 - k];
//							if(X1 >= M_X && Y1 >= M_Y && X1 <= N_X && Y1 <= N_Y && grid[X1][Y1]) ++ M;
//						}
//						if(M == 0) _grid[d][z] = false;
//					}
//					else 
//					{
//						int M = 0;
//						for(int k = 0; k < 2; ++ k)
//						{
//							X1 = d + dir[k];
//							Y1 = z + dir[1 - k];
//							if(X1 >= M_X && Y1 >= M_Y && X1 <= N_X && Y1 <= N_Y && grid[X1][Y1]) ++ M;
//						}
//						if(M == 2) _grid[d][z] = true;
//					}
//				}
//				puts("");
//			}
//			if(check(M_X,N_X,M_Y,N_Y)) break;
//			for(int d = M_X; d <= N_X; ++ d)
//			{
//				for(int z = M_Y; z <= N_Y; ++ z)
//					grid[d][z] = _grid[d][z];
//			}
//			++ Z;
//		}
//		printf("Case #%d: %d\n",i,Z);
//	}
//	return 0;
//}
//

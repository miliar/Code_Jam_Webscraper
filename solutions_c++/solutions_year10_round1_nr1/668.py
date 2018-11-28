// 10_1a.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
using namespace std;

#define REP(i,a,b) for (int i = a; i < b; i++)

const int dir[][2] = {{0,1},{1,0},{1,1},{-1,-1},{0,-1},{-1,0},{1,-1},{-1,1}};
int main()
{
	//freopen("A-small-attempt0.in","r",stdin);
	//freopen("A-small.in","r",stdin);
	freopen("A-large.in","r",stdin);
	freopen("a.txt","w",stdout);

	int t,n,k;
	char a[100][100];

	scanf("%d",&t);
	for (int zz = 1; zz <= t; zz++)
	{
		printf("Case #%d: ",zz);

		scanf("%d%d",&n,&k);
		getchar();
		REP(i,0,n)
		{
			REP(j,0,n)
				scanf("%c",&a[i][j]);
			getchar();
		}

		REP(i,0,n)
		{
			int p = n - 1;
			for (int j = n-1; j >= 0; j--)
			{
				if (a[i][j] != '.')
					swap(a[i][j],a[i][p--]);
			}
		}

		bool blue = false,red = false;
		REP(i,0,n)
			REP(j,0,n)
		{
			if (a[i][j] == '.') continue;
			//printf("i =  %d  j = %d\n",i,j);
			for (int ti = 0; ti < 8; ti++)
			{
				int p,si = dir[ti][0],sj = dir[ti][1];
				for (p = 0; p < k; p++)
				{
					int ii = i + si,jj = j + sj;
					//printf("%d %d\n",ii,jj);
					if (ii < 0 || ii >= n || jj < 0 || jj >= n) break;
					if (a[ii][jj] != a[i][j]) break;
					si += dir[ti][0],sj += dir[ti][1];
				}
				if (p == k-1)
				{
					if (a[i][j] == 'B') blue = true;
					else if (a[i][j] == 'R') red = true;
				}
				//printf("blue %d red %d\n",blue,red);
			}
		}

		if (blue && red)
			printf("Both\n");
		else if (!blue && !red)
			printf("Neither\n");
		else if (blue)
			printf("Blue\n");
		else if (red)
			printf("Red\n");
	}

	return 1;
}
//
//int t,n,cd,ci,m;
//	int a[101] = {0};
//
//	scanf("%d",&t);
//	for (int zz = 1; zz <= t; zz++)
//	{
//		printf("Case #%d: ",zz);
//
//		scanf("%d%d%d",&cd,&ci,&m,&n);
//		REP(i,0,n)
//			scanf("%d",&a[i]);
//
//
//	}

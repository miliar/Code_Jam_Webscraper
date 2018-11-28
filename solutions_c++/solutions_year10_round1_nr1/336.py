// codejam.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>

using namespace std;

const int MAXN = 100;

int n, m;
char map[MAXN][MAXN], rot[MAXN][MAXN];
bool blue, red;

void init()
{
	char c;
	int i, j;

	scanf("%d%d", &n, &m);
	for (i=0; i<n; i++)
		for (j=0; j<n; j++){
			while (scanf("%c", &c), (c!='R' && c!='B' && c!='.'));
			map[i][j] = c;
		}
}

void goover(int sx, int sy, int dx, int dy)
{
	int cnt = 0;
	char last = '?';
	while (sx>=0 && sx<n && sy>=0 && sy<n){
		if (last!='?' && rot[sx][sy]==last)
			cnt++;
		else
			cnt = 1;
		if (cnt>=m){
			if (rot[sx][sy]=='B') blue = true;
			if (rot[sx][sy]=='R') red = true;
		}
		last = rot[sx][sy];
		sx+=dx;
		sy+=dy;
	}
}

void work()
{
	int i, j, k;

	memset(rot, '.', sizeof(rot));
	for (i=0; i<n; i++){
		k = n-1;
		for (j=n-1; j>=0; j--)
			if (map[i][j]!='.'){
				rot[k][i] = map[i][j];
				k--;
			}
	}
	blue = red = false;
	
	for (i=0; i<n; i++){
		goover(i, 0, 0, 1);
		goover(0, i, 1, 0);

		goover(0, i, 1, 1);
		goover(i, 0, -1, 1);
		goover(i, 0, 1, 1);
		goover(n-1, i, -1, 1);
	}
	if (blue && red)
		printf("Both\n");
	else
	if (!blue && !red)
		printf("Neither\n");
	else
	if (blue)
		printf("Blue\n");
	else
		printf("Red\n");
	
}

int main()
{
	int t, i;
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d", &t);
	i = 0;
	while (t--){
		printf("Case #%d: ", (++i));
		init();
		work();
	}

	return 0;
}

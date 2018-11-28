#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <string.h>
#include <string>
#include <vector>
#include <map>
#include <cmath>
#include <set>
#include <algorithm>
#include <queue>
#include <cassert>
#include <fstream>
#include <sstream>
#include <bitset>
#include <stack>
#include <list>
#define debug1(x) cout << #x" = " << x << endl;
#define debug2(x, y) cout << #x" = " << x << " " << #y" = " << y << endl;
#define debug3(x, y, z) cout << #x" = " << x << " " << #y" = " << y << " " << #z" = " << z << endl;
#define debug4(x, y, z, w) cout << #x" = " << x << " " << #y" = " << y << " " << #z" = " << z << " " << #w" = " << w << endl;
using namespace std;

int T;
int testid;

double ept[2000];
double trans[2000][2000];
double D[2000];
double jie[2000];
void _init()
{
	ept[0] = 0;
	ept[1] = 0;
	ept[2] = 2;
	
	D[0] = 1;
	D[1] = 0;
	D[2] = 1;
	for (int i = 3; i <= 1000; ++i)
		D[i] = (i - 1) * (D[i - 1] + D[i - 2]);

	jie[0] = 1;
	jie[1] = 1;
	for (int i = 2; i <= 1000; ++i)
		jie[i] = jie[i - 1] * i;

	for (int i = 3; i <= 1000; ++i)
		for (int j = 0; j <= i; ++j)
			trans[i][j] = D[j] / jie[j] / jie[i - j];

	for (int i = 3; i <= 10; ++i)
	{
		double t = 1;
		for (int j = 0; j < i; ++j)
			t += trans[i][j] * ept[j];
		//debug3(i, t, trans[i][i]);
		ept[i] = t / (1 - trans[i][i]);
	}

	//for (int i = 1; i <= 10; ++i)
	//	cout << ept[i] << endl;
}

int N;
void init()
{
	cin >> N;
	int diff = 0;
	for (int i = 1; i <= N; ++i)
	{
		int d;
		cin >> d;
		if (d != i) diff++;
	}

	printf("Case #%d: %.6f\n", testid, (double)diff);
}

void york()
{
}

int main()
{
	_init();
	scanf("%d", &T);
	for (testid = 1; testid <= T; ++testid)
	{
		init();
		york();
	}

	return 0;
}




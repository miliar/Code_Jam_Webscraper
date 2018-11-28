#include <iostream>
#include <fstream>
#include <cmath>
#include <vector>
#include <algorithm>
#include <iomanip>
#include <cstdio>
#include <map>
#include <set>
#include <sstream>
#include <strstream>
#include <queue>
#include <stack>
#include <set>
#include <cstring>
#include <string>

using namespace std;

ifstream in("small.in");
ofstream out("small.out");

int a[110][110];
int b[110][110];

int n;

bool datark()
{
	int i,j;
	for (i = 0 ;i < 110; i ++)
		for (j = 0 ; j < 110; j++)
			if (a[i][j] == 1)
				return false;
	return true;
}

void next()
{
	int i,j;
	for (i = 0 ;i < 110; i ++)
		for (j = 0 ; j < 110; j++)
		{
			if (a[i][j] == 0 && (i > 0 && a[i - 1][j] == 1 && j > 0 && a[i][j - 1] == 1))
				b[i][j] = 1; else
			if (a[i][j] == 1 && (i > 0 && a[i - 1][j] == 0 && j > 0 && a[i][j - 1] == 0))
				b[i][j] = 0; else
				b[i][j] = a[i][j];
		}

	for (i = 0 ;i < 110; i ++)
		for (j = 0 ; j < 110; j++)
			a[i][j] = b[i][j];

}

int main()
{
	int test,i,j,u,v;
	in >> test;	
	for (int t = 1; t <= test; t++)	
	{
		in >> n;

		for (i = 0 ; i< 110; i++)
			for (j = 0; j < 110; j++)
				a[i][j] = 0;

		for (i = 0; i < n ; i++)
		{
			int x1,y1,x2,y2;

			in >> x1 >> y1 >> x2 >> y2;

			for (u = x1; u <= x2; u++)
				for (v = y1; v <= y2; v++)
					a[u][v] = 1;
		}

		int answer = 0;

		while (!datark())
		{
			next();
			answer++;
			
		}

		out << "Case #" << t << ": " << answer << endl;
	}
	return 0;
}
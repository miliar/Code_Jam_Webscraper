#include <cstdio>
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <string>
#include <set>
#include <map>
#include <ctime>
#include <cstring>
#include <cassert>
#include <sstream>

using namespace std;

#define forn(i, n) for(int i = 0; i < (int)(n); i++)
#define ford(i, n) for(int i = (int)(n) - 1; i >= 0; i--)
#define pb push_back
#define mp make_pair
#define fs first
#define sc second
#define last(a) int(a.size() - 1)
#define all(a) a.begin(), a.end()
#define seta(a,x) memset (a, x, sizeof (a))
#define I (int)

typedef long long int64;
typedef pair <int, int> pii;
typedef long double ldb;

const long double eps = 1e-9;
const int inf = (1 << 30) - 1;
const int64 inf64 = ((int64)1 << 62) - 1;
const long double pi = 3.1415926535897932384626433832795;
const string task = "";

template <class T> T sqr (T x) {return x * x;}

int n, m;
int a[100][100];
char s[100][100];
char it;
const int dx[4] = {-1, 0, 0, 1};
const int dy[4] = {0, -1, 1, 0};

char go (int vx, int vy)
{
	if (s[vx][vy] != 0)
		return s[vx][vy];
	int x1, y1, z1;
	x1 = y1 = -1;
	z1 = inf;
	forn (i, 4)
	{
		int x = vx + dx[i];
		int y = vy + dy[i];
		if (x < 0 || x >= n || y < 0 || y >= m)
			continue;
		if (a[x][y] >= a[vx][vy])
			continue;
		if (a[x][y] < z1)
		{
			z1 = a[x][y];
			x1 = x;
			y1 = y;
		}
	}		
	if (x1 == -1)
	{
		s[vx][vy] = it;
		it ++;
		return s[vx][vy];
	}
	else
		return s[vx][vy] = go (x1, y1);
}

int main ()
{
	int nn;
	scanf ("%d", &nn);
 	forn (ii, nn)
 	{
 		scanf ("%d%d", &n, &m);
 		forn (i, n)
 			forn (j, m)
 				scanf ("%d", &a[i][j]);
 		seta (s, 0);
 		it = 'a';
 		forn (i, n)
 			forn (j, m)
 				if (s[i][j] == 0)
 					go (i, j);
 		printf ("Case #%d:\n", ii+1);
 		forn (i, n)
 		{
 			forn (j, m)
 				printf ("%c ", s[i][j]);
 			printf ("\n");
 		}
 	}
	return 0;
}

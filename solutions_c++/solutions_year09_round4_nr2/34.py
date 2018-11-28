#include <algorithm>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <cmath>
#include <queue>
#include <assert.h>
using namespace std;

typedef long long LL;
typedef vector <string> vs;
typedef vector <int> vi;
typedef vector <LL> vll;
typedef vector <double> vd;
typedef pair <int,int> pii;


vs token(string s, string d)
{
	string t;
	vs res;
	int pos;
	while (true)
	{
		pos = s.find(d);
		if (pos == -1) break;
		t = s.substr(0, pos);
		s = s.substr(pos+d.length());
		if (t != "") res.push_back( t );
	}
	if (s != "") res.push_back( s );
	return res;
}

vs token(string s)
{
	return token(s, " ");
}

vi s2vi(string s, string d)
{
	vs tvs = token(s, d);
	vi res;
	int i;
	for (i=0; i<tvs.size(); i++) res.push_back( atoi(tvs[i].c_str()) );
	return res;
}

vi s2vi(string s)
{
	return s2vi(s, " ");
}

////////////////////////////////////////////

int tc, ntc;
int n, m, h;

int dp[51][51][51][51];
char mm[51][51];

#define INF 1000000

int doit(int y, int x, int ca, int cb)
{
	if (y == n-1) return 0;
	int& res = dp[y][x][ca][cb];
	if (res != -1) return res;

	// try to create hole at y, i, or fall
	res = INF;
	int i, j;

	// no hole
	for (i=x; i<m; i++)
	{
		if (mm[y][i] == '#' && !(ca <= i && i < cb)) break;
		if (mm[y+1][i] == '.')
		{
			for (j=y+2; j<n; j++) if (mm[j][i] == '#') break;
			int ny = j - 1;
			if (ny - y > h) break;

			res = min(res, doit(ny, i, 0, 0));
			break;
		}
	}
	int right_most = i - 1;

	for (i=x-1; i>=0; i--)
	{
		if (mm[y][i] == '#' && !(ca <= i && i < cb)) break;
		if (mm[y+1][i] == '.')
		{
			for (j=y+2; j<n; j++) if (mm[j][i] == '#') break;
			int ny = j - 1;
			if (ny - y > h) break;

			res = min(res, doit(ny, i, 0, 0));
			break;
		}
	}
	int left_most = i + 1;

	// creating hole
	for (i=left_most; i<=right_most; i++) for (j=i; j<=right_most; j++)
	{
		if (i == left_most && j == right_most) continue;
		int cost = j-i+1;
	
		int k, ny, nx;
		if (i != left_most)
		{			
			nx = i;
			for (k=y+2; k<n; k++) if (mm[k][nx] == '#') break;
			ny = k - 1;
			if (ny - y <= h) 
			{
				if (ny == y + 1)
					res = min(res, cost + doit(ny, nx, i, j+1));
				else
					res = min(res, cost + doit(ny, nx, 0, 0));
			}
		}

		if (i != right_most)
		{
			nx = j;
			for (k=y+2; k<n; k++) if (mm[k][nx] == '#') break;
			ny = k - 1;
			if (ny - y <= h) 
			{
				if (ny == y + 1)
					res = min(res, cost + doit(ny, nx, i, j+1));
				else
					res = min(res, cost + doit(ny, nx, 0, 0));
			}
		}
	}

	return res;
}

int main()
{
	FILE* fi = fopen("B-large.in", "r");
	FILE* fo = fopen("B-large.out", "w");

	fscanf(fi, "%d", &ntc);
	int i;
	for (tc=1; tc<=ntc; tc++)
	{
		fscanf(fi, "%d %d %d", &n, &m, &h);
		for (i=0; i<n; i++) fscanf(fi, "%s", mm[i]);

		memset(dp, -1, sizeof(dp));
		int res = doit(0, 0, 0, 0);

		printf("Case #%d: ", tc);
		if (res == INF) printf("No\n");
		else printf("Yes %d\n", res);	

		fprintf(fo, "Case #%d: ", tc);
		if (res == INF) fprintf(fo, "No\n");
		else fprintf(fo, "Yes %d\n", res);	
	}

	fclose(fi); fclose(fo);
}
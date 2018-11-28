#pragma warning(disable:4786)

#include <vector>
#include <string>
#include <map>
#include <set>
#include <cstdio>
#include <algorithm>
#include <queue>
#include <sstream>
#include <iostream>
#include <fstream>

using namespace std;

#define VT vector
typedef VT<int> VI;
typedef VT<VI> VVI;
typedef VT<string> VS;
typedef VT<double> VD;
typedef pair<int,int> PII;
#define REP(i,n) for (int i = 0; i < (n); i++)
#define ALL(c) c.begin(),c.end()
#define pb push_back
#define mp make_pair
#define fs first
#define sc second
#define sz size()

ifstream ifs;
ofstream ofs;

typedef long long ll;

int x1[1024];
int x2[1024];
int y1[1024];
int y2[1024];

bool intersects(int i, int j) {

	if (y2[j] < (y1[i]-1)) return false;
	if (y1[j] > (y2[i]+1)) return false;
	if (x2[j] < (x1[i]-1)) return false;
	if (x1[j] > (x2[i]+1)) return false;

	if (((x2[j]+1) == x1[i]) && ((y2[j]+1) == y1[i])) return false;
	if (((x2[i]+1) == x1[j]) && ((y2[i]+1) == y1[j])) return false;
 
	return true;
}

void testcase(int tst)
{
	int n;
	ifs >> n;

	REP(i, n)
		ifs >> x1[i] >> y1[i] >> x2[i] >> y2[i];

	VI color(n, -1);

	int cur = 0;

	REP(i, n) {
		
		VI colors;
		REP(j, i)
			if (intersects(i, j)) {
				colors.pb(color[j]);
			}

		if (colors.sz == 0) {
			color[i] = cur++;
		} else {
			if (colors.sz == 1) {
				color[i] = colors[0];
			} else {
				color[i] = colors[0];
				REP(j, i)
					if (find(ALL(colors), color[j]) != colors.end())
						color[j] = colors[0];
			}
		}
	}

	int res = 0;
	REP(i, cur) {

		int mn = 1000000000;
		int maxx = -1, maxy = -1;
		REP(j, n)
			if (color[j] == i) {
				mn = min(mn, x1[j] + y1[j]);
				maxx = max(maxx, x2[j]);
				maxy = max(maxy, y2[j]);
			}
		res = max(res, maxx+maxy-mn+1);
	}

	ofs << "Case #" << tst+1 << ": " << res << endl;
}

int main()
{
	ifs.open("input.txt");
	ofs.open("output.txt");
	
	int t;
	ifs >> t;
	REP(tn, t)
	{
		testcase(tn);
	}

	return 0;
} 

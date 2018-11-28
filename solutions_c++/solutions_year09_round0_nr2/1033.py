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
#include <math.h>
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

int h, w;
vector<vector<int> > el;
VVI was;

vector<vector<char> > result;

char curletter;

const int dx[] = {0,-1,1,0};
const int dy[] = {-1,0,0,1};
const int op[] = {3,2,1,0};

bool hasedge(int j, int i, int cz) {

	if (j < 0 || j >= h || i < 0 || i >= w) return false;
	
	int minl = 1000000000, minz = -1;

	REP(z, 4) {
		int nj = j+dy[z];
		int ni = i+dx[z];
		if (nj < 0 || nj >= h || ni < 0 || ni >= w) continue;
		
		if (el[nj][ni] < minl) {
			minl = el[nj][ni];
			minz = z;
		}
	}

	if (minl >= el[j][i]) return false;
	return cz == minz;
}

void go(int j, int i) {

	if (j < 0 || j >= h || i < 0 || i >= w || was[j][i]) return;
	was[j][i] = 1;
	result[j][i] = curletter;

	REP(z, 4)
		if (hasedge(j, i, z) || hasedge(j+dy[z], i+dx[z], op[z])) {
			go(j+dy[z], i+dx[z]);
		}
}

void testcase(int tst)
{
	ifs >> h >> w;

	el.assign(h, VI(w, 0));

	REP(j, h)
		REP(i, w)
			ifs >> el[j][i];

	was.assign(h, VI(w, 0));
	result.assign(h, vector<char>(w, ' '));

	curletter = 'a';

	REP(j, h)
		REP(i, w)
		if (!was[j][i]) {
			go(j, i);
			curletter++;
		}

	ofs << "Case #" << tst+1 << ":" << endl;

	REP(j, h) {
		REP(i, w) {
			if (i) ofs << ' ';
			ofs << result[j][i];
		}
		ofs << endl;
	}

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

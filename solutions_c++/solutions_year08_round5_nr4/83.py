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
#include <queue>
#include <fstream>

using namespace std;

typedef vector <string> vs;
typedef vector <int> vi;
#define REP(a,b) for(long long a=0;a<(b);++a)
#define FOR(a,c,b) for(long long  a=c;a<(b);++a)

#define mod 10007

vector <pair<int,int> > r;

const int dx[] = {-2, -1};
const int dy[] = {-1, -2};

int m[1000][1000];

int count(int x, int y) {
	if (x < 1 || y < 1) return 0;
	if (m[x][y] < 0) {
		m[x][y] = (count(x-2, y-1) + count(x-1, y-2))%mod;
	}

	return m[x][y];
}

int main()
{
	ifstream fin("D-small.in");
	ofstream fout("D-small.out");
	//ifstream fin("D-large.in");
	//ofstream fout("D-large.out");

	long long nc, h, w, nr;

	fin >> nc;

	for (int tc = 1; tc <= nc; ++tc)
	{
		fout <<"Case #"<<tc<<": ";	
		fin >> h >> w >> nr;
		r.resize(nr);
		
		memset(m, -1, sizeof(m));
		m[1][1] = 1;

		REP(i,nr) {
			fin >> r[i].first >> r[i].second;
			m[r[i].second][r[i].first] = 0;
		}
		fout << count(w, h) << endl;
	}

	fin.close();
	fout.close();

	return 0;
}


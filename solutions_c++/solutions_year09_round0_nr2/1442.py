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

const int MAX = 101;

int b[MAX][MAX];
int p[MAX][MAX];
int d[MAX][MAX];

char asgn[MAX*MAX];

int dh[] = {-1,0,0,1};
int dw[] = {0,-1,1,0};

int find(int a, int b)
{
	if (p[a][b] == ((a<<8)|b))
		return (a<<8)|b;
	else
		return p[a][b] = find(p[a][b]>>8, p[a][b]&255);
}

void make_union(int a, int b, int c, int d)
{
	int ra = find(a, b);
	int rb = find(c, d);
	p[ra>>8][ra&255] = rb;
}

int main()
{
	int t, h, w, nh, nw;

	//ifstream fin("B-small.in");
	//ofstream fout("B-small.out");
	ifstream fin("B-large.in");
	ofstream fout("B-large.out");

	fin >> t;

	REP(tc,t) {
		fout <<"Case #"<<tc+1<<":"<<endl;	

		fin >> h >> w;

		int k = 1;
		REP(i,h) REP(j,w) {
			fin >> b[i][j];
			d[i][j] = k++;
			p[i][j] = (i<<8) | j;
		}

		REP(i,h) REP(j,w) {
			int low = 9999999, dir = -1;
			REP(z,4) {
				nh = i + dh[z];
				nw = j + dw[z];
				if (nh < 0 || nw < 0 || nh >= h || nw >= w) continue;
				if (low > b[nh][nw]) { low = b[nh][nw]; dir = z; }
			}
			if (low >= b[i][j]) continue;
			make_union(i,j,i+dh[dir],j+dw[dir]);			
		}

		memset(asgn, 0, sizeof(asgn));
		char next = 'a';
		REP(i,h) REP(j,w) {
			int c = find(i,j);
			int id = d[c>>8][c&255];
			if (asgn[id] == 0) {
				asgn[id] = next;
				++next;
			}
			fout << asgn[id];
			if (j < w-1) fout << " ";
			else fout << endl;
		}

	}


	fin.close();
	fout.close();

	return 0;
}


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

int r, c, f;
string b[100];
int m[11][7][64][64][64];
char o[11][7][64][64][64];

int str2msk(string s) {
	int m = 0;

	REP (i,s.size()) {
		m <<= 1;
		if (s[i] == '#')
			m |= 1;		
	}

	return m;
}

string msk2str(int m) {
	string s;
	REP(i,c) if (m&(1<<(c-1-i))) s += '#';
	else s+=".";
	return s;
}


int go(int cr, int cc, int msk1, int msk2, int msk3) {
	if (o[cr][cc][msk1][msk2][msk3]) return 9999;
	if (m[cr][cc][msk1][msk2][msk3] == -1) {
		if (cr == r-1) 
			m[cr][cc][msk1][msk2][msk3] = 0;
		else {
			string b[50];
			REP(i,r) b[i] = ::b[i];
			string tmp1 = cr==0?"":b[cr-1], tmp2 = b[cr], tmp3 = b[cr+1];
			if (cr>0) b[cr-1] = msk2str(msk1);
			b[cr] = msk2str(msk2);
			b[cr+1] = msk2str(msk3);
			
			m[cr][cc][msk1][msk2][msk3] = 9999;
			o[cr][cc][msk1][msk2][msk3] = 1;

			//move right
			if (cc != c-1 && b[cr][cc+1] != '#') {
				if (b[cr+1][cc+1] == '#')
					m[cr][cc][msk1][msk2][msk3] = min(m[cr][cc][msk1][msk2][msk3], go(cr,cc+1,msk1,msk2,msk3));
				else {	// fall
					int len = 1, d = cr+1;
					while (d < r-1 && b[d+1][cc+1] == '.') { ++len; ++d; }
					if (len <= f) {
						m[cr][cc][msk1][msk2][msk3] = min(m[cr][cc][msk1][msk2][msk3], go(d,cc+1,str2msk(b[d-1]),str2msk(b[d]),d == r-1 ? 0 : str2msk(b[d+1])));
					}
				}
			}

			// move left
			if (cc != 0 && b[cr][cc-1] != '#') {
				if (b[cr+1][cc-1] == '#')
					m[cr][cc][msk1][msk2][msk3] = min(m[cr][cc][msk1][msk2][msk3], go(cr,cc-1,msk1,msk2,msk3));
				else {	// fall
					int len = 1, d = cr+1;
					while (d < r-1 && b[d+1][cc-1] == '.') { ++len; ++d; }
					if (len <= f) {
						m[cr][cc][msk1][msk2][msk3] = min(m[cr][cc][msk1][msk2][msk3], go(d,cc-1,str2msk(b[d-1]),str2msk(b[d]),d == r-1 ? 0 : str2msk(b[d+1])));
					}
				}
			}

			// dig right
			if (cc != c-1 && b[cr+1][cc+1] == '#' && b[cr][cc+1] == '.') {
				b[cr+1][cc+1] = '.';
				m[cr][cc][msk1][msk2][msk3] = min(m[cr][cc][msk1][msk2][msk3], 1+go(cr,cc,msk1,str2msk(b[cr]),str2msk(b[cr+1])));
				b[cr+1][cc+1] = '#';
			}

			// dig left
			if (cc != 0 && b[cr+1][cc-1] == '#' && b[cr][cc-1] == '.') {
				b[cr+1][cc-1] = '.';
				m[cr][cc][msk1][msk2][msk3] = min(m[cr][cc][msk1][msk2][msk3], 1+go(cr,cc,msk1,str2msk(b[cr]),str2msk(b[cr+1])));
				b[cr+1][cc-1] = '#';
			}

			if (cr>0) b[cr-1] = tmp1;
			b[cr] = tmp2;
			b[cr+1] = tmp3;
			o[cr][cc][msk1][msk2][msk3] = 0;
		}
	}

	return m[cr][cc][msk1][msk2][msk3];

}

int main()
{
	int n;

	ifstream fin("B-small.in");
	ofstream fout("B-small.out");
	//ifstream fin("B-large.in");
	//ofstream fout("B-large.out");

	fin >> n;

	REP(tc,n) {
		fout <<"Case #"<<tc+1<<": ";
		fin >> r >> c >> f;

		REP(i,r) fin >> b[i];

		memset(m, -1, sizeof(m));
		memset(o, 0, sizeof(o));

		int best = go(0,0,0,str2msk(b[0]), str2msk(b[1]));

		if (best == 9999) fout << "No" << endl;
		else fout << "Yes " << best << endl;
	}

	fin.close();
	fout.close();

	return 0;
}


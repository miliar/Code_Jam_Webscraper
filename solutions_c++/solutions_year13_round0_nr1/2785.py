#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <ctype.h>
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

using namespace std;

#define FOR(i,a,b) for(int i=(a);i<(int)(b);i++)
#define REP(i,a) for(int i=0;i<(int)(a);i++)
#define ALL(i) i.begin(),i.end()
#define rALL(i) i.rbegin(),i.rend()
#define PB push_back

typedef vector<int> vi;
typedef vector<vector<int> > vvi;

template<class T> string i2a(T x) {ostringstream oss; oss<<x; return oss.str();}

void printvec(vector<int> a)
{
 cout<<"Vecteur:  ";
 REP(i,a.size()) cout<<a[i]<<"  ";
 cout<<endl;
}

bool same(string s) {
	for(int i = 1; i < s.size(); i++) {
		if(s[i] != s[i-1]) return false;
	}
	return true;
}

int main()
{

   freopen("A-large.in","r",stdin);
   freopen("A-large.out","w",stdout);


	int cases;
	string s;

	getline(cin, s);
	sscanf(s.c_str(), "%d", &cases);

	REP(k, cases) {
		printf("Case #%d: ", k + 1);
		char result = '-';
		bool p = false;
		vector<string> grid;
		REP(i, 4) {
			getline(cin, s);
			grid.PB(s);
		}

		REP(i, 4) {
			int o = 0, x = 0, t = 0;
			REP(j, 4) {
				char c = grid[i][j];
				if(c == 'O') o++;
				else if(c == 'X') x++;
				else if(c == 'T') t++;
			}
			if(o == 4 || (o == 3 && t == 1)) {
				result = 'O';
			} else if(x == 4 || (x == 3 && t == 1)) {
				result = 'X';
			}
		}

		if(result == '-') {
			REP(j, 4) {
				int o = 0, x = 0, t = 0;
				REP(i, 4) {
					char c = grid[i][j];
					if(c == 'O') o++;
					else if(c == 'X') x++;
					else if(c == 'T') t++;
				}
				if(o == 4 || (o == 3 && t == 1)) {
					result = 'O';
				} else if(x == 4 || (x == 3 && t == 1)) {
					result = 'X';
				}
			}
		}

		if(result == '-') {
			int o = 0, x = 0, t = 0;
			REP(i, 4) {
				char c = grid[i][i];
				if(c == 'O') o++;
				else if(c == 'X') x++;
				else if(c == 'T') t++;
			}
			if(o == 4 || (o == 3 && t == 1)) {
				result = 'O';
			} else if(x == 4 || (x == 3 && t == 1)) {
				result = 'X';
			}
		}

		if(result == '-') {
			int o = 0, x = 0, t = 0;
			REP(i, 4) {
				char c = grid[i][3-i];
				if(c == 'O') o++;
				else if(c == 'X') x++;
				else if(c == 'T') t++;
			}
			if(o == 4 || (o == 3 && t == 1)) {
				result = 'O';
			} else if(x == 4 || (x == 3 && t == 1)) {
				result = 'X';
			}
		}

		if(result == '-') {
			REP(i, 4) {
				REP(j, 4) {
					if(grid[i][j] == '.') {
						result = 'N';
					}
				}
			}
		}

		if(result == 'O') {
			printf("O won\n");
		} else if(result == 'X') {
			printf("X won\n");
		} else if(result == 'N') {
			printf("Game has not completed\n");
		} else {
			printf("Draw\n");
		}

		getline(cin, s);
	}

    return 0;
}

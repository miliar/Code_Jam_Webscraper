#include <iostream>
#include <fstream>
#include <map>
#include <set>
#include <queue>
#include <utility>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

#define REP(i,n) for (int i = 0; i < n; i++)
#define REPP(i,m,n) for (int i = m; i < m+n; i++)
#define REPR(i,a,b) for (int i = a; i <= b; i++)

#define foreach(it,type) for (typeof(type.begin()) it = type.begin(); it != type.end(); it++)

#define MAX(n,m) (((n) > (m)) ? (n) : (m))
#define MIN(n,m) (((n) < (m)) ? (n) : (m))

typedef vector<int> vi;

vector<string> sol;
map<vector<string>, bool> hist;
int R,C;

bool solve(vector<string> & board, int left) {
	if (hist.find(board) != hist.end()) {
		return hist[board];
	}

	if (left == 0) {
		sol = board;
		return true;
	}

	int r = -1;
	int c = -1;
	REP(i,R){
		REP(j,C) {
			if (board[i][j] == '#') {
				r=i; c=j; break;
			}
		}
		if (r != -1) break;
	}
	
	for(int dr = -1; dr <= 1; dr+=2) {
		for(int dc = -1; dc <= 1; dc+=2) {
			
			bool all = true;
			for(int sr = 0; sr <= 1; sr++) {
				for(int sc = 0; sc <= 1; sc++) {
					int nr = r + dr * sr;			
					int nc = c + dc * sc;
					if (0 <= nr && 0 <= nc && nr < R && nc < C) {
					  all = all && board[nr][nc] == '#';
					} else {
						all = false;
					}
				}
			}

				if (all) {
					vector<string> nboard = board;
					int pr = r;
					int pc = c;
					if (dr == -1) pr--;
					if (dc == -1) pc--;

					nboard[pr][pc] = '/';
					nboard[pr+1][pc] = '\\';
					nboard[pr][pc+1] = '\\';
					nboard[pr+1][pc+1] = '/';

					if (solve(nboard, left-4)) {
						return true;
					}
				}
				
			}
		}

	hist[board] = false;
	return false;
}

int main(int argc, char* argv[]) {
  ifstream fin (argv[1]);

  int T;
  fin >> T;

	REP(t,T) {
		hist.clear();

		fin >> R >> C;
		vector<string> board(R);
		REP(i,R) {
			string row;
			fin >> row;
			board[i] = row;
		}

		int count = 0;
		REP(i,R) REP(j,C) {
			if (board[i][j] == '#') count++;
		}

		cout << "Case #" << t+1 << ":" << endl;
		if (count % 4 == 0 && solve(board, count)) {
			REP(r,R) {
				cout << sol[r] << endl;
			}
		} else {
			cout << "Impossible" << endl;
		}
	}

  return 0;
}


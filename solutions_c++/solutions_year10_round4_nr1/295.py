#include <fstream>
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

using namespace std;

#define VI vector<int> 
#define VS vector<string> 
#define LL long long 
#define FOR(i,n,m) for(int i=n;i<=m;i++)
#define REP(i,n) for(int i = 0; i < n; i++)
#define REPD(i,n) for(int i = n - 1; i>=0; i--)
#define BE(a) a.begin(), a.end()
#define PB push_back
#define MP make_pair
#define SI(a) sizeof(a)
#define FE(i, x) for (typeof((x).begin()) i = (x).begin(); i != (x).end(); i++)
#define FOR_SET(it, type, ss) for (set<type>::iterator it = ss.begin(); it!= ss.end(); it++)

const int INFI = 2000000000;
const int goX[4] = {-1, 0, 1, 0};
const int goY[4] = {0, 1, 0, -1};

const string PROBLEM_NAME = "A-large";
const string INPUT_FILE = PROBLEM_NAME + ".in";
const string OUTPUT_FILE = PROBLEM_NAME + ".out";

ofstream fout (OUTPUT_FILE.c_str());
ifstream fin (INPUT_FILE.c_str());

void read_input(){
	freopen (INPUT_FILE.c_str(),"r",stdin);
	//freopen ("","w",stdout);
	freopen (OUTPUT_FILE.c_str(),"w",stdout);
}
typedef int arr1[200][200];

int n, T, m;
arr1 a, b;

//bool check(int nn, arr1 c){
//	FOR(i, 1, nn) FOR(j, 1, nn){
//		if (c[i][j] != c[n - 1 - i][j] return false;
//		if (c[i][j] != c[i][n - 1 -j] return false;
//		if (c[i][j] != c[n - 1 -j][n - 1 - i] return false;
//	}
//	return true;
//}

bool DFS(int x, int y, int value){
	if (b[x][y] != -1) return b[x][y] == value;
	if (b[x][y] == -1) b[x][y] = value;
	if (!DFS(y, x, value)) return false;
	if (!DFS(m - 1 - x, m - 1 - y, value)) return false;
	if (!DFS(m - 1 - y, m - 1 - x, value)) return false;

	return true;
}

int solve(int step){
	FOR(k, n, 4 * n){
		m = k;		
		bool ok = true;
		FOR(i, 0, m - n) FOR(j, 0, m - n){

			ok = true;
			REP(i, m) REP(j, m) b[i][j] = -1;
			if (m == 5 && i == 1 && j == 0)
					cout << "";

			REP(ii, n){
				REP(jj, n) if (b[i + ii][j + jj] == -1){
					if (m == 5 && i == 5 && j == 0 && ii == 0 && jj == 2)
						cout << "";
					ok &= DFS(i + ii, j + jj, a[ii][jj]);
					if (!ok) {
						if (m == 5 && i == 1 && j == 0)
							cout << ii << " " << jj << endl;
						break;
					}

				} else if (a[ii][jj] != b[i + ii][j + jj]){
					ok = false; 
					break;
				}
				if (!ok) break;
			}
			if (ok) return m * m - n * n;
		}
	}
}

void m_main(){
	cin >> T;
	REP(step, T){
		cin >> n;
		int t = 1;
		FOR(i, 1, n){
			t ++;
			FOR(j, 1, i){
				int x = i - j + 1;
				cin >> a[x][t - x];
			}
		}
		for (int i = n - 1; i >= 1; i--){
			t ++;
			FOR(j, 1, i){				
				int x = n - j + 1;
				cin >> a[x][t - x];
			}
		}
		REP(i, n) REP(j, n) a[i][j] = a[i + 1][j + 1];
		cout << "Case #" << step + 1 << ": " << solve(step) << endl;
	}
}

int main(){
	read_input();
	m_main();

	return 0;
}
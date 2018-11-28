#include<algorithm>
#include<bitset>
#include<iostream>
#include<string>
#include<cstdio>
#include<sstream>
#include<vector>
#include<stack>
#include<deque>
#include<map>
#include<iterator>
#include<cmath>
#include<complex>
#include<queue>
#include<cassert>
#include<set>
#include<cstring>
#include<list>

#define FOREACH(it ,c ) for( typeof((c).begin()) it= (c).begin();it!=(c).end();++it) 
#define debug(x) cerr<< #x << " = " << x << "\n";
#define debugv(x) cerr<< #x << " = " ; FOREACH(it,(x)) cerr << *it << "," ; cerr<< "\n" ;
#define MP make_pair
#define PB push_back
#define siz(w) (int)w.size()
#define fup(i,st,ko) for(int i=st;i<=ko;i++)
#define fdo(i,st,ko) for(int i=st;i>=ko;i--)
#define REP(i,w) for(int i=0;i<siz(w);i++)
#define inf 500000000
using namespace std;

typedef long long ll;
#define maxn 8009

int M[maxn];
int drzewo[maxn][12];
int koszt[maxn];
int N;
int teams;

void solve(int pos) {
	//cout << pos << " " << koszt[pos] << endl;
	if(pos >= teams / 2) {
		int t1 = pos - teams / 2;
		int ile1 = M[teams - t1 * 2 - 1];
		int ile2 = M[teams - t1 * 2 + 1 - 1];
		
		//cout << "ile" << ile1 << " " << ile2 << endl;
		if(ile1 > 0 && ile2 > 0) {
			drzewo[pos][min(ile1, ile2) - 1] = 0;
		}
		drzewo[pos][min(ile1, ile2)] = koszt[pos];
		//cout << " " << pos << " " << min(ile1, ile2)<<"fdsf"  << endl;
	}
	else {
		fup(i, 0, 10) fup(j, 0, 10) {
			if(drzewo[pos * 2][i] < inf && drzewo[pos * 2 + 1][j] < inf) {
		//		cout << pos << " " << i << " " << j << "fdsf" << drzewo[pos * 2][i] << " " << drzewo[pos * 2 + 1][j] << endl;
				if(min(i, j) > 0) {
					drzewo[pos][min(i, j) - 1] = min(drzewo[pos][min(i, j) - 1], drzewo[pos * 2][i] + drzewo[pos * 2 + 1][j]);
				}
				drzewo[pos][min(i, j)] = min(drzewo[pos][min(i, j)], drzewo[pos * 2][i] + drzewo[pos * 2 + 1][j] + koszt[pos]);
			}
		}
	}
}

int main(){

	int cas;
	cin >> cas;
	fup(test, 1, cas) {
		memset(drzewo, 32, sizeof(drzewo));
		memset(koszt, 0, sizeof(koszt));
		memset(M, 0, sizeof(M));
		cin >> N;
		teams = 1;
		fup(j, 1, N) teams *= 2;
		fup(j, 0, teams - 1) cin >> M[j + 1];
		int tmp = teams;
		vector<int> vec;
		fup(j, 0, N - 1) {
			tmp /= 2;
			fup(k, 1, tmp) {
				int x; cin >> x;
				vec.push_back(x);
			}
		}
		reverse(vec.begin(), vec.end());
		fup(j, 0, siz(vec) - 1) koszt[j + 1] = vec[j];
		fdo(j, siz(vec) - 1, 0) {
			solve(j + 1);
		}
		int minw = inf;
		fup(i, 0, 10) minw = min(minw, drzewo[1][i]);
		cout << "Case #" << test << ": " << minw << endl;
	}

return 0;
}

#include <iostream>
#include <string>
#include <vector>

#define FOR(i,a,b) for(int i=(a); i<(b); i++)

using namespace std;

bool fun(vector<int>& a, vector<int> &b) {
	FOR(i,0,a.size()) {
		if(a[i] == b[i]) return false;
	}
	FOR(i,1,a.size()) {
		if((a[i] > b[i]) != (a[i-1] > b[i-1])) return false;
	}
	return true;
}

#include <set>
#include <list>


int licz(vector<vector<int> >& mmm, int beg, int& best, vector<int>& col, int cur) {
	if(beg == mmm.size()) return cur;
	if(cur >= best) return cur;

	int curbest = best;
	FOR(i,0,cur+1) {
		bool ok = true;
		FOR(j,0,mmm[beg].size()) {
			if(col[mmm[beg][j]] == i) {
				ok = false;
				break;
			}
		}
		if(!ok) continue;
		col[beg] = i;
		int c = licz(mmm, beg+1, best, col, max(cur, i+1));
		col[beg] = -1;
		if(c < best) best = c;
		//if(c < curbest) curbest = c;
	}
	return best;//curbest + 1;
}

int main() {
	int T, k, n;
	cin >> T;
	FOR(q,1,T+1) {
		cin >> n >> k;
		vector< vector<int> > v(n);
		FOR(i,0,n) {
			v[i].resize(k);
			FOR(j,0,k) cin >> v[i][j];
		}

		vector<vector<int> > mmm(n);
		vector<int> col(n, -1);
		FOR(i,0,n) FOR(j,0,n) if(j != i && !fun(v[i], v[j])) {
			mmm[i].push_back(j);
		}
		int ret = licz(mmm, 0, n, col, 0);

/*		int ret = 0;
		vector< vector<int> > ch(1);
		ch[0].push_back(0);
		FOR(i,1,n) {
			FOR(j,0,ch.size()) {
				bool ok = true;
				FOR(k,0,ch[j].size()) {
					if( !fun(v[i], v[ch[j][k]]) ) {
						ok = false;
						break;
					}
				}
				if(ok) {
					ch[j].push_back(i);
					break;
				}
				if(ch.size() == j+1) {
					ch.resize(ch.size()+1);
					ch[ch.size()-1].push_back(i);
					break;
				}
			}
		}*/



		cout << "Case #" << q << ": " << ret << endl;
	}
	return 0;
}
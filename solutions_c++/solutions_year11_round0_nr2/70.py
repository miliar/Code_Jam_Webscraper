#include <iostream>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <algorithm>
#include <vector>
#include <string>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <sstream>
using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int,int> pii;
#define sz(A) (int)(A).size()
#define FOR(A,B) for(int A=0; A < (int) (B);A++)
#define pb push_back
#define all(x) x.begin() , x.end()

vector<string> combina;
vector<string> deleta;
string s;

int faz_combinacao(string & ans) {
	if(sz(ans) <= 1) return 0;
	int n = sz(ans);
	FOR(i, sz(combina)) {
		if( (ans[n-1] == combina[i][0] && ans[n-2] == combina[i][1] ) || ( ans[n-1] == combina[i][1] && ans[n-2] == combina[i][0]) ) {
			ans.erase(sz(ans) - 2);
			ans += combina[i][2];
			return 1;
		}
	}
	return 0;
}
int faz_remocao(string & ans) {
	if(sz(ans) <= 1) return 0;
	int n = sz(ans);
	FOR(i, sz(deleta)) {
		if(ans[n-1] == deleta[i][0] || ans[n-1] == deleta[i][1]) {
			FOR(j, sz(ans) - 1) {
				if(ans[n-1] == deleta[i][0] && ans[j] == deleta[i][1]) {
					ans = "";
					return 1;
				}
				if(ans[n-1] == deleta[i][1] && ans[j] == deleta[i][0]) {
					ans = "";
					return 1;
				}
			}
		}
	}
	return 0;
}



void solve() {
	string ans;
	FOR(i, sz(s)) {
		ans += s[i];
		while(1) {
			if(faz_combinacao(ans)) continue;
			if(faz_remocao(ans)) continue;
			break;
		}
	}
	cout << "[";
	FOR(i, sz(ans)) {
		if(i) cout << ", ";
		cout << ans[i];
	}
	cout << "]\n";
}

int main() {

	int TESTES; scanf("%d", &TESTES);
	for(int TESTE = 1; TESTE <= TESTES; TESTE++) {
		printf("Case #%d: ", TESTE);

		int C,D;
		combina.clear();
		cin >> C;
		FOR(i,C) {
			string aux;
			cin >> aux;
			combina.push_back(aux);
		}

		cin >> D;
		deleta.clear();
		FOR(i,D) {
			string aux;
			cin >> aux;
			deleta.push_back(aux);
		}
		cin >> C;
		cin >> s;

		solve();
	}
    return 0;
}


#include <iostream>
#include <algorithm>
#include <map>
#include <sstream>
#include <vector>
#include <string>
using namespace std;

typedef long long ll;
typedef pair<int,int> ii;
#define sz(x) (int)(x).size()
#define pb push_back
#define clr(x) (x).clear()
#define all(x) (x).begin(), (x).end()

int tn, cc;
int K;
string s;
string t;
int ret;
void input() {
	cin >> K;
	cin >> s;
	t = s;
}

void solve() {
	vector<int> P(K);
	int i,j;
	ret = 987654321;
	for(i=0;i<K;++i) P[i] = i;
	do {
		t = s;
		for(i=0;i<sz(s);i+=K) {
			for(j=0;j<K;++j) {
				t[i+j] = s[i+P[j]];
			}
		}
		t.erase(unique(all(t)),t.end());
		// cerr << t << " " << sz(t) <<  endl;
		ret <?= sz(t);
	} while(next_permutation(all(P)));	
}

void output() {
	printf("Case #%d: %d\n", cc,ret);
}

int main() {
	cin >> tn;
	for(cc=1;cc<=tn;++cc) {
		input();
		solve();
		output();
	}
}


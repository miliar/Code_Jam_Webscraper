#include <iostream>
#include <string>
#include <numeric>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <map>
#include <set>

using namespace std;

#define pb push_back
#define sz(a) int((a).size())
#define rep(i, n) for(int i = 0; i < n; i++)
#define foreach(it, m) for(__typeof((m).begin()) it = (m).begin(); it != (m).end(); it++)

int L, D, N;
string st[5000];
vector<char> v[500];

int main() {
	
	scanf("%d %d %d", &L, &D, &N);

	char buff[1000];

	rep(i, D) scanf("%s", buff), st[i] = string(buff);

	rep(c, N) 
	{
		rep(i, L) v[i].clear();

		scanf("%s", buff);
		string s(buff);

		int p = 0, k = 0;
		while(p < sz(s)) {
			if(s[p] == '(') {
				p++;
				while(s[p] != ')') v[k].pb(s[p]), p++;
				p++;;
			}
			else v[k].pb(s[p]), p++;
			k++;
		}

		int ret = 0;

		rep(i, D) { 
			bool ok1 = false;
			rep(j, N) {
				bool ok2 = true;
				rep(m, L) {
					bool ok3 = false;
					rep(n, sz(v[m])) if(st[i][m] == v[m][n]) ok3 = true;
					if(ok3 == false) ok2 = false;
				}
				if(ok2 == true) ok1 = true;
			}
			ret += ok1;
		}

		printf("Case #%d: %d\n", c + 1, ret);
	}

	return 0;
}

#include <iostream>
#include <cmath>
#include <ctime>
#include <cassert>
#include <algorithm>
#include <set>
#include <map>
#include <queue>
#include <string>
#include <vector>
#include <stack>

#define forn(i, n) for(int i = 0; i < int(n); i++)
#define X first
#define Y second
#define sz(a) (int)a.size()

using namespace std;

typedef long long li;
typedef long double ld;
typedef pair<int, int> pt;
string w[300], a[300];
set<int> b[30];
bool us[30];
int main(){
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	int tests;
	cin >> tests;
	forn(test, tests){
		int n, m;
		cin >> n >> m;
		forn(i, 30)
			b[i].clear();
		
		forn(i, n){
			cin >> w[i];
			forn(j, sz(w[i]))
				b[w[i][j] - 'a'].insert(i);
		}
		forn(j, m)
			cin >> a[j];
		vector<string> res;
		forn(i, m){
			int mx = 0;
			string ans = w[0];
			forn(j, n){
				memset(us, false, sizeof us);
				int uk = 0;
				string mask = "";
				forn(k, sz(w[j]))
					mask += "*";
				vector<int> good;
				forn(k, n)
					if(sz(w[j]) == sz(w[k]))
						good.push_back(k);
				int cur = 0;
				while(sz(good) > 1){
					bool was = false;
					forn(k, sz(good))
						if(b[a[i][uk] - 'a'].count(good[k]))
							was = true;
					us[a[i][uk] - 'a'] = true;
					if(!was){
						uk++;
						
						continue;
					}
					forn(k, sz(w[j]))
						if(a[i][uk] == w[j][k])
							mask[k] = a[i][uk];
					if(!b[a[i][uk] - 'a'].count(j))
						cur++;
					vector<int> ngood;
					forn(k, sz(good)){
						int cnt = 0;
						forn(k1, sz(w[good[k]]))
						if((mask[k1] != '*' && w[good[k]][k1] == mask[k1]) ||(mask[k1] == '*' && !us[w[good[k]][k1] - 'a'])){
							cnt++;
						}
						if(cnt == sz(w[j]))
							ngood.push_back(good[k]);
					}
					good = ngood;
					uk++;

				}
				if(cur > mx){
					mx = cur;
					ans = w[j];
				}
			}
			res.push_back(ans);

		}
		printf("Case #%d:", test + 1);
		forn(i, sz(res))
			cout << " " << res[i];
		cout << endl;

	}
	return 0;
}
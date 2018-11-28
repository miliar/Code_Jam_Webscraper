#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#define beg 10000000
#define pb push_back
#define mp make_pair
#define sz size()
#define iss istringstream
#define oss ostringstream
#define pf pop_front()
#define nd second
#define st first
#define fr(i, n) for(int i = 0; i < (int)n; i++)
#define LL long long
#define vi vector<int>
#define pii pair<int, int>
#define vs vector<string>

using namespace std;

int seka[1004];

int main() {
	freopen("in.in", "r", stdin);
	freopen("out.out", "w", stdout);
	int test;
	cin >> test;
	for(int tt = 1; tt <= test; tt++) {
		map<string, int> v;
		string temp;
		int s;
		cin >> s;
		getline(cin, temp);
		for(int i = 1; i <= s; i++) {
			getline(cin, temp);
			v.insert(mp(temp, i - 1));
		}
		int q;
		cin >> q;
		getline(cin, temp);
		for(int i = 1; i <= q; i++) {
			getline(cin, temp);
			seka[i - 1] = v[temp];
		}
		vi L;
		fr(i, s) L.pb(1);
		int kiek = s;
		int ans = 0;
		fr(i, q) {
			if(L[seka[i]] == 1) {
				kiek--;
				if(!kiek) {
					fr(j, s) L[j] = 1;
					ans++;
					kiek = s - 1;
				}
				L[seka[i]] = 0;
			}
		}
		cout << "Case #" << tt << ": " << ans << endl;
	}
	return 0;
}

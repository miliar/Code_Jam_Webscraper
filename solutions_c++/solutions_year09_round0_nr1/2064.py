#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <cstring>
#include <fstream>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <numeric>
#define beg 10000000
#define pb push_back
#define mp make_pair
#define sz(x) (int)x.size()
#define ss stringstream
#define pf pop_front()
#define nd second
#define st first
#define fr(i, n) for(int i = 0; i < (int)n; i++)
#define LL long long
#define vi vector<int>
#define pii pair<int, int>
#define vii vector<pii >
#define vs vector<string>
#define LD long double

using namespace std;

//always reset global variables!

int main() {
	int L, D, N;
	cin >> L >> D >> N;
	vs dict;
	fr(i, D) {
		string s;
		cin >> s;
		dict.pb(s);
	}
	fr(i, N) {
		string s;
		cin >> s;
		int pos = 0;
		vi c[20];
		fr(j, L) {
			if(s[pos] == '(') {
				pos++;
				while(s[pos] != ')') {
					c[j].pb(s[pos]);
					pos++;
				}
			}
			else c[j].pb(s[pos]);
			pos++;
		}
		fr(j, L) sort(c[j].begin(), c[j].end());
		int ans = 0;
		fr(j, D) {
			bool ok = true;
			fr(k, L) if(!binary_search(c[k].begin(), c[k].end(), dict[j][k])) ok = false;
			ans += ok;
		}
		cout << "Case #" << i + 1 << ": " << ans << endl;
	}
	return 0;
}

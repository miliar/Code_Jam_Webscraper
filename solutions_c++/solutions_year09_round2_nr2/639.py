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

void solveCase(int Case) {
	cout << "Case #" <<  Case + 1 << ": ";
	string s;
	cin >> s;
	deque<char> v;
//	cout << "S = " << s << endl;
	for(int i = sz(s) - 1; i >= 0; i--) {
		v.push_front(s[i]);
//		fr(j, sz(v)) cout << v[j];
//		cout << endl;
		if(sz(v) > 1 && v[0] < v[1]) {
//			cout << "Here" << endl;
			next_permutation(v.begin(), v.end());
			cout << s.substr(0, i);
			string t = "";
			fr(j, sz(v)) t += v[j];
			cout << t << endl;
			return;
		}
//		fr(j, sz(v)) cout << v[j];
//		cout << endl;
	}
	sort(v.begin(), v.end());
	fr(i, sz(v)) if(v[i] != '0') {
		cout << v[i];
		v.erase(v.begin() + i);
		break;
	}
	cout << "0";
	string t = "";
	fr(j, sz(v)) t += v[j];
	cout << t << endl;
}

int main() {
	int T;
	cin >> T;
	fr(i, T) solveCase(i);
	return 0;
}

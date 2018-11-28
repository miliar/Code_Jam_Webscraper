//C.cpp
//_are89
#include <functional>
#include <algorithm>
#include <iostream>
#include <numeric>
#include <utility>
#include <sstream>
#include <iomanip>
#include <cstring>
#include <cstdlib>
#include <vector>
#include <cstdio>
#include <bitset>
#include <cmath>
#include <ctime>
#include <queue>
#include <deque>
#include <stack>
#include <list>
#include <map>
#include <set>

using namespace std;

#define sz(a) int((a).size())
#define pb push_back
#define mp make_pair
#define all(c) (c).begin(),(c).end()
#define tr(c,i) for(typeof((c).begin()) i=(c).begin(); i!=(c).end();i++)
#define present(c,x)  ( (c).find(x) !=(c).end())
#define cpresent(c,x) (find(all(c),x)!= (c).end() )
#define minEI(x)  min_element(x.begin(),x.end())-(x).begin()
#define maxEI(x)  max_element(x.begin(),x.end())-(x).begin()

#define UNS(v)     sort((v).begin(),(v).end()),v.erase(unique(v.begin(),v.end()),v.end())
#define acuSum(x)  accumulate(x.begin(),x.end(),0)
#define acuMul(x)  accumulate(x.begin(),x.end(),1, multiplies<int>()); 
#define bits(x)     __builtin_popcount( x )

template<class F, class T> T convert(F input, int width = 0, int prec = -1) {
	stringstream A;
	T res;
	if (prec > -1)
		A << fixed << setprecision(prec);
	A << setw(width) << setfill('0') << input;
	A >> res;
	return res;
}

vector<string> split(string s) {
	stringstream A(s);
	vector<string> res;
	string t;
	while (A >> t)
		res.push_back(t);
	return res;
}
int sum(vector<int> v, int i, int j) {
	int sm = 0;
	for (int k = i; k < j; k++) {
		sm += v[k];
	}
	return sm;
}
int EOR(vector<int> v, int i, int j) {
	int n = v[i];
	for (int k = i + 1; k < j; k++)
		n = n ^ v[k];
	return n;
}
void pv(vector<int> v) {
	cout << "[ ";
	for (int i = 0; i < sz(v); i++)
		cout << v[i] << " ";
	cout << " ]" << endl;
}
int main() {
#ifndef ONLINE_JUDGE
	freopen("C-large.in", "rt", stdin);
	freopen("C-largeO.txt", "wt", stdout);
#endif
	int t;
	cin >> t;
	for (int i = 1; i <= t; i++) {
		int num;
		cin >> num;
		vector<int> v;
		for (int x = 0; x < num; x++) {
			int nm;
			cin >> nm;
			v.pb(nm);
		}
		sort(v.begin(), v.end());
		//pv(v);
		if (EOR(v, 0, sz(v)) != 0) {
			cout << "Case #" << i << ": " << "NO" << endl;

		} else {
			int mx = -1;
			for (int y = 1; y < sz(v); y++) {
				if (EOR(v, 0, y) == EOR(v, y, sz(v))) {
					mx = max(mx, max(sum(v, 0, y), sum(v, y, sz(v))));
				}

			}
			cout << "Case #" << i << ": " << mx << endl;
		}
	}
	return 0;
}


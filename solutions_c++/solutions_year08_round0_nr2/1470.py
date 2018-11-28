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

int tim[4000];

int main() {
	freopen("in.in", "r", stdin);
	freopen("out.out", "w", stdout);
	int tests;
	cin >> tests;
	for(int test = 1; test <= tests; test++) {
		int T;
		vi timsA, timsB, avA, avB;
		cin >> T;
		int nA, nB;
		cin >> nA >> nB;
		string temp;
		getline(cin, temp);
		fr(i, nA) {
			getline(cin, temp);
			fr(j, temp.sz) if(temp[j] == ':') temp[j] = ' ';
			int arr, dep;
			iss sin(temp);
			sin >> arr >> dep;
			timsA.pb(60*arr + dep);
			sin >> arr >> dep;
			avB.pb(60*arr + dep + T);
		}
		fr(i, nB) {
			getline(cin, temp);
			fr(j, temp.sz) if(temp[j] == ':') temp[j] = ' ';
			iss sin(temp);
			int arr, dep;
			sin >> arr >> dep;
			timsB.pb(60*arr + dep);
			sin >> arr >> dep;
			avA.pb(60*arr + dep + T);
		}
		sort(timsA.begin(), timsA.end());
		sort(timsB.begin(), timsB.end());
		sort(avA.begin(), avA.end());
		sort(avB.begin(), avB.end());
	//	cout << "cia1" << endl;
		memset(tim, 0, sizeof(tim));
	//	cout << "cia" << endl;
		fr(i, timsA.sz) tim[timsA[i]]--;
		fr(i, avA.sz) tim[avA[i]]++;
		int ansA = 0;
		int sum = 0;
		for(int t = 0; t < 3600; t++) {
			sum += tim[t];
			if(sum < 0) {
				ansA -= sum;
				sum = 0;
			}
		}
	//	cout << "cia" << endl;
		memset(tim, 0, sizeof(tim));
		fr(i, timsB.sz) tim[timsB[i]]--;
		fr(i, avB.sz) tim[avB[i]]++;
		int ansB = 0;
		sum = 0;
		for(int t = 0; t < 3600; t++) {
			sum += tim[t];
			if(sum < 0) {
				ansB -= sum;
				sum = 0;
			}
		}
		cout << "Case #" << test << ": " << ansA << ' ' << ansB << endl;
	}
	return 0;
}

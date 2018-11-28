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
	cout << "Case #" << Case + 1<< ": ";
	int n;
	cin >> n;
	vs M;
	fr(i, n) {
		string t;
		cin >> t;
		M.pb(t);
	}
	vi high;
	fr(i, n) {
		int kur = 0;
		fr(j, n) if(M[i][j] == '1') kur = j;
		high.pb(kur);
	}
	int kiek = 0;
	fr(i, n) {
		fr(j, sz(M)) if(high[j] <= i) {
			kiek += j;
			M.erase(M.begin() + j);
			high.erase(high.begin() + j);
			break;
		}
	}
	cout << kiek << endl;
}

int main() {
	int tests;
	cin >> tests;
	fr(i, tests) solveCase(i);
	return 0;
}

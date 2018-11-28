#include <iostream>
#include <stdio.h>
#include <cmath>
#include <string>
#include <vector>
#include <algorithm>
#include <queue>
#include <sstream>
#include <set>
#include <map>
#include <utility>

using namespace std;

#define forn(i, n) for(int i = 0; i < (int) n; ++i)
#define fore(i, a, b) for(int i = (int) (a); i < (int) (b); ++i)

#define ll long long
#define ld long double

#define PII pair <int, int>

#define x first
#define y second

const ld EPS = 1e-9;
const int MAXN = 1000;

char tmp[MAXN];
string s;
int main(){
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);

	int tk;
	cin >> tk;

	forn(ii, tk){
		scanf("%s", &tmp);
		s = tmp;
		s = "0" + s;
		next_permutation(s.begin(), s.end());
		if (s.size() > 1 && s[0] == '0'){
			s.erase(0, 1);
		}
		printf("Case #%d: %s\n", ii + 1, s.c_str());
	}

	return 0;
}
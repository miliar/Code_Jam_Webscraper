#include <iostream>
#include <cstdio>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <string>
#include <sstream>
#include <algorithm>
#include <stack>

#define INF 1000000000
#define EPS 1E-8
#define PI 3.14159265358979

using namespace std;

string word[5010];

vector<set<char> > cut(string a) {
	vector<set<char> > res;
	for(int i = 0; i < a.size(); ++i) {
		if(a[i] == '(') {
			set<char> add;
			for(++i; a[i] != ')'; ++i) add.insert(a[i]);
			res.push_back(add);
		}else {
			set<char> add;
			add.insert(a[i]);
			res.push_back(add);
		}
	}
	return res;
}

int main() {
	int L, D, N;
	cin >> L >> D >> N;
	for(int i = 0; i < D; ++i) cin >> word[i];
	for(int t = 0; t < N; ++t) {
		string test;
		cin >> test;
		vector<set<char> > cutted = cut(test);
		int res = 0;
		for(int i = 0; i < D; ++i) {
			if(cutted.size() != word[i].size()) continue;
			bool ok = true;
			for(int j = 0; j < word[i].size(); ++j) {
				ok = ok && cutted[j].find(word[i][j]) != cutted[j].end();
			}
			if(ok) ++res;
		}
		printf("Case #%d: %d\n", t + 1, res);
	}
	return 0;
}

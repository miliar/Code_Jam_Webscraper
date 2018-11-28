#include <cstdio>
#include <map>
#include <set>
#include <iostream>
#include <vector>
using namespace std;

void solve() {
	int C;
	cin>>C;
	map<  pair<char, char>, char > nonbase;
	for (int i = 0; i < C; i++) {
		string s;
		cin>>s;
		nonbase[make_pair(s[0],s[1])] = s[2];
		nonbase[make_pair(s[1], s[0])] = s[2];
	}
	int D;
	cin>>D;
	set< pair<char, char> > opposed;
	for (int i = 0; i < D; i++) {
		string s;
		cin>>s;
		opposed.insert(make_pair(s[0], s[1]));
		opposed.insert(make_pair(s[1], s[0]));
	}
	int N;
	cin>>N;
	string s;
	cin>>s;
	vector<char> res;
	for (int i = 0; i < N; i++) {
		if (res.size() > 0) {
			bool clear = false;
			for (int j = 0; j < res.size(); j++) {
				if (opposed.count(make_pair(res[j], s[i]))) {
					clear = true;
					break;
				}
			}
			if (nonbase.count(make_pair(s[i], res.back()))) {
				char c = res.back();
				res.pop_back();
				res.push_back(nonbase[make_pair(s[i], c)]);
			} else if (clear) {
				res.clear();
			} else if (!opposed.count(make_pair(s[i], res.back()))) {
				res.push_back(s[i]);
			}
		} else {
			res.push_back(s[i]);
		}
	}
	printf("[");
	for (int i = 0; i < res.size(); i++) {
		if (i == res.size() - 1) {
			printf("%c", res[i]);
		} else {
			printf("%c, ", res[i]);
		}
	}
	printf("]\n");

}

int main(void) {
	int n;
	cin>>n;
	for (int t=1; t<= n; t++) {
		printf("Case #%d: ", t);
		solve();
	}
	
	return 0;
}

#include <iostream>
#include <string>
#include <set>
#include <cstdio>
using namespace std;

int main(){
	string s;
	int t;
	cin >> t;
	for(int testcase = 1; testcase <= t; ++testcase){
		set<string> S;
		int n, m, r;
		cin >> n >> m;
		while(n--){
			cin >> s;
			s += '/';
			for(int i = 1; ;){
				i = s.find('/', i + 1);
				if(i < 0) break;
				S.insert(s.substr(0, i));
			}
		}
		r = - S.size();
		while(m--){
			cin >> s;
			s += '/';
			for(int i = 1; ;){
				i = s.find('/', i + 1);
				if(i < 0) break;
				S.insert(s.substr(0, i));
			}
		}
		r += S.size();
		printf("Case #%d: %d\n", testcase, r);
	}
}

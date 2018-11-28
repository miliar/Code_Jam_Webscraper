#include <cstdio>
#include <iostream>
#include <set>
#include <map>
using namespace std;

int T, N, C, D;
map<pair<char, char>, char> comb;
set<pair<char, char> > opp;

int main() {
	cin>>T;
	for(int z = 1; z <= T; z++) {
		opp.clear();
		comb.clear();
		cin >> C;
		for(int i = 0; i < C; i++) {
			char str[4];
			scanf("%s", str);
			comb[make_pair(str[0], str[1])] = str[2];
			comb[make_pair(str[1], str[0])] = str[2];
		}
		cin >> D;
		for(int i = 0; i < D; i++) {
			char str[4];
			scanf("%s", str);
			opp.insert(make_pair(str[0], str[1]));
			opp.insert(make_pair(str[1], str[0]));
		}
		char str[105];
		cin >> N;
		string ans = "";
		scanf("%s", str);
		ans += str[0];
		for(int i = 1; i < N; i++) {
			if(ans.empty()) {
				ans += str[i];
				continue;
			}
			map<pair<char, char>, char> :: iterator it;
			it = comb.find(make_pair(str[i], *(ans.end()-1)));
			if(it == comb.end()) {
				int j;
				for(j = 0; j < ans.length(); j++)
					if(opp.find(make_pair(str[i], ans[j])) != opp.end()) {
						ans = "";
				//		cout << "destroyed at " << i << endl;
						break;
					}
				if(!ans.empty())
					ans += str[i];
			}
			else {
				ans[ans.length()-1] = it->second;
			}
		}
		cout << "Case #" << z << ": [";
		if(!ans.empty()) {
			for(int i = 0; i < ans.length()-1; i++)
				cout << ans[i] << ", ";
			cout << ans[ans.length()-1];
		}
		cout << "]\n";
	}

	return 0;
}

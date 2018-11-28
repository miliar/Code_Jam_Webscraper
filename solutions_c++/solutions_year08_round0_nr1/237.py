#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <cassert>
using namespace std;

int main() {
	int N; cin>>N;
	for (int t = 1; t <= N; t++) {
		int ans = 0;
		int S; cin>>S;
		map<string,int> dic;
		cin.ignore();
		for (int i = 0; i < S; i++) {
			string engine;
			getline(cin, engine);
			dic[engine] = i;
		}
		vector<bool> used(S);
		int cnt = 0;
		int Q; cin>>Q;
		cin.ignore();
		for (int i = 0; i < Q; i++) {
			string query;
			getline(cin,query);
			assert(dic.count(query));
			int id = dic[query];
			if (!used[id]) {
				used[id] = true;
				cnt++;
				if (cnt == S) {
					ans++;
					used.clear();
					used.resize(S,false);
					used[id] = true;
					cnt = 1;
				}
			}
		}
		cout<<"Case #"<<t<<": "<<ans<<endl;
	}
	return 0;
}

#include <iostream>
#include <string>
#include <set>
#include <vector>
#include <algorithm>

using namespace std;

bool cmp1(string a, string b) {
	if(a.size()<b.size()) return true;
	if(b.size()<a.size()) return false;
	return a<b;
}

int main () {
	int N,M,T,caso = 1;
	cin >> T;
	while(caso <= T) {
		cin >> N >> M;
		int total = 0;
		vector<string> created;
		set<string> S;
		vector<string> paths;
		string s;
		for(int i = 0; i < N; i++) {
			cin >> s;
			s.push_back('/');
			created.push_back(s);
		}
		for(int i = 0; i < M; i++) {
			cin >> s;
			s.push_back('/');
			paths.push_back(s);
		}
		sort(created.begin(),created.end(),cmp1);
		sort(paths.begin(),paths.end(),cmp1);
		for(int i = 0; i < created.size(); i++) {
			for(int j = 1; j < created[i].size(); j++) {
				if(created[i][j] == '/') {
					S.insert(string(created[i].begin(),created[i].begin()+j));
				}
			}
		}
		for(int i = 0; i < paths.size(); i++) {
			for(int j = 1; j < paths[i].size(); j++) {
				if(paths[i][j] == '/') {
					if(S.find(string(paths[i].begin(),paths[i].begin()+j))==S.end()) {
						int cnt = 0;
						for(int z = j; z < paths[i].size(); z++) {
							if(paths[i][z] == '/' ) {
								S.insert(string(paths[i].begin(),paths[i].begin()+z));
//								cout << " adding " << string(paths[i].begin(),paths[i].begin()+z) << endl;
								cnt++;
							}
						}
						total+=cnt;
					}
				}
			}
		}

		cout << "Case #" << caso++ << ": " << total << endl;
	}
	return 0;
}


#include <iostream>
#include <cmath>
#include <cstring>
#include <string>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
using namespace std;

map<char, char> M[256];
set<char> bad[256];

int main(){
	freopen("B.in", "r", stdin);
	freopen("B.out", "w", stdout);
	int t;
	cin >> t;
	for (int I=0; I<t; I++){
		cout << "Case #" << I+1 << ": ";
		int n, d, len;
		string str, ans;
		ans.clear();
		for (int i=0; i<256; i++){
			bad[i].clear();
			M[i].clear();
		}
		cin >> n;
		for (int i=0; i<n; i++){
			string s1;
			cin >> s1;
			M[s1[0]][s1[1]] = s1[2];
			M[s1[1]][s1[0]] = s1[2];
		}
		cin >> d;
		for (int i=0; i<d; i++){
			string s1;
			cin >> s1;
			bad[s1[0]].insert(s1[1]);
			bad[s1[1]].insert(s1[0]);
		}
		cin >> len;
		cin >> str;
		for (int i=0; i<len; i++){
			char tec = str[i];
			while (!ans.empty() && M[tec].find(ans[ans.size()-1]) != M[tec].end()){
				tec = M[tec][ans[ans.size()-1]];
				ans = ans.substr(0, ans.size()-1);
			}
			bool too_bad = false;
			for (int j=0; j<ans.size(); j++){
				if (bad[tec].find(ans[j]) != bad[tec].end()){
					ans.clear();
					too_bad = true;
					break;
				}
			}
			if (!too_bad){
				ans += tec;
			}
		}
		cout << "[";
		for (int i=0; i<ans.size(); i++){
			cout << ans[i];
			if (i < ans.size() - 1){
				cout << ", ";
			}
		}
		cout << "]" << endl;
	}
	return 0;
}
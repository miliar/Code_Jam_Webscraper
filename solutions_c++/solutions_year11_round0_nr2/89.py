#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <cctype>
#include <cassert>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <list>
#include <map>
#include <set>
#include <algorithm>
#include <utility>

using namespace std;

int main () {
	int T, t = 1;
	
	cin >> T;
	while (T--) {
		char combine[128][128], opposed[128][128];
		int c, d, n;
		string s;
		
		memset(combine,0,sizeof(combine));
		memset(opposed,0,sizeof(opposed));
		
		cin >> c;
		
		for (int i=0; i < c; i++) {
			cin >> s;
			combine[s[0]][s[1]] = combine[s[1]][s[0]] = s[2];
		}
		
		cin >> d;
		
		for (int i=0; i < d; i++) {
			cin >> s;
			opposed[s[0]][s[1]] = opposed[s[1]][s[0]] = 1;
		}
		
		cin >> n >> s;
		
		string ans = "";
		int present[128];
		
		memset(present,0,sizeof(present));
		
		for (int i=0; i < n; i++) {
			
			if (ans.length() == 0) {
				ans += s[i];
				present[s[i]]++;
				continue;
			}
			
			if (combine[s[i]][ans[ans.length()-1]] != 0) {
				present[ans[ans.length()-1]]--;
				ans[ans.length()-1] = combine[s[i]][ans[ans.length()-1]];
				present[ans[ans.length()-1]]++;
				continue;
			}
			
			ans += s[i];
			present[s[i]]++;
			
			for (int j=0; j < 128; j++) {
				if (present[j] > 0 && opposed[j][s[i]]) {
					memset(present,0,sizeof(present));
					ans = "";
					break;
				}
			}
		}
		
		cout << "Case #" << t++ << ": [";
		for (int i=0; i < ans.length(); i++) {
			if (i) cout << ", ";
			cout << ans[i];
		}
		cout << "]" << endl;
	}
	
	return 0;
}

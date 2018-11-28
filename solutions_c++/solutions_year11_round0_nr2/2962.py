#include <iostream>
#include <vector>
#include <string>
#include <queue>
#include <set>
#include <map>
using namespace std;

inline pair<char,char> to_pair(char a,char b) {
	if (a>b) swap(a,b);
	return make_pair(a,b);
}

int main() {
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);
	int c,d,t,n,z;
	cin >> t;
	char s;
	for (int i=0;i<t;i++) {
		cin >> c;
		//vector <string> C;
		//C.resize(c);
		string s;
		map<pair<char,char>,char> C;
		for (int j=0;j<c;j++) {
			cin >> s;
			C[to_pair(s[0],s[1])] = s[2];
		}
		cin >> d;
		//vector <string> D;
		//D.resize(d);
		set <pair<char,char>> D;
		//map < char , set <char> > D; 
		for (int j=0;j<d;j++) {
			cin >> s;
			D.insert(to_pair(s[0],s[1]));
			//D[s[0]].insert(s[1]);
			//D[s[1]].insert(s[0]);
		}
		cin >> n;
		cin >> s;
		vector<char> ans;
		ans.reserve(666);
		set <char> was;
		for (int j=0;j<n;j++) {
			z = ans.size() - 1;
			if (z>=0) {
				map<pair<char,char>,char>::iterator it = C.find(to_pair(ans[z],s[j]));
				if (it!=C.end()) {
					ans[z]=it->second; 
					//continue;
				} else ans.push_back(s[j]);
			} else ans.push_back(s[j]);
			z = ans.size() - 1;
			if (z>=1) {
				//if (D.find(to_pair(ans[z],ans[0]))!=D.end()) ans.clear();
				for (int k=0;k<z;k++) {
					if (D.find(to_pair(ans[z],ans[k]))!=D.end()) {
						ans.clear();
						break;
					}
				}
			}
		}
		cout << "Case #" << i+1 << ": [";
		z = ans.size() - 1;
		for (int i=0;i<z;i++) cout << ans[i] << ", ";
		if (z>=0) cout << ans[z];
		cout << ']' << endl;
	}

}

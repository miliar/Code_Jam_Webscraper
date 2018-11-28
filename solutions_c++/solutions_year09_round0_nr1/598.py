#include <iostream>
#include <string>
#include <vector>
#include <set>
using namespace std;
int l, d, n;
vector<set<char> > split(const string &pattern){
	int pos = 0;
	vector<set<char> > ans;
	for (int i = 0; i < l; ++i){
		set<char> ret;
		if (pattern[pos] == '('){
			++pos;
			while (pattern[pos] != ')') ret.insert(pattern[pos++]);
			++pos;
		} else {
			ret.insert(pattern[pos++]);
		}
		ans.push_back(ret);
	}
	return ans;
}

int main(){
		scanf("%d%d%d", &l, &d, &n);
		vector<string> data;
		for (int i = 0; i < d; ++i){
			string str;
			cin >> str;
			data.push_back(str);
		}
		for (int i = 0; i < n; ++i){
			string pattern;
			cin >> pattern;
			int ans = 0;
			vector<set<char> > req = split(pattern);
			for (int j = 0; j < d; ++j){
				bool ok = true;
				for (int k = 0; k < l; ++k){
					if (req[k].find(data[j][k]) == req[k].end()){
						ok = false;
						break;
					}
				}
				if (ok) ++ans;
			}
			cout << "Case #" << i + 1 << ": " << ans << endl;
		}
	return 0;
}
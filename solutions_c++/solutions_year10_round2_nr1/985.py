#include <string>
#include <algorithm>
#include <iostream>
#include <map>

using namespace std;

int N,M;
map<string,int>hash;
int cnt,ans;

void deal(string s) {
	s += '/';
	string tmp = "/";
	for(int i = 1;i < s.size(); ++i) {
		if(s[i] == '/') {
			if(hash.find(tmp) == hash.end()) {
				hash[tmp] = cnt++;
			}
			tmp += '/';
		} else {
			tmp += s[i];
			continue;
		}
	} 
}

void deal2(string s) {
	s += '/';
	string tmp = "/";
	for(int i = 1;i < s.size();++i) {
		if(s[i] == '/') {
			if(hash.find(tmp) == hash.end()) {
				ans++;
				hash[tmp] = cnt++;
			}
			tmp += '/';
		} else {
			tmp += s[i];
			continue;
		}
	}
}

int main() {
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int T,cas = 1;
	cin >> T;
	while(T--) {
		hash.clear();
		cnt = ans = 0;
		cin >> N >> M;
		while(N--) {
			string str;
			cin >> str;
		//	cout << str << endl;
			deal(str);
		}
		while(M--) {
			string str;
			cin >> str;
			deal2(str);
		}
		cout << "Case #" << cas++ << ": " << ans << endl;
	}
	return 0;
}

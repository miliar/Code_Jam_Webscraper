#include <cstdio>
#include <cstring>
#include <string>
#include <sstream>
#include <map>
#include <vector>

using namespace std;

struct A {
	map <string, int> next;
};

int n, m, res;
A a;
vector <A> v;

void split(char* str, vector <string>& token) {
	for (int i = 0; str[i] != '\0'; i++) {
		if (str[i] == '/') {
			str[i] = ' ';
		}
	}
	istringstream ist(str);
	string s;
	while (ist >> s) {
		token.push_back(s);
	}
}

void insert(const vector <string>& token) {
	int now = 0;
	for (size_t i = 0; i < token.size(); i++) {
		map <string, int>& mp = v[now].next;
		if (mp.find(token[i]) != mp.end()) {
			now = mp[token[i]];
		} else {
			res++;
			now = (int)v.size();
			mp[token[i]] = now;
			v.push_back(A());
		}
	}
}

int main() {
	int T;
	scanf("%d", &T);
	for (int cas = 1; cas <= T; cas++) {
		scanf("%d%d", &n, &m);
		v.clear();
		v.push_back(a);
		for (int i = 0; i < n; i++) {
			char s[105];
			scanf("%s", s);
			vector <string> token;
			split(s, token);
			insert(token);
		}
		res = 0;
		for (int i = 0; i < m; i++) {
			char s[105];
			scanf("%s", s);
			vector <string> token;
			split(s, token);
			insert(token);
		}
		printf("Case #%d: %d\n", cas, res);
	}
	return 0;
}

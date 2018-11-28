#include <cstdio>
#include <map>
#include <string>
using namespace std;

map<char, char> mp;

bool ck[30];
bool ck2[30];
int main() {

	char str[1024];
	char str2[1024];

	string s = "ejp mysljylc kd kxveddknmc re jsicpdrysi";
	s += "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
	s += "de kr kd eoya kw aej tysr re ujdr lkgc jv";
	string s2 = "our language is impossible to understand";
	s2 += "there are twenty six factorial possibilities";
	s2 += "so it is okay if you want to just give up";
	s += "qz";
	s2 += "zq";
	for(int i=0;i<s.size();i++) {
		if(mp.find(s[i]) == mp.end()) {
			mp[s[i]] = s2[i];
			if(s[i] == ' ') continue;
			ck2[s[i]-'a'] = 1;
			ck[s2[i]-'a'] = 1;
		}
	}
	int T;
	scanf("%d", &T);
	gets(str);
	for(int q=1;q<=T;q++) {
		gets(str);
		printf("Case #%d: ", q);
		s = str;
		for(int i=0;i<s.size();i++) {
			s[i] = mp[s[i]];
		}
		printf("%s\n", s.c_str());
	}
	return 0;
}

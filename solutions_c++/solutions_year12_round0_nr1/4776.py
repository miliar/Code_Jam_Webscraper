#include<cstdio>
#include<string>
#include<map>
using namespace std;

int main() {
	string g = "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv";
	string e = "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up";
	map<char, char> mapping;
	for(int i  = 0; i < g.length(); i++) {
		mapping[g[i]] = e[i];
	}
	mapping['q'] = 'z';
	mapping['z'] = 'q';	
	int tc;
	scanf("%d", &tc);
	getchar();
	char st[500];
	for(int i = 1; i <= tc; i++) {
		gets(st);
		printf("Case #%d: ", i);
		for(int j = 0; st[j]; j++) {
			printf("%c", mapping[st[j]]);
		}
		printf("\n");
	}
	return 0;
}

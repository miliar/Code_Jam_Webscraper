#include<cstdio>
#include<algorithm>
#include<string>

using namespace std;

int casos;
string s, a[5], r[5];
char mapa[32];

int main(){
a[0] = "ejp mysljylc kd kxveddknmc re jsicpdrysi";
r[0] = "our language is impossible to understand";
a[1] = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
r[1] = "there are twenty six factorial possibilities";
a[2] = "de kr kd eoya kw aej tysr re ujdr lkgc jv";
r[2] = "so it is okay if you want to just give up";
	for(int i=0;i<=26;i++) mapa[i] = '#';
	for(int w=0;w<3;w++){
		for(int i=0;i<a[w].size();i++){
			if(a[w][i] == ' ') continue;
			mapa[a[w][i]-'a'] = r[w][i];
		}
	}
	mapa['z'-'a'] = 'q'; mapa['q'-'a'] = 'z';
	scanf(" %d ", &casos);
	for(int h=1;h<=casos;h++){
		s = "";
		char c;
		while(scanf("%c", &c) == 1 && c != '\n') s += c;
		printf("Case #%d: ", h);
		for(int i=0;i<s.size();i++){
			if(s[i] == ' ') printf(" ");
			else printf("%c", mapa[s[i]-'a']);
		}
		printf("\n");
	}
	return 0;
}


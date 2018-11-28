#include <cstdio>
#include <string>
#include <vector>
#include <iostream>
#include <set>
#include <algorithm>
#define sz(a) a.size()
#define forn(i,n) for(int i=0; i<(int)n; i++)
#define pb push_back
using namespace std;
bool used[30];
char G[30];
int main () {
#ifndef ONLINE_JUDGE
	freopen("A-small-attempt2.in","rt",stdin);
	freopen("A-small-attempt2.out","wt",stdout);
#endif
	string e = "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jvqz";
	string r = "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give upzq";
	forn(i,sz(e)) {
		if (!used[e[i]-'a'])
			G[e[i]-'a']=r[i];
	}
	int T;
	scanf("%d",&T);
	forn(i,T) {
		scanf("\n");
		string s;
		printf("Case #%d: ",(i+1));
		getline(cin,s);
		forn(j,sz(s))
			if (s[j]>='a'&&s[j]<='z')
				s[j]=G[s[j]-'a'];
		cout<<s<<endl;
	}
}
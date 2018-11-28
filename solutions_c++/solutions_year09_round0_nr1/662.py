#include <cstdio>
#include <cstring>
#include <string>
#include <set>
using namespace std;

int ans = 0;
int l, d, n;

set<string> dict[16];
char s[3000000];
string cur;

void dfs (int i,int k) {
	if (dict[k].find(cur)==dict[k].end())
		return;
	if (k==l) {
		++ans;
		return;
	}
	int e = i+1, a = i, b = i+1;
	if (s[i]=='(') {
		++i;
		while (s[e]!=')')
			++e;
		++e;
		b = e-1;
		a = i+1;
	}
	string last = cur;
	for (int j=i; j<b; j++) {
		cur = last + s[j];
		dfs(e,k+1);
	}
}

int main() {
	scanf("%d%d%d",&l,&d,&n);
	for (int i=0;i<d;i++) {
		scanf("%s",s);
		for (int i=strlen(s);i;i--)
			s[i]=0, dict[i].insert(string(s));
	}
	dict[0].insert("");
	for (int nn=1;nn<=n;nn++) {
		scanf("%s",s);
		cur = "";
		ans = 0;
		dfs(0,0);
		printf("Case #%d: %d\n", nn, ans);
	}
	return 0;
}

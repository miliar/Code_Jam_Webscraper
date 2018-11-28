#include <cstdio>
#include <string>
#include <set>
using namespace std;
int n,l,d;
int a[100000][26];
int q=0;
char s[500];
set<int> now,next;
int main() {
	int i,j;
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	scanf("%d%d%d",&l,&d,&n);
	for (i=1; i<=d; ++i) {
		scanf("%s",s);
		int now=0;
		for (j=0; j<l; ++j) {
			if (a[now][s[j]-'a']==0) a[now][s[j]-'a']=++q;
			now=a[now][s[j]-'a'];
		}
	}
	set<int>::iterator ii;
	for (i=1; i<=n; ++i) {
		scanf("%s",s);
		int len=strlen(s);
		int pos=0;
		j=0;
		now.clear();
		now.insert(0);

		while (j<l) {
			next.clear();
			if (s[pos]=='(') {
				while (1) {
					++pos;
					if (s[pos]==')') break;
					for (ii=now.begin(); ii!=now.end(); ++ii) if (a[*ii][s[pos]-'a']>0) next.insert(a[*ii][s[pos]-'a']);
				}
				now=next;
			} else {
				for (ii=now.begin(); ii!=now.end(); ++ii) if (a[*ii][s[pos]-'a']>0) next.insert(a[*ii][s[pos]-'a']);
				now=next;
			}
			++pos;
			++j;
		}
		printf("Case #%d: %d\n",i,now.size());		
	}
	return 0;
}
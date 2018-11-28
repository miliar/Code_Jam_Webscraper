#include <cstdio>
#include <string>
using namespace std;

char s[10000];
int a[10000][22];
int t[22];
int len;

bool mat(int *x,int *y) {
int i;
	for (i=0;i<len;++i) {
		if (((1<<x[i])&y[i])==0) {
			return false;
		}
	}
	return true;
}

int main() {
int i,j,k,n,d;
	freopen("in","r",stdin);
	freopen("out","w",stdout);
	scanf("%d%d%d",&len,&d,&n);
	for (i=0;i<d;++i) {
		scanf("%s",s);
		for (j=0;j<len;++j) {
			a[i][j]=s[j]-'a';
		}
	}
	for (i=1;i<=n;++i) {
		scanf("%s",s);
		for (j=k=0;k<len;++k,++j) {
			t[k]=0;
			if (s[j]=='(') {
				for (++j;s[j]!=')';++j) {
					t[k]|=(1<<(s[j]-'a'));
				}
			}
			else {
				t[k]|=(1<<(s[j]-'a'));
			}
		}
		for (j=k=0;j<d;++j) {
			if (mat(a[j],t)) {
				++k;
			}
		}
		printf("Case #%d: %d\n",i,k);
	}

	return 0;
}
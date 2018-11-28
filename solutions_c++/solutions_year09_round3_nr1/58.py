#include <cstdio>
#include <cstring>
typedef unsigned char uc;
typedef long long ll;
int b[1000];
int t,ii;
char s[1000];
int res[1000];
int main() {
	int i,k;
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	scanf("%d\n",&t);
	for (ii=1; ii<=t; ++ii) {
		scanf("%s",s);
		int len=strlen(s);
		memset(b,-1,sizeof(b));
		k=0;
		for (i=0; i<len; ++i) {
			if (b[(uc)s[i]]==-1) {
				if (k==0) b[(uc)s[i]]=1; else
				if (k==1) b[(uc)s[i]]=0; else
				b[(uc)s[i]]=k;
				++k;	
			}
			res[i]=b[(uc)s[i]];
		}
		if (k<2) k=2;
		ll ans=0;
		for (i=0; i<len; ++i) ans=ans*k+res[i];
		printf("Case #%d: %I64Ld\n",ii,ans);
	}
	return 0;
}
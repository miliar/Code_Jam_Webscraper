#include <cstdio>
#include <cstring>
const int c=510;
const int d=30;
typedef char str[c];
const str data="welcome to code jam";
const int dlen=strlen(data);
int n,len;
str s;
int a[c][d];
int main() {
	int ii,i,j,k,ans;
	freopen("c.in","r",stdin);
	freopen("c.out","w",stdout);
	scanf("%d",&n);
	getchar();
	for (ii=1; ii<=n; ++ii) {
		gets(s);
		len=strlen(s);
		memset(a,0,sizeof(a));
		for (i=0; i<len; ++i) {
			for (j=0; j<dlen; ++j) if (s[i]==data[j]) {
				if (j==0) a[i][j]=1; else {
					a[i][j]=0;
					for (k=0; k<i; ++k) if (s[k]==data[j-1]) a[i][j]=(a[i][j]+a[k][j-1])%10000;
				}
			}
		}
		ans=0;
		for (i=0; i<len; ++i) ans=(ans+a[i][dlen-1])%10000;
		printf("Case #%d: %04d\n",ii,ans);
	}
	return 0;
}
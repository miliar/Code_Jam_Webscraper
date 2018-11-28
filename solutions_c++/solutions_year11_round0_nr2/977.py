#include <cstdio>
#include <cstring>
#include <cctype>
const int cc=256;
int t,ii;
int c,d,n;
char ac[cc][cc];
bool ad[cc][cc];
char s[cc];
int len;
inline void geth(char &h) {
	do h=getchar(); while (!isalpha(h));
}
int main() {
	int i,j;
	char h,h1,h2,h3;
	scanf("%d",&t);
	for (ii=1; ii<=t; ++ii) {
		printf("Case #%d: ",ii);
		memset(ac,0,sizeof(ac));
		memset(ad,0,sizeof(ad));
		scanf("%d",&c);
		for (i=1; i<=c; ++i) {
			geth(h1);
			geth(h2);
			geth(h3);
			ac[h1][h2]=ac[h2][h1]=h3;
		}
		scanf("%d",&d);
		for (i=1; i<=d; ++i) {
			geth(h1);
			geth(h2);
			ad[h1][h2]=ad[h2][h1]=1;
		}
		scanf("%d",&n);
		len=0;
		for (i=1; i<=n; ++i) {
			geth(h);
			s[len++]=h;
			if (len>1 && ac[s[len-2]][s[len-1]]) {
				len--;
				s[len-1]=ac[s[len-1]][s[len]];
			}
			if (len>0) {
				for (j=0; j<len; ++j) if (ad[s[j]][s[len-1]]) break;
				if (j<len) len=0;
			}
		}
		printf("[");
		for (i=0; i<len-1; ++i) printf("%c, ",s[i]);
		if (len>0) printf("%c",s[len-1]);
		printf("]\n");
	}	
	return 0;
}
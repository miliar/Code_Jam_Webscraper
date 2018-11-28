#include <stdio.h>
#include <string.h>

#include <algorithm>

using namespace std;

char w[] = "welcome to code jam";

int d[1111][22];
char s[1111];

int main(void) {
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);
	int wlen = strlen(w);
	int t=1;
	int N;
	scanf("%d\n", &N);
	while(N--) {
		gets(s); int len = strlen(s);

		memset(d, 0, sizeof(d));

		if(s[0]==w[0]) d[0][0]=1;

		for(int i=1;i<len;i++) {
			for(int j=0;j<wlen;j++) {
				d[i][j] = d[i-1][j];
				if(s[i]==w[j]) {
					if(j==0) d[i][0]++;
					else d[i][j] += d[i-1][j-1];
				}
				d[i][j]%=10000;
			}
		}
		printf("Case #%d: %04d\n", t++, d[len-1][wlen-1]);
	}
	

	return 0;
}
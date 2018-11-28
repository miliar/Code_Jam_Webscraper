/* vim: set sw=4 sts=4 noet tw=80 : */
#include <cstring>
#include <cstdio>

const char *s="welcome to code jam";
char line[1000];
int T[600][22];


int main() {
	int N;
	int LL=strlen(s);
	fgets(line, 900, stdin);
	sscanf(line, "%d", &N);
	for(int i=0;i<N;++i) {
		fgets(line, 900, stdin);
		bzero(T,sizeof(T));
		int L = strlen(line); //  \n at the end!
		for(int j=L-1;j>=0;--j) {
			T[j+1][LL]=1;
			for(int k=0;k<LL;++k) {
				T[j][k] = T[j+1][k];
				if (line[j]==s[k])
					T[j][k] = (T[j][k] + T[j+1][k+1]) % 10000;
			}
		}
		printf("Case #%d: %04d\n", i+1, T[0][0]);
	}
	return 0;
}


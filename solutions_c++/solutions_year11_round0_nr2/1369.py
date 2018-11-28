#include <iostream>
#include <cstring>
#include <cstdio>

using namespace std;

bool s[256][256];
char m[256][256];
int t;
char str[500];

int main() {
	scanf("%d", &t);
	for(int cas=1; cas<=t; ++cas) {
		memset(s, 0, sizeof(s));
		memset(m, 0, sizeof(m));
		int tn;
		scanf("%d", &tn);
		for(int i=0; i<tn; ++i) {
			scanf("%s", str);
			m[str[0]][str[1]] = str[2];
			m[str[1]][str[0]] = str[2];
		}
		scanf("%d", &tn);
		for(int i=0; i<tn; ++i) {
			scanf("%s", str);
			s[str[0]][str[1]] = true;
			s[str[1]][str[0]] = true;
		}
		scanf("%d", &tn);
		scanf("%s", str+1);
		int j=1;
		for(int i=1; i<=tn; ++i) {
			str[j++] = str[i];
			while(j>2&&m[str[j-2]][str[j-1]]) {
				str[j-2] = m[str[j-2]][str[j-1]];
				--j;
			}
			for(int k=1; k<j; ++k) {
				if(s[str[k]][str[j-1]]) j=1;
			}
		}
		if(j==1) {
			printf("Case #%d: [%s]\n", cas, "");
			continue;
		}
		for(int i=j-1; i>0; --i) {
			str[i*3] = str[i];
			str[i*3+1] = ',';
			str[i*3+2] = ' ';
		}
		str[3*(j-1)+1] = 0;
		printf("Case #%d: [%s]\n", cas, str+3);
	}
}

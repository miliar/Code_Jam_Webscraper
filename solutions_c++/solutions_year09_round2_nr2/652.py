#include <iostream>
#include <iomanip>
#include <sstream>
#include <string>
#include <vector>
#include <deque>
#include <set>
#include <map>
#include <bitset>
#include <valarray>
#include <algorithm>
#include <functional>
#include <numeric>
#include <complex>
#include <utility>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <cmath>
#include <queue>
using namespace std;

int b[100];
char s[100];

void gao(int x,int y) {
	for (;y;--y) {
		printf("%d",x);
	}
}

int main() {
int n,c,i,j,z,zz;
	freopen("in","r",stdin);
	freopen("out","w",stdout);
	scanf("%d",&zz);
	for (z=1;z<=zz;++z) {
		scanf("%s",s);
		printf("Case #%d: ",z);
		n=strlen(s);
		memset(b,0,sizeof(b));
		for (i=n-1;i>=0;--i) {
			++b[c=s[i]-'0'];
			for (++c;c<10;++c) {
				if (b[c]) {
					break;
				}
			}
			if (c<10) {
				for (j=0;j<i;++j) {
					printf("%c",s[j]);
				}
				printf("%d",c);
				--b[c];
				for (j=0;j<10;++j) {
					gao(j,b[j]);
				}
				break;
			}
		}
		if (i<0) {
			for (j=1;j<10;++j) {
				if (b[j]) {
					break;
				}
			}
			printf("%d0",j);
			--b[j];
			for (j=0;j<10;++j) {
				gao(j,b[j]);
			}
		}
		puts("");

	}
	return 0;
}




	

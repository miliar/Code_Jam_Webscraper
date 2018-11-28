#include <cstdio>
#include <algorithm>
#include <iostream>
#include <string>
using namespace std;



int ntc,n;
char cos[40],niu[40];

int main() {
	scanf("%d", &ntc);
	for(int x=1; x<=ntc; ++x) {
		scanf("%s", cos);
		n=0; while(cos[n++]!='\0');
		--n;
		if(next_permutation(cos,cos+n)) {
			printf("Case #%d: %s\n",x,cos);
		}
		else {
			for(int i=n+1; i>0; --i) cos[i]=cos[i-1];
			cos[0]='0';
			for(int i=1; i<=n; ++i) {
				if(cos[i]>cos[i-1]) {
					cos[0]=cos[i];
					cos[i]='0';
					break;
				}
			}
			printf("Case #%d: %s\n",x,cos);
				
		}
	}
}

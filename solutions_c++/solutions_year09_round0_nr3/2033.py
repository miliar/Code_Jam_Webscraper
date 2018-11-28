#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
char s[505], X[]="maj edoc ot emoclew", Xlen = 19;
int D[505][20];
int main() {
	int N,res=0,len;
	scanf("%d\n",&N);
	for(int x=1;x<=N;++x) {
		fgets(s,505,stdin);
		len = strlen(s);
		for(int i=len;i>=0;--i)
			for(int k=0;k<20;++k)
				D[i][k] = 0;
		D[len-1][0] = (s[len-1] == X[0]);
		for(int i=len-2;i>=0;--i) {
			for(int k=0;k<=19;++k) {
				D[i][k]=D[i+1][k]; 
				if(s[i]==X[k] && k!=0) D[i][k]+=D[i+1][k-1];
				if(s[i]==X[k] && k==0) D[i][k]++;
				D[i][k]%=10000;
			}
		}
		printf("Case #%d: %0*d\n", x, 4, D[0][18]%10000);
	}
	return 0;
}

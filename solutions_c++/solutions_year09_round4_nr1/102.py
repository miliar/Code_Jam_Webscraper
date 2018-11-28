#include <stdio.h>
#include <string.h>

int v[40];
char s[60];
int N;

int solve(){
	int ret=0;
	int i,j,k;
	for (i=0;i<N;i++){
		scanf("%s",s);
		for (j=N-1;j>0;j--) if (s[j]=='1') break;
		v[i]=j;
	}
	for (i=0;i<N;i++){
		for (j=i;j<N;j++){
			if (v[j]<=i) break;
		}
		ret+=j-i;
		for (k=j;k>i;k--) v[k]=v[k-1];
	}
	return ret;
}

int main(){
	int T,cas;
	scanf("%d",&T);
	for (cas=1;cas<=T;cas++){
		scanf("%d",&N);
		printf("Case #%d: %d\n",cas,solve());
	}
	return 0;
}


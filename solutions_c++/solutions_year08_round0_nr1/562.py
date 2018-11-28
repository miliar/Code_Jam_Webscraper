#include <stdio.h>
#include <stdlib.h>
#include <memory.h>
#include <string.h>

char se[100][105];
int q[1000];
int nse,nq;

char mask[1000];
int work() {
	memset(mask,0,sizeof(char)*nse);
	int sw = 0;
	int total = 0;
	for(int i=0;i<nq;i++) {
		if (!mask[q[i]]) {
			mask[q[i]]=1;
			total++;
			if (total==nse) {
				sw ++;
				memset(mask,0,sizeof(char)*nse);
				total = 0;
				i--;
			}
		}
	}
	return sw;
}
int main() {
	int n;
	scanf("%d", &n);
	for(int i=1;i<=n;i++) {
		scanf("%d ",&nse);
		for(int j=0;j<nse;j++){
			gets(se[j]);
		}
		scanf("%d ",&nq);
		for(int j=0;j<nq;j++) {
			char query[105];
			gets(query);
			q[j]=-1;
			for(int k=0;k<nse;k++) {
				if (strcmp(se[k],query)==0) {
					q[j]=k; break;
				}
			}
			if (q[j]<0) {
				printf("error.");
			}
		}
		printf("Case #%d: %d\n",i,work());
		
	}
//	scanf("%d",&n);
	return 0;
}
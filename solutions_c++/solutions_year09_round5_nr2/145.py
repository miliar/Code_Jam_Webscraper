#include<stdio.h>
#include<map>

using namespace std;

#define MOD 10009
#define lint long long

map<lint,int> M[11];
map<lint,int>::iterator it;

char par[100];
char wrd[100][51];
lint val[100];
int ans[11];
int K, N;

int main() {
	int t,T,i,j,k,s,l;
	lint v;
	scanf("%d\n",&T);
	M[0][0] = 1;
	for(t=1;t<=T;t++) {
		scanf("%s %d %d",par,&K,&N);
		for(i=0;i<N;i++) {
			scanf("%s",wrd[i]);
		}
		
		for(k=1;k<=K;k++) ans[k] = 0;
		
		s=0;
		while(1) {
			for(i=0;i<N;i++) {
				val[i] = 0;
				for(j=s;par[j] >= 'a' && par[j] <= 'z';j++) {
					for(k=0;wrd[i][k];k++) {
						if(wrd[i][k] != par[j]) continue;
						val[i] += (lint)1<<(9*(j-s));
					}
				}
			}
			l=j-s;
			s=j;
			for(k=1;k<=K;k++) M[k].clear();
			
			for(k=0;k<K;k++) {
				for(i=0;i<N;i++) {
				//for(k=K-1;k>=0;k--) {
				//for(k=0;k<K;k++) {
					for(it=M[k].begin();it!=M[k].end();it++) {
						v = it->first + val[i];
						M[k+1][v] += it->second;
						M[k+1][v] %= MOD;
					}
				}
			}
			
			
			for(k=1;k<=K;k++) {
//				printf("%d",k);
				for(it=M[k].begin();it!=M[k].end();it++) {
					v = 1;
					for(j=0;j<l;j++) {
						v *= (((it->first)>>(9*j))&511);
					}
//					printf(" %d(%d)",v,it->second);
					v %= MOD;
					v *= it->second;
					v %= MOD;
//					printf(" = %d",v);
					ans[k] = (ans[k]+v)%MOD;
				}
//				printf("\n");
			}
			
			if(par[s]!='+') break;
			s++;
		}
		printf("Case #%d:",t);
		for(k=1;k<=K;k++) {
			printf(" %d",ans[k]);
		}
		printf("\n");
	}
	return 0;
}

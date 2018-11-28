#include<stdio.h>
#include<string.h>
char path[1000][1000];
char path2make[1000][1000];
int main() {
	int i,j,l,k,len1, len2, N, M,m,T;
	freopen("google1.txt","r",stdin);
	freopen("google2.txt","w",stdout);
	scanf("%d", &T);
	for(i=0;i<T;i++){
		int cnt=0;
		scanf("%d %d", &N, &M);
		for(j=0;j<N;j++){
			scanf("%s", path[j]);
			k = strlen(path[j]);
			path[j][k] = '/';
			path[j][k+1] = 0;
		}
		for(l=0;l<M;l++){
			scanf("%s", path2make[l]);
			len1 = strlen(path2make[l]);
			path2make[l][len1] = '/';
			path2make[l][len1+1] = 0;
			len1++;
			m=0;
			for(j=0;j<N;j++) {
				len2 = strlen(path[j]);
				for(k=0;k<len2 && k<len1 && path[j][k] == path2make[l][k];k++) {
					if(path[j][k] == '/' && k>m)m = k;
				}
			}
			for(j=m+1;j<len1;j++){
				if(path2make[l][j]=='/')cnt++;			
			}
			
			strcpy(path[N],path2make[l]);
			N++;
		}
		printf("Case #%d: %d\n", i+1, cnt);
		
	}
	
	return 0;	
}

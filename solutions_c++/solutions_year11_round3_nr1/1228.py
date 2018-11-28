//GCJ 1C A
#include <cstdio>

int main(){
	int t,tt,i,j,m,n,cnt;
	char d[55][55];
	scanf("%d",&tt);

	for(t=1;t<=tt;t++){
		scanf("%d%d",&m,&n);
		printf("Case #%d:\n",t);
		for(i=0;i<m;i++){
			scanf("%s",d[i]);
		}
		for(i=0,cnt=0;i<m;i++){
			for(j=0;j<n;j++){
				if(d[i][j]=='#'){
					cnt++;
				}
			}
		}
		if(cnt%4!=0){
			printf("Impossible\n");
			continue;
		}
		for(i=0;i<m;i++){
			for(j=0;j<n;j++){
				if(d[i][j]=='#'){
					if(i==m-1 || j==n-1 || d[i][j+1]=='.' || d[i+1][j]=='.' || d[i+1][j+1] == '.'){
						printf("Impossible\n");
						cnt=-1;
						break;
					}
					d[i][j]=d[i+1][j+1]='/';
					d[i][j+1]=d[i+1][j]='\\';
					j++;
				}
			}
			if(cnt==-1) break;
		}
		if(cnt==-1) continue;
		for(i=0;i<m;i++){
			for(j=0;j<n;j++){
				printf("%c",d[i][j]);
			}
			printf("\n");
		}
	}
	return 0;
}

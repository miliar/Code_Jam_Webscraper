#include<stdio.h>
#include<string.h>
#define MAXN 60
char map[MAXN][MAXN];
int main()
{
	int i,j,k,m,n,t,ca=1;
	freopen("A-large.in","r",stdin);
	freopen("A2.txt","w",stdout);
	scanf("%d%*c",&t);
	while(t--){
		scanf("%d%d%*c",&n,&m);
		for(i=0;i<n;i++){
			gets(map[i]);
		}
		for(i=0;i<n;i++){
			for(j=0;j<m;j++){
				if(map[i][j]=='#'){
					if(j+1<m&&i+1<n){
						if(map[i][j+1]=='#'&&map[i+1][j]=='#'&&map[i+1][j+1]=='#'){
							map[i][j]=map[i+1][j+1]='\/';
							map[i][j+1]=map[i+1][j]='\\';
						}
						else
							break;
					}
					else
						break;
				}
			}
			if(j<m)
				break;
		}
		printf("Case #%d:\n",ca++);
		if(i==n){
			for(i=0;i<n;i++)
				puts(map[i]);
		}
		else
			printf("Impossible\n");
	}
	return 0;
}

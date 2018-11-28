#include <cstdio>
#include <cstring>
#include <iostream>
using namespace std;
#define M 100
char sou[M+5][M+5];
char mid[M+5][M+5];
int n,m;

int check(int u,int v,char ch){
	int i,j;

	for(i=0;i<m;i++){
		int dy=v+i;
		if(dy>=n) break;
		if(mid[u][dy]!=ch)
			break;
	}

	if(i==m) return 1;
	for(i=0;i<m;i++){
		int dx=u+i;
		if(dx>=n) break;
		if(mid[dx][v]!=ch)
			break;
	}
	if(i==m) return 1;

	for(i=0;i<m;i++){
		int dx=u+i;
		int dy=v+i;
		if(dx>=n||dy>=n) break;
		if(mid[dx][dy]!=ch)
			break;
	}
	if(i==m) return 1;

	for(i=0;i<m;i++){
		int dx=u-i;
		int dy=v+i;
		if(dx<0||dy>=n) break;
		if(mid[dx][dy]!=ch)
			break;
	}
	if(i==m) return 1;
	return 0;
}

int main(){
	freopen("big.in","rb",stdin);
	freopen("big.out","wb",stdout);

	int ca,c=0,i,j,k;
	scanf("%d",&ca);
	while(ca--){
		c++;
		scanf("%d%d",&n,&m);

		for(i=0;i<n;i++){
			scanf("%s",&sou[i]);
		}

		for(i=0;i<n;i++){
			for(j=0;j<n;j++){
				mid[j][n-i-1]=sou[i][j];
			}
		}


		for(i=n-2;i>=0;i--){
			for(j=0;j<n;j++){
				if(mid[i][j]!='.'){
					k=i+1;
					while(mid[k][j]=='.'&&k<n)
						k++;

					if(k==i+1)
						continue;
					char ch;
					ch=mid[k-1][j];
					mid[k-1][j]=mid[i][j];
					mid[i][j]=ch;
				}
			}
		}
		for(i=0;i<n;i++)
			mid[i][n]=0;
		//for(i=0;i<n;i++)
		//	printf("%s\n",mid[i]);


		int flag1=0,flag2=0;
		for(i=0;i<n;i++){
			for(j=0;j<n;j++){
				if(mid[i][j]=='R'){
					if(check(i,j,'R'))
						flag1=1;
				}
				if(mid[i][j]=='B'){
					if(check(i,j,'B'))
						flag2=1;
				}
			}
		}

		if(flag1&&flag2){
			printf("Case #%d: Both\n",c);
		}
		if((!flag1)&&(!flag2)){
			printf("Case #%d: Neither\n",c);
		}
		if(flag1&&(!flag2)){
			printf("Case #%d: Red\n",c);
		}
		if((!flag1)&&flag2){
			printf("Case #%d: Blue\n",c);
		}
	}
	//system("pause");
	return 0;
}
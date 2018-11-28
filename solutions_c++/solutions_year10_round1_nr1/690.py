#include<cstdio>
#include<algorithm>
#include<cstring>

using namespace std;

#define N 55

int n,m,ans[3];
int data[N][N];

int proc(int y,int x,int k,int code,int col){
	if (x<0 || x>=n) return 0;
	if (y<0 || y>=n) return 0;
	if (data[y][x]!=col) return 0;
	if (k==m) return 1;
	switch(code){
		case 0:
			return proc(y,x+1,k+1,code,col);
			break;
		case 1:
			return proc(y+1,x,k+1,code,col);
			break;
		case 2:
			return proc(y+1,x+1,k+1,code,col);
			break;
		case 3:
			return proc(y+1,x-1,k+1,code,col);
			break;
	}
	return 0;
}

int main(){
	int i,j,k,l,tc;
	char str[N];
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d",&tc);
	for(int tcc=1;tcc<=tc;tcc++){
		ans[1]=ans[2]=0;
		scanf("%d %d ",&n,&m);
//		printf("%d %d\n",n,m);
//		printf("***********\n");
		for(i=0;i<n;i++){
			scanf("%s",&str);
			for(j=0;j<n;j++){
				if (str[j]=='.'){
					data[i][j]=0;
				}else if (str[j]=='B'){
					data[i][j]=1;
				}else {
					data[i][j]=2;
				}
			}
//			printf("%s\n",str);
		}
//		printf("**\n");
		for(i=0;i<n;i++){
			k=n-1;
			for(j=n-1;j>=0;j--){
				if (data[i][j]!=0){
					data[i][k]=data[i][j];
					if (j!=k) data[i][j]=0;
					k--;
				}
			}
		}
		for(i=0;i<n;i++){
			for(j=0;j<n;j++){
				if (data[i][j]==0) continue;
				for(l=0;l<4;l++){
					ans[data[i][j]]|=proc(i,j,1,l,data[i][j]);
				}
			}
		}
		if (ans[1]+ans[2]==2){
			printf("Case #%d: Both\n",tcc);
		}else if (ans[1]+ans[2]==0){
			printf("Case #%d: Neither\n",tcc);
		}else if (ans[1]!=0){
			printf("Case #%d: Blue\n",tcc);
		}else {
			printf("Case #%d: Red\n",tcc);
		}
	}
	return 0;
}
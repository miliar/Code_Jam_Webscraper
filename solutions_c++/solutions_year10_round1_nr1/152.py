#include <stdio.h>
#include <string.h>
char b[60][60];
char b2[60][60];

bool chk(int x,int y,int n,int k){
	char p=b2[x][y];
	int dx[]={1,-1,0,0,-1,1,1,-1};
	int dy[]={0,0,-1,1,-1,1,-1,1};
	for(int i=0;i<8;i++){
		int nx=x,ny=y;
		bool ok=1;
		for(int j=1;j<k;j++){
			nx+=dx[i];
			ny+=dy[i];
			if(nx>=n || ny>=n || nx<0 ||ny<0){
				ok=0;
				break;
			}
			if(b2[nx][ny]!=p){
				ok=0;
				break;
			}
		}
		if(ok)
			return 1;
	}
	return 0;
}

int main(){
	int T;
	scanf("%d",&T);
	for(int TT = 1; TT <=T; TT++){
		int n,k;
		scanf("%d%d",&n,&k);
		for(int i=0;i<n;i++){
			scanf("%s", b[i]);
		}
		memset(b2,'.',sizeof(b2));
		for(int i=0;i<n;i++){
			for(int j=n-1,k=n-1;j>=0;j--){
				if(b[i][j]!='.'){
					b2[i][k] = b[i][j];
					k--;
				}
			}
			b2[i][n]=0;
		}
		bool r=0,b=0;
		for(int i=0;i<n;i++){
			for(int j=0;j<n;j++){
				if(b2[i][j] != '.'){
					if(chk(i,j,n,k)){
						if(b2[i][j]=='R'){
							r=1;
						}else{
							b=1;
						}
					}
				}
			}
		}
		printf("Case #%d: ", TT);
		if(r && b){
			printf("Both\n");
		}else if(r){
			printf("Red\n");
		}else if(b){
			printf("Blue\n");
		}else{
			printf("Neither\n");
		}
	}
}
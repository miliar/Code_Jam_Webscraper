#include <iostream>
#include <cstring>
#include <cstdio>
#include <algorithm>
#include <vector>
using namespace std;

#define pb push_back
#define sz size()
#define MAXN 101

void opens(){
	freopen("Csmall.in","r",stdin);
	freopen("Csmall.out","w",stdout);
}

void openb(){
	freopen("Clarge.in","r",stdin);
	freopen("Clarge.out","w",stdout);
}
int t,n,mat[MAXN][MAXN],mat2[MAXN][MAXN],ans,x,y,x2,y2;

int main(){
	opens();
	//openb();
	scanf("%d",&t);
	int xx=1;
	while (t--){
		scanf("%d",&n);
		memset(mat,0,sizeof(mat));
		for (int i=0;i<n;i++){
			scanf("%d%d%d%d",&x,&y,&x2,&y2);
			for (int j=x;j<=x2;j++){
				for (int k=y;k<=y2;k++){
					mat[j][k]=1;
				}
			}
		}
		ans=0;
		memset(mat2,0,sizeof(mat2));
		while (1){
			memcpy(mat2,mat,sizeof(mat2));
			bool valid=1;
			for (int i=1;i<=100;i++){
				for (int j=1;j<=100;j++){
					if (mat2[i][j]==1){
						valid=0;
						break;
					}
				}
				if (!valid) break;
			}
			if (valid) break;
			ans++;
			for (int i=1;i<=100;i++){
				for (int j=1;j<=100;j++){
					if (mat[i-1][j]==0 && mat[i][j-1]==0){
						mat2[i][j]=0;
					}
					if (mat[i-1][j]==1 && mat[i][j-1]==1){
						mat2[i][j]=1;
					}
				}
			}
			memcpy(mat,mat2,sizeof(mat));
		}
		printf("Case #%d: %d\n",xx++,ans);
	}
	//system("pause");
	return 0;
}

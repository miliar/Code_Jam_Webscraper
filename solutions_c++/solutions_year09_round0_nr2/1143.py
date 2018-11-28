#include<algorithm>
#include<iostream>
#include<math.h>
#include<map>
#include<string>
using namespace std;
#define memo(a,b) memset(a,b,sizeof(a))

int mov[4][2]={-1,0,0,-1,0,1,1,0},n,m,b[105][105],a[105][105],k;

bool valid(int x,int y){
	if(x<0 || x>=n || y<0 || y>=m) return false;
	return true;
}
int solve(int x,int y){
	if(b[x][y]!=-1){
		return b[x][y];
	}
	int i,j,mn;
	mn = a[x][y];
	for(i=0;i<4;i++){
		if(valid(x+mov[i][0],y+mov[i][1])){
			if(a[x+mov[i][0]][y+mov[i][1]]<mn){
				mn=a[x+mov[i][0]][y+mov[i][1]];
				j = i;
			}
		}
	}
	if(mn==a[x][y]){
		b[x][y]=k++;
	}
	else b[x][y]=solve(x+mov[j][0],y+mov[j][1]);
	return b[x][y];
}
int main(){
	
//	freopen("B.in","r",stdin);
//	freopen("B.ans","w",stdout);
	int i,j,cs,t;
	scanf("%d",&t);
	for(cs=1;cs<=t;cs++){
		scanf("%d %d",&n,&m);
		for(i=0;i<n;i++){
			for(j=0;j<m;j++) {
				scanf("%d",&a[i][j]);
				b[i][j]=-1;
			}
		}
		for(i=0,k=0;i<n;i++){
			for(j=0;j<m;j++){
				if(b[i][j]==-1){
					solve(i,j);
				}
			}
		}
		printf("Case #%d:\n",cs);
		for(i=0;i<n;i++){
			for(j=0;j<m;j++){
				if(j) printf(" ");
				printf("%c",b[i][j]+97);
			}
			puts("");
		}
	}
	return 0;
}
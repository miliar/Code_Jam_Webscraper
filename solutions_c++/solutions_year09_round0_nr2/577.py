//poj 

#include<iostream>
#include<stdlib.h>
#include<string.h>
#include<algorithm>
#include<map>
#include<math.h>
#include<vector>
#include<set>
#include<queue>

using namespace std;
typedef long long llt;

#define maxv 105

#define LEN 17
#define myAbs(x) ((x)>=0?(x):-(x))
#define Max(x,y) ((x)>(y)?(x):(y))
#define Min(x,y) ((x)<(y)?(x):(y))
#define inf 1999999999
#define MOD 200039
#define eps 1e-8
#define EPS 1e-8
#define M_PI 3.14159265358979323846



int M[maxv][maxv];
int res[maxv][maxv];
int r,c;
int step[4][2]={-1,0,0,-1,0,1,1,0};
int end;
int ttt;

int inMap(int rr ,int cc){
	if(rr < 0 || rr >= r|| cc < 0|| cc >=c)
		return 0;
	return 1;
}
int dfs(int r,int c){
	if(res[r][c]!=-1){
		return res[r][c];
	}
	int mi= M[r][c];
	int i,k;
	int flag=0;
	int rr,cc;
	for(i=0;i<4;++i){
		rr= r+ step[i][0];
		cc= c+ step[i][1];
		if(inMap(rr,cc) && M[rr][cc] < mi){
			flag=1;
			mi = M[rr][cc]; 
			k=i;
		}
	}
	if(flag==0){
		return res[r][c]=end++;
	}else{
		return res[r][c]=dfs(r+step[k][0], c+ step[k][1]);
	}
}
void solve(){
	int i,j,k;
	scanf("%d%d",&r,&c);
	for(i=0;i<r;++i){
		for(j=0;j<c;++j){
			scanf("%d",M[i]+j);
		}
	}
	memset(res,-1,sizeof(res));
	end=0;
	for(i=0;i<r;++i){
		for(j=0;j<c;++j){
			dfs(i,j);
		}
	}
	printf("Case #%d:\n",++ttt);
	for(i=0;i<r;++i){
		for(j=0;j<c;++j){
			printf("%c ",res[i][j]+'a');
		}
		printf("\n");
	}
}
int main(){
	//freopen("out.txt","w",stdout);
	ttt=0;
	int t;
	scanf("%d",&t);
	while(--t>=0){
		solve();
	}
	//system("PAUSE");
	return 0;
}


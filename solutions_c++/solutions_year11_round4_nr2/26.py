#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <vector>
#include <string>
#include <map>
#include <algorithm>
using namespace std;

typedef long long ll;

long long board[600][600];
long long xs[600][600];
long long ys[600][600];
long long ms[600][600];

main(){
	int datasuu;
	scanf("%d ",&datasuu);
	for(int casenum=1;casenum<=datasuu;casenum++){
		printf("Case #%d: ",casenum);
		
		int isize,jsize,d;
		scanf("%d%d%d ",&isize,&jsize,&d);
		for(int i=0;i<isize;i++){
			char buf[1000];
			gets(buf);
			for(int j=0;j<jsize;j++)board[i][j]=buf[j]-'0'+1;
		}
		for(int i=0;i<=isize;i++){
			for(int j=0;j<=jsize;j++){
				if(i==0 || j==0)xs[i][j]=ys[i][j]=ms[i][j]=0;
				else{
					xs[i][j]=xs[i-1][j]+xs[i][j-1]-xs[i-1][j-1]+board[i-1][j-1]*(i-1);
					ys[i][j]=ys[i-1][j]+ys[i][j-1]-ys[i-1][j-1]+board[i-1][j-1]*(j-1);
					ms[i][j]=ms[i-1][j]+ms[i][j-1]-ms[i-1][j-1]+board[i-1][j-1];
				}
			}
		}
		int ans=-1;
		for(int i=0;i<isize;i++){
			for(int j=0;j<jsize;j++){
				for(int k=3;i+k<=isize && j+k<=jsize;k++){
					ll x=xs[i+k][j+k]-xs[i][j+k]-xs[i+k][j]+xs[i][j];
					ll y=ys[i+k][j+k]-ys[i][j+k]-ys[i+k][j]+ys[i][j];
					ll m=ms[i+k][j+k]-ms[i][j+k]-ms[i+k][j]+ms[i][j];
					x-=(board[i][j]*i+board[i][j+k-1]*i+board[i+k-1][j]*(i+k-1)+board[i+k-1][j+k-1]*(i+k-1));
					y-=(board[i][j]*j+board[i][j+k-1]*(j+k-1)+board[i+k-1][j]*j+board[i+k-1][j+k-1]*(j+k-1));
					m-=(board[i][j]+board[i][j+k-1]+board[i+k-1][j]+board[i+k-1][j+k-1]);
					//printf("%d,%d kara %d:%lld %lld %lld\n",i,j,k,x,y,m);
					if(2*x%m==0 && 2*x/m==2*i+(k-1)){ //x/m==i+(k-1)/2
					if(2*y%m==0 && 2*y/m==2*j+(k-1)){ //y/m==j+(k-1)/2
						ans=max(ans,k);
					}
					}
				}
			}
		}
		if(ans==-1)puts("IMPOSSIBLE");
		else printf("%d\n",ans);
	}
}
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
#include<limits.h>
#include<iostream>
#include<iomanip>
#include<sstream>
#include<algorithm>
#include<functional>
#include<vector>
#include<string>
#include<stack>
#include<queue>
#include<set>
#include<map>
#include<complex>
#define EPS (1e-8)
#define PI (3.141592653589793238)
#define MP make_pair
typedef long long ll;
using namespace std;

int board[510][510];
int xsum[510][510];
int sum[510][510];

inline int calc(int x1,int y1,int x2,int y2){
	return sum[x2+1][y2+1]-sum[x1][y2+1]-sum[x2+1][y1]+sum[x1][y1];
}

bool solve(int x,int y,int k){
	int x1=x,x2,x3,x4=x+k-1;
	int y1=y,y2,y3,y4=y+k-1;
	if(k%2==0){
		x2=(x1+x4)/2;
		x3=x2+1;
		y2=(y1+y4)/2;
		y3=y2+1;
	}else{
		x2=(x1+x4)/2-1;
		x3=x2+2;
		y2=(y1+y4)/2-1;
		y3=y2+2;
	}
	int i,j;
	for(i=0;i<x2-x1;i++){
		int ii=i+1;

	}
	//printf("x=%d y=%d k=%d   x:(%d,%d,%d,%d) y:(%d,%d,%d,%d) ",x,y,k,x1,x2,x3,x4,y1,y2,y3,y4);
	//if((calc(x1,y1,x2,y4)-board[x1][y1]-board[x1][y4])!=(calc(x3,y1,x4,y4)-board[x4][y1]-board[x4][y4]))return false;
	//if((calc(x1,y1,x4,y2)-board[x1][y1]-board[x4][y1])!=(calc(x1,y3,x4,y4)-board[x1][y4]-board[x4][y4]))return false;
	return true;
}

int main(void){
	int T;
	scanf("%d",&T);
	for(int casenum=1;casenum<=T;casenum++){
		int i,j,k;
		int xx,yy,D;
		scanf("%d %d %d ",&yy,&xx,&D);
		for(j=0;j<yy;j++){
			char ch[510];
			gets(ch);
			for(i=0;i<xx;i++){
				board[i][j]=ch[i]-'0';
			}
		}
		for(j=0;j<yy;j++){
			for(i=0;i<xx;i++){
				xsum[i+1][j+1]=board[i][j];
				if(i>0)xsum[i+1][j+1]+=xsum[i+1-1][j+1];
			}
		}
		for(j=0;j<yy;j++){
			for(i=0;i<xx;i++){
				sum[i+1][j+1]=xsum[i+1][j+1];
				if(j>0)sum[i+1][j+1]+=sum[i+1][j+1-1];
			}
		}
		/*for(j=0;j<=yy;j++){
			for(i=0;i<=xx;i++){
				printf("%d ",sum[i][j]);
			}
			puts("");
		}*/
		int ans=0;
		int p,q;
		for(i=0;i<xx;i++){
			for(j=0;j<yy;j++){
				for(k=3;;k++){
					if(k<ans || i+k>xx || j+k>yy)break;
					double xs=0,ys=0,xc=0,yc=0;
					for(p=i;p<=i+k-1;p++)for(q=j;q<=j+k-1;q++){
						if(p==i && q==j)continue;
						if(p==i+k-1 && q==j)continue;
						if(p==i && q==j+k-1)continue;
						if(p==i+k-1 && q==j+k-1)continue;
						xs+=p*(board[p][q]+D);
						ys+=q*(board[p][q]+D);
						xc+=(board[p][q]+D);
						yc+=(board[p][q]+D);
					}
					double xw=xs/xc,yw=ys/yc;
					//printf("%d %d %d   %lf %lf\n",i,j,k,xw,yw);
					bool b=false;
					double xp,yp;
					xp=((double)i+i+k-1)/2;
					yp=((double)j+j+k-1)/2;
					if(fabs(xw-xp)<=EPS && fabs(yw-yp)<=EPS)b=true;
					if(b)ans=max(ans,k);
				}
			}
		}
		printf("Case #%d: ",casenum);
		if(ans!=0)printf("%d\n",ans);
		else printf("IMPOSSIBLE\n");
	}
	return 0;
}

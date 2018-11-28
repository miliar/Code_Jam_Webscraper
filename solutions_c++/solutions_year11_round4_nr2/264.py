#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

#define maxn 50
int R,C,D;
char mat[505][505];

struct DD{
	double M,x,y;
}; //



DD hh[maxn][maxn][maxn];
DD vv[maxn][maxn][maxn];
DD zz[maxn][maxn][maxn];



DD merge(const DD &a,const DD &b){
	DD ret;
	ret.M=a.M+b.M;
	ret.x=a.x+(b.x-a.x)*b.M/(a.M+b.M);
	ret.y=a.y+(b.y-a.y)*b.M/(a.M+b.M);
	return ret;
}

int main(){
	freopen("B-small-attempt0(1).in","r",stdin);
	freopen("B-small-attempt0(1).out","w",stdout);
	//for(int i=0;i<500;i++) dd[i]=new DD[505][505];

	//for(int i=0;i<500;i++) delete dd[i];
	int cas,Te=1;
	scanf("%d",&cas);
	while( cas-- ){
		//**
		scanf("%d %d %d",&R,&C,&D);
		for(int i=R-1;i>=0;i--){
			scanf(" %s",mat[i]);
		}

		for(int i=0;i<R;i++){
			for(int j=0;j<C;j++){
				hh[i][j][1].M=D+mat[i][j]-'0';
				hh[i][j][1].x=i+0.5;
				hh[i][j][1].y=j+0.5;
				zz[i][j][1]=vv[i][j][1]=hh[i][j][1];
			}
		}
		for(int k=2;k<=max(C,R);k++){
			for(int i=0;i<R;i++){
				for(int j=0;j<C;j++){
					if( j+k-1 < C )
						hh[i][j][k]=merge(hh[i][j][k-1],hh[i][j+k-1][1]);
					if( i+k-1 < R )
						vv[i][j][k]=merge(vv[i][j][k-1],vv[i+k-1][j][1]);
					if( i+k-1 < R && j+k-1<C ){
						zz[i][j][k]=merge(zz[i][j][k-1],zz[i+k-1][j+k-1][1]);
						DD tmp=merge(hh[i+k-1][j][k-1],vv[i][j+k-1][k-1]);
						zz[i][j][k]=merge(tmp,zz[i][j][k]);
					}
				}
			}
		}

		int sum=0;
		for(int i=0;i<R;i++){
			for(int j=0;j<C;j++){
				for(int k=max(3,sum);k<=max(R,C);k++){
					if( i+k-1 < R && j+k-1 <C ){
						DD tmpH=merge(hh[i][j+1][k-2],hh[i+k-1][j+1][k-2]);
						DD tmpV=merge(vv[i+1][j][k-2],vv[i+1][j+k-1][k-2]);
						tmpH=merge(tmpH,tmpV);
						tmpH=merge(tmpH,zz[i+1][j+1][k-2]);
						if( fabs(tmpH.x-(i+k+i)/2.0) < 1e-5  &&
							fabs(tmpH.y-(j+k+j)/2.0) < 1e-5 ){
							sum=max(sum,k);
						}
					}
				}
			}
		}

		if( sum )
			printf("Case #%d: %d\n",Te++,sum);
		else 
			printf("Case #%d: IMPOSSIBLE\n",Te++);
	}
	return 0;
}
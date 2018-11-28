#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <cmath>
#include <cstring>
#include <memory.h>
#include <algorithm>
#define sqr(x) ((x)*(x))
#define min(a,b) ((a)<(b)?(a):(b))
#define max(a,b) ((a)>(b)?(a):(b))
#define abs(a) ((a)<0?(-(a)):(a))
#define swap(a,b) {typeof(a) t_=a; a=b; b=t_;}
#define For(i,a,b) for(int &i_=i=(a), e_=(b); i_<e_; ++i_)
#define cinar(m,n) for(int i_=0; i_<n; ++i_) cin>>m[i_];
#define in(x,l,r) ((x)>=(l) && (x)<=(r))
#define fill(m) memset(m,0,sizeof(m));
#define pi 3.141592653589793
#define y1 stupid_math
#define tm stupid_time
typedef long long int64;
typedef unsigned char byte;
using namespace std;

int T, ti;
int i,j,k,l,n,m,ii,jj,res;

int d;
char p[1000][1000];

double x,y,cx,cy,s,z;

int main(){
	freopen("input.txt","r",stdin); freopen("output.txt","w",stdout);
	
	cin>>T;
	for(ti=1;ti<=T;++ti){
		cin>>n>>m>>d;
		
		res=-1;
		for(i=0;i<n;++i) cin>>p[i];
		
		for(k=3;k<=min(n,m);++k){
			for(i=0;i<=n-k;++i)
			for(j=0;j<=m-k;++j){
				x=(k/2.)+i;
				y=(k/2.)+j;
				
				cx=cy=z=0;
				for(ii=i;ii<i+k;++ii)
				for(jj=j;jj<j+k;++jj) if(!(  (ii==i && jj==j)||(ii==i+k-1 && jj==j+k-1)||(ii==i && jj==j+k-1)||(ii==i+k-1 && jj==j) )){
					cx+=(0.5+ii)*(d+p[ii][jj]-'0');
					cy+=(0.5+jj)*(d+p[ii][jj]-'0');
					z+=(d+p[ii][jj]-'0');
				}
				cx/=z;
				cy/=z;
				if( abs(cx-x)<1e-6 && abs(cy-y)<1e-6) res = max(res,k);
			}
		}
		
		if(res<0)
		printf("Case #%d: IMPOSSIBLE\n",ti);
		else
		printf("Case #%d: %d\n",ti,res);
	}
	
	return 0;
}
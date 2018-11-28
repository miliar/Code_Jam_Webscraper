#include <vector>
#include <string>
#include <algorithm>
#include <cstdio>
using namespace std;

#define FOR(i) for(int i = 0;  i< 3; ++i)
typedef  long long int Int;
Int NT[3][3];
char buf[10000];

Int ntr(){
	gets(buf);
	for(int x = 0; x <3; ++x)for(int y = 0; y < 3; ++y)NT[x][y]=0;
	int n, A, B, C, D; Int M, x0,y0;
	sscanf(buf, "%d %d %d %d %d %lld %lld %lld",&n,&A,&B,&C,&D,&x0,&y0,&M);
	for( int i = 0;i < n;++i){
		NT[x0%3][y0%3]++;
	  	x0 = (A * x0 + B) % M;
	  	y0 = (C * y0 + D) % M;
  	}
  	Int TS = 0;
  	FOR(x0)FOR(x1)FOR(x2)FOR(y0)FOR(y1)FOR(y2){
		if( (x1 > x0 || x1==x0 && y1>=y0) && (x2 > x1 || x2==x1 && y2 >= y1)&&
			(x0+x1+x2) %3 == 0 && (y0+y1+y2)%3 == 0){
			if( x0 == x1 && y0 == y1 && x0 == x2 && y0 == y2){
				if( NT[x0][y0]>2 ){
					TS += (NT[x0][y0]*(NT[x0][y0]-1)*(NT[x0][y0]-2))/6;
				}
			} else if( x0 == x1 && y0 == y1 ){
				if( NT[x0][y0] > 1){
					TS += NT[x2][y2]*(NT[x0][y0]*(NT[x0][y0]-1))/2;
				}
			} else if( x0 == x2 && y0 == y2 ){
				if( NT[x0][y0] > 1){
					TS += NT[x1][y1]*(NT[x0][y0]*(NT[x0][y0]-1))/2;
				}
			} else if( x2 == x1 && y2 == y1 ){
				if( NT[x1][y1] > 1){
					TS += NT[x0][y0]*(NT[x1][y1]*(NT[x1][y1]-1))/2;
				}
			} else {
				TS += NT[x0][y0]*NT[x1][y1]*NT[x2][y2];
			}
			//fprintf(stderr,"%d %d %d %d %d %d : %d\n",x0,x1,x2,y0,y1,y2,TS);
		}
	}
	return TS;
}



int main(){
	freopen("Ain.txt","r",stdin);
	freopen("Aout.txt","w",stdout);

	int N;
	gets(buf); sscanf(buf,"%d", &N);

	for(int nc = 1; nc <= N; ++nc){
		fprintf(stderr,"%d / %d ",nc,N);
		Int r = ntr();
		printf( "Case #%d: %lld\n", nc, r);
	}
}

#include <iostream>
#include <algorithm>
using namespace std;
typedef long long LL;
#define REP(i,n) for(int i=0;i<n;i++)
#define FOR(a,b,c) for(int a=b;a<=c;a++)
#define MAXN 100005

LL n,A,B,C,D,x0,y0,M;

LL ile[9];

void generate(){
	LL X = x0,Y=y0;
	REP(i,n){
		ile[ (X%3)*3+Y%3 ]++;
		X = (A*X+B)%M;
		Y = (C*Y+D)%M;
	}
}
int main(){
	int d;
	scanf("%d",&d);
	REP(test,d){
		REP(i,9)ile[i]=0;
		scanf("%lld %lld %lld %lld %lld %lld %lld %lld",&n,&A,&B,&C,&D,&x0,&y0,&M);
		generate();
		LL res = 0;
		REP(i,9)if(ile[i]){
			int x1=i/3,y1=i%3;

			FOR(j,i,8)if(ile[j]){
				int x2=j/3,y2=j%3;

				FOR(k,j,8)if(ile[k]){
					int x3=k/3,y3=k%3;

					if( (x1+x2+x3)%3==0 && (y1+y2+y3)%3==0 ){
						if( i==j && j == k ){
							res += ile[i]*(ile[i]-1)*(ile[i]-2)/6;
						}else if( i == j ){
							res += ile[i]*(ile[i]-1)/2*ile[k];
						}else if( j == k ){
							res += ile[j]*(ile[j]-1)/2*ile[i];
						}else{
							res += ile[i]*ile[j]*ile[k];
						}
					}
				}
			}
		}
		printf("Case #%d: %lld\n",test+1,res);
	}
	return 0;
}

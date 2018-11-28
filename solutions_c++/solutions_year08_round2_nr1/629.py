#include <cstdlib>
#include <cstdio>
#include <cmath>
#include <cctype>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <queue>
#include <string>
#include <sstream>
#include <vector>
#include <map>
#include <bitset>

#define FOR(i,a,b) for(int i=a;i<b;i++)
#define REP(i,b) FOR(i,0,b)
#define sqr(a) ((a)*(a))

const double EPS=1e-5;
#define eq(a,b) (abs((a)-(b))<=EPS)

using namespace std;

char fin[]="a.in",fout[]="a.out";
const int NUM=10000;
__int64 n, a, b, c, d, xo, yo, m,res;
int o;
__int64 x[NUM],y[NUM];

int main(){
	freopen(fin,"r",stdin);
	freopen(fout,"w",stdout);
	scanf("%d",&o);
	REP(z,o){
		res=0;
		cin>>n>>a>> b>> c>> d>> xo>> yo>> m;
		x[0]=xo;y[0]=yo;
		FOR(i,1,n){
			x[i] = (a * x[i-1] + b) % m;
			y[i] = (c * y[i-1] + d) %m;
		}
		REP(i,n)
			FOR(j,i+1,n)
				FOR(k,j+1,n)
//				FOR(u,k+1,n)
		if(
						(((x[i]+x[j]+x[k])/3)*3==x[i]+x[j]+x[k])&&
						(((y[i]+y[j]+y[k])/3)*3==y[i]+y[j]+y[k])
						)
						res++;

		printf("Case #%ld: %ld\n",z+1,res);
	}
	exit(0);
}

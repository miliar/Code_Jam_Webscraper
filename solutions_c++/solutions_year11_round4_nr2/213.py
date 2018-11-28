//Jakub Sygnowski
#include<iostream>
#include<cstdio>
#include<cmath>
#include<cstdlib>
#include<algorithm>
#include<vector>
#include<string>
#include<list>
#include<map>
#include<set>
#include<queue>
#include<stack>
#include<utility>
#include<sstream>
//#include<gmp.h> // http://gmplib.org/
//#include<gmpxx.h>
using namespace std;
#define FOR(I,A,B) for(int I=(A);I<=(B);I++)
#define REP(I,N) for(int I=0;I<(N);I++)
#define ALL(X) (X).begin(),(X).end()
#define F first
#define S second
#define INF 1000000007
#define PB push_back
#define MP make_pair
typedef pair<int,int> PII;
typedef long long LL;

int t,r,c,d;
char tab[507][507];
bool odp;
int cx,cy;
LL sumx,sumy;
const inline void dodaj(const int &rx,const  int &ry,const int &w){
	sumx+=rx*w; sumy+=ry*w;
}
double sx,sy,ccx,ccy;
const inline void dodaj2(const double rx,const double ry,const int w){
	sx+=rx*w; sy+=ry*w;
}
bool dziala(int x,int y,int roz){
	if (roz%2){
	cx=x+(roz)/2; cy=y+(roz)/2;
	sumx=0LL; sumy=0LL;
	for(int iy=0;iy<roz;iy++) for(int ix=0;ix<roz;ix++){
		if (iy==0 && (ix==0 || ix==roz-1)) continue;
		if (ix==0 && (iy==0 || iy==roz-1)) continue;
		if (ix==roz-1 && iy==roz-1) continue;
		dodaj(cx-(x+ix),cy-(y+iy),tab[x+ix][y+iy]);
	}
//	printf("dla punktu %d %d i rozmiaru %d wektor wynosi %d %d\n",x,y,roz,sumx,sumy);
	return sumx==0LL && sumy==0LL;
	} else {
		sx=0.0; sy=0.0;
		ccx=x+(double)(roz-1)/2.0; ccy=y+(double)(roz-1)/2.0;
		for(int iy=0;iy<roz;iy++) for(int ix=0;ix<roz;ix++){
		if (iy==0 && (ix==0 || ix==roz-1)) continue;
		if (ix==0 && (iy==0 || iy==roz-1)) continue;
		if (ix==roz-1 && iy==roz-1) continue;
		dodaj2(ccx-(x+ix),ccy-(y+iy),tab[x+ix][y+iy]);
		}
		return abs(sx)<1E-7 && abs(sy)<1E-7;
	}
}
int main(){
	scanf("%d",&t);
	REP(nr,t){
		printf("Case #%d: ",nr+1);
		scanf("%d%d%d",&r,&c,&d);
		odp=false;
		REP(y,r) REP(x,c) scanf(" %c",&tab[x][y]);
		for(int rozm=(min(r,c));rozm>=3;rozm--){
			REP(y,1+r-rozm) REP(x,1+c-rozm){
				if (odp) break;
				if (dziala(x,y,rozm)){
					printf("%d\n",rozm);
					odp=true;
					break;
				}
			}
			if (odp) break;
		}
		if (!odp) printf("IMPOSSIBLE\n");
	}
}

#include <stdio.h>
#include <vector>
#include <algorithm>
#include <string>
#include <sstream>
#include <iostream>
#include <map>
#include <math.h>
#include <set>
#include <queue>
using namespace std;
typedef long long LL;
#define INF 1000000000
#define SZ(v) ((int)(v).size())
#define FOR(i,a,b) for(int i=(a);i<(b);i++)
#define REP(i,n) FOR(i,0,n)
#define FORE(i,a,b) for(int i=(a);i<=(b);i++) 



int main(){
	int T;
	scanf("%d",&T);
	FORE(t,1,T){
		int n,m,a;
		scanf("%d%d%d",&n,&m,&a);
		int X1,Y1,X2,Y2=1000,X3=0,Y3=0;
		
		FORE(x1,0,n){
			if(Y2!=1000) break;
			FORE(x2,0,n) FORE(y1,-m,m) FORE(y2,-m,m){
				int r = y2-y1;
				if(r>m || r<-m) continue;
				r = x1*y2-x2*y1;
				if(r<0) r= -r;
				if(r==a){
					X1 = x1;
					Y1 = y1;
					X2 = x2;
					Y2 = y2;
				}
			}
		}
		if(Y2==1000){
			printf("Case #%d: IMPOSSIBLE\n",t);
		}
		else{
			while(Y1<0 || Y2<0){
				Y1++;
				Y2++;
				Y3++;
			}
			printf("Case #%d: %d %d %d %d %d %d\n",t,X1,Y1,X2,Y2,X3,Y3);
		}
	}


}

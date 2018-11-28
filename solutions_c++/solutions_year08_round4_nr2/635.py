#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <sstream>
#include <string>
#include <set>
#include <map>
#include <algorithm>

using namespace std;

int m,n;
int A;
int x1,y1,x2,y2,x3,y3;

bool ok;

inline int mod(int d){
	if(d < 0) return -d;
	return d;
}

inline bool test(){
	if(x1 == x2 && y1 == y2) return false;
	if(x2 == x3 && y2 == y3) return false;
	if(x3 == x1 && y3 == y1) return false;
	if( mod((x1*y2+x2*y3+x3*y1) - (x2*y1+x3*y2+x1*y3)) == A) return true;
	return false;
}

void tenta(){
	
	if(ok) return ;
	
	for(x1=0;x1<=m;x1++){
		for(y1=0;y1<=n;y1++){
			for(x2=0;x2<=m;x2++){
				for(y2=0;y2<=n;y2++){
					if(test()){
						ok = true;
						return ;
					}
				}
			}
		}
	}
	
}

int main(){
	
	int t,lp;
	int r;
	int i,k;
	
	scanf("%d",&t);
	
	for(lp=1;lp<=t;lp++){
		scanf("%d %d %d",&m,&n,&A);
		ok = false;
		
		if(!ok){
			x3 = y3 = 0;
			tenta();
		}
		if(!ok){
			x3 = m;
			y3 = 0;
			tenta();
		}
		if(!ok){
			x3 = 0;
			y3 = n;
			tenta();
		}
		if(!ok){
			x3 = m;
			y3 = n;
			tenta();
		}
		
		printf("Case #%d: ",lp);
		
		if(ok) printf("%d %d %d %d %d %d\n",x1,y1,x2,y2,x3,y3);
		else printf("IMPOSSIBLE\n");
		
	}
	
	return 0;
	
}

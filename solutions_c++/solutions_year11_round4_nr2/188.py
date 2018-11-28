#include <map>        
#include <set>        
#include <queue> 
#include <cmath>       
#include <cstdio>      
#include <vector>        
#include <string>        
#include <sstream>       
#include <iostream>       
#include <algorithm>        
using namespace std;        
#define FOR(i,a,b) for(int i=(a); i<(b); ++i)        
#define FORE(it,x) for(typeof(x.begin()) it=x.begin(); it!=x.end(); ++it)        
#define SET(x, v) memset(x, v, sizeof (x))        
#define sz size()        
#define cs c_str()        
#define pb push_back        
#define mp make_pair       
    
typedef long long ll;        
char dat[512][512];
bool pos(int x, int y, int z) {
	int ver = 0, hor = 0;
	FOR(i,0,z) {
		FOR(j,0,z) {
			if(i==0&&(j==0 || j==z-1))continue;
			if(i==z-1&&(j==0||j==z-1)) continue;
			
			if(i < z/2) ver += (dat[x+i][y+j]-'0') * (z/2 - i);
			if(i > (z-1)/2) ver -= (dat[x+i][y+j]-'0') * (i - (z-1)/2);
			if(j < z/2) hor += (dat[x+i][y+j]-'0') * (z/2 - j);
			if(j > (z-1)/2) hor -= (dat[x+i][y+j]-'0') * (j - (z-1)/2);
		}
	}
	//if(z==5)printf("(%d, %d, %d): %d %d\n", x, y, z, ver, hor);
	return ver == 0 && hor == 0;
}
int main() {
	int e= 0, T;
	scanf("%d",&T);
	while(T--) {
		int r, c, d;
		scanf("%d%d%d",&r,&c,&d);
		FOR(i,0,r)
			scanf(" %s",dat[i]);
			
		for(int k = min(r, c); k >= 3;--k) {
			FOR(i,0,r) {
				if(i+k > r) break;
				FOR(j,0,c) {
					if(j+k > c) break;
					if(pos(i, j, k)) {
						printf("Case #%d: %d\n", ++e, k);
						goto p1;
					}
				}
			}
		}
		printf("Case #%d: IMPOSSIBLE\n", ++e);
		continue;
		p1:;
	}
	return 0;
}
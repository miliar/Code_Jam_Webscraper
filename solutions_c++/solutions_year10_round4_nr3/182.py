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
#define FS first
#define SD second
#define MOD 100003

int M[200][200];
int main(){
	int T;
	scanf("%d",&T);
	FORE(test,1,T){
		int n;
		scanf("%d",&n);
		FOR(i,0,200) FOR(j,0,200) M[i][j] = 0;
		FOR(i,0,n){
			int x1,y1,x2,y2;scanf("%d%d%d%d",&x1,&y1,&x2,&y2);
			FORE(a,x1,x2) FORE(b,y1,y2) M[a][b] = 1;
		}
		int ret = -1;
		while(true){
			bool ok = false;
			ret++;
			for(int i = 190;i>=1;i--) for(int j=190;j>=1;j--){
				if(M[i][j]){
					ok = true;
					if(!M[i-1][j] && !M[i][j-1]) M[i][j] = 0;
				}
				else if(M[i-1][j] && M[i][j-1]) M[i][j] = 1;
			}
			
			if(!ok) break;
		}
		printf("Case #%d: %d\n",test,ret);
	}

}

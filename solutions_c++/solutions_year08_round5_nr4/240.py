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


int mem[1000][1000];
bool ok[1000][1000];
int moves[][2]={{1,2},{2,1}};

int main(){
	int T;
	scanf("%d",&T);
	FORE(t,1,T){
		int h,w,r;
		scanf("%d%d%d",&h,&w,&r);
		
		for(int i=0;i<=h;i++) for(int j=0;j<=w;j++){
			ok[i][j]=true;
			mem[i][j]=0;
		}
		
		for(int i=0;i<r;i++){
			int x,y;
			scanf("%d%d",&x,&y);
			ok[x][y]=false;
		}
		mem[1][1]=true;
		for(int i=1;i<=h;i++){
			for(int j=1;j<=w;j++){
				for(int z=0;z<2;z++){
					int x = i+moves[z][0];
					int y = j+moves[z][1];
					if(x>h || y>w) continue;
					if(!ok[x][y]) continue;
					mem[x][y] = (mem[i][j]+mem[x][y])%10007;
				}
			}
		}
		printf("Case #%d: %d\n",t,mem[h][w]);
		
	}
}

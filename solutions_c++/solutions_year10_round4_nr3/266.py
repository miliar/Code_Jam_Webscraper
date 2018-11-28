#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
using namespace std;

#define BIT(X,B) (((X)>>(B))&1)
#define SET(X,B) ((X)|(1<<(B)))
#define CLR(X,B) ((X)&(~(1<<(B))))
#define REV(X,B) ((X)^(1<<(B)))

const int Max=128;
bool b[2][Max][Max];
bool proc(bool (*pre)[Max],bool (*cur)[Max]){
	bool live=false;
	for(int i=0;i<Max;++i){
		for(int j=0;j<Max;++j){
			if(pre[i][j]) cur[i][j]=pre[i-1][j]||pre[i][j-1];
			else cur[i][j]=pre[i-1][j]&&pre[i][j-1];
			if(cur[i][j]) live=true;
		}
	}
	return live;
}
int main(){
	int TT;
	scanf("%d",&TT);
	for(int cas=1;cas<=TT;++cas){
		int R;
		bool (*pre)[Max]=b[1],(*cur)[Max]=b[0];
		memset(cur,0,sizeof(b[0]));
		scanf("%d",&R);
		for(int i=0;i<R;++i){
			int x1,y1,x2,y2;
			scanf("%d %d %d %d",&x1,&y1,&x2,&y2);
			for(int x=x1;x<=x2;++x){
				for(int y=y1;y<=y2;++y)
				    cur[x][y]=true;
			}
		}
		int round=0;
		do{
			++round;
			swap(cur,pre);
		}while(proc(pre,cur));
		printf("Case #%d: %d\n",cas,round);
	}
	return 0;
}

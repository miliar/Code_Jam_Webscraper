#include <iostream>
#include <algorithm>
#include <cstring>
#include <climits>
#include <cmath>
#include <string>
#include <vector>
#include <queue>
#include <set>
using namespace std;
bool G[2][105][105];
int main() {
	int T;
	scanf("%d",&T);
	for(int cn=1;cn<=T;++cn) {
		int R;
		scanf("%d",&R);
		memset(G,0,sizeof(G));
		for(int i=0;i<R;++i) {
			int x1,y1,x2,y2;
			scanf("%d%d%d%d",&x1,&y1,&x2,&y2);
			for(int y=y1;y<=y2;++y)
				for(int x=x1;x<=x2;++x)
					G[0][y][x] = 1;
		}
		bool f = 0;
		for(int t=1;;++t) {
			f = !f;
			bool fail = 0;
			for(int y=1;y<=100;++y)
				for(int x=1;x<=100;++x) {
					if(G[!f][y-1][x] && G[!f][y][x-1]) G[f][y][x] = 1;
					else if(!G[!f][y-1][x] && !G[!f][y][x-1]) G[f][y][x] = 0;
					else G[f][y][x] = G[!f][y][x];
					if(G[f][y][x]) fail = 1;
				}
			if(!fail) {
				printf("Case #%d: %d\n",cn,t);
				break;
			}
		}
	}
}

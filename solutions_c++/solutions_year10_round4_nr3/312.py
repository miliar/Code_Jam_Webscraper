#include <cstdio>
#include <set>
#include <utility>
using namespace std;
typedef pair<int,int> ii;

bool S[2][200][200];
int main() {
	freopen("C-small-attempt0.in","r",stdin);
	int tn;
	scanf("%d", &tn);
	for(int cc=1;cc<=tn;++cc) {
		int R;
		scanf("%d", &R);	
		set<ii> S;
		for(int i=0;i<R;++i) {
			int x1, x2, y1, y2;
			scanf("%d %d %d %d", &x1, &y1, &x2, &y2);
			for(int x=x1;x<=x2;++x) for(int y=y1;y<=y2;++y) S[0][x][y] = true;
		}
		set<ii> Q;
		int ret = 0;
		for(;!S.empty();++ret) {
			Q.clear();
			for(int x=-100;x<=100;++x) for(int y=-100;y<=100;++y) {
				if( S.find(ii(x,y)) == S.end() ) {
					if( S.find(ii(x-1,y)) != S.end() && S.find(ii(x,y-1)) != S.end() ) 
						Q.insert(ii(x,y));
				}
				else {
					if( !(S.find(ii(x-1,y)) == S.end() && S.find(ii(x,y-1)) ==S.end()) ) 
						Q.insert(ii(x,y));
				}
			}
			S = Q;
		}
		printf("Case #%d: %d\n", cc, ret);
	}
}


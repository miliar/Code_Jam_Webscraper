#include <iostream>
#include <deque>
#include <vector>
#include <assert.h>
using namespace std;

const int maxn = 2010;
const int maxm = 2010;

int n,m;
bool malt[maxn];
deque< vector<int> > ul;
//int ml[maxm];
deque< int > ml;

int main() {
	int C;
	scanf("%d", &C);
	for(int c=0;c<C;c++) {
//		cerr<< "test: " <<c<<endl;
		memset(malt, 0, sizeof(malt));
		ml.clear();
		ul.clear();
		scanf("%d%d", &n,&m);
		for(int i=0;i<m;i++) {
			int t;
			scanf("%d", &t);
			vector<int> p;
			int mlx = 0;
			for(int j=0;j<t;j++) {
				int x,y;
				scanf("%d%d", &x,&y);
				if(y==1) {
					mlx = x;
				} else {
					p.push_back(x);
				}
			}
			if(mlx>0) {
				if(find(p.begin(), p.end(), mlx)!=p.end()) {
					continue;
				}
			}
			ul.push_back(p);
			ml.push_back(mlx);
		}

		bool imposs = false;

		for(int remain=ml.size()+2;remain>=0 && ml.size()>0;remain--) {
			vector<int> p = ul.front();
			ul.pop_front();
			int mlx = ml.front();
			ml.pop_front();
			if(mlx>0 && malt[mlx]) {
				continue;
			}
			bool conti = false;
			for(int i=0;i<p.size();i++) {
				if(!malt[p[i]]) {
					conti = true;
					break;
				}
			}
			if(!conti) {
				if(mlx==0) {
//					cerr<<"mlx:"<<mlx<<endl;
					imposs = true;
					break;
				}
				assert(!malt[mlx]);
				malt[mlx] = true;
				remain = ul.size()+2;
				continue;
			}
			ml.push_back(mlx);
			ul.push_back(p);
		}

		printf("Case #%d:", c+1);
		if(imposs) {
			printf(" IMPOSSIBLE\n");
		} else {
			for(int i=1;i<=n;i++) {
				int x = malt[i]?1:0;
				printf(" %d", x);
			}
			printf("\n");
		}
	}
	return 0;
}


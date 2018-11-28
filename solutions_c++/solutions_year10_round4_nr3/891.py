#include <cstdio>
#include <set>
#include <map>
#include <algorithm>
using namespace std;

typedef pair<int,int> pii;
typedef set<pii> spii;

#define rep(i, a, b) for(int i = (a); i < (b); ++i)
#define trav(it, v) for(typeof((v).begin()) it = (v).begin(); \
                        it != (v).end(); ++it)

int main() {
	int T;
	scanf("%d",&T);
	for(int t=0;t<T;++t) {
		int R;
		scanf("%d",&R);
		spii alive;
		for(int r=0;r<R;++r) {
			int X1,X2,Y1,Y2;
			scanf("%d%d%d%d",&X1,&Y1,&X2,&Y2);
			for(int x=X1;x<=X2;++x)
				for(int y=Y1;y<=Y2;++y)
					alive.insert(pii(x,y));
		}
		spii die, born;
		trav(it, alive) {
			if(alive.count(pii(it->first+1, it->second-1)) && !alive.count(pii(it->first+1, it->second)))
				born.insert(pii(it->first+1, it->second));
			if(!alive.count(pii(it->first, it->second-1)) && !alive.count(pii(it->first-1, it->second)))
				die.insert(*it);
		}
		spii die2, born2;
		int time = 0;
		while(!alive.empty()) {
			time++;
//			alive.erase(die.begin(),die.end());
			set_difference(alive.begin(), alive.end(), die.begin(), die.end(), inserter(die2, die2.begin()));
			alive.swap(die2);
			die2.clear();
			alive.insert(born.begin(),born.end());
			trav(it, born) {
				if(alive.count(pii(it->first+1, it->second-1)) && !alive.count(pii(it->first+1, it->second)))
					born2.insert(pii(it->first+1, it->second));
				if(alive.count(pii(it->first-1, it->second+1)) && !alive.count(pii(it->first, it->second+1)))
					born2.insert(pii(it->first, it->second+1));
			}
			trav(it, die) {
				if(!alive.count(pii(it->first-1, it->second+1)) && alive.count(pii(it->first, it->second+1)))
					die2.insert(pii(it->first, it->second+1));
				if(!alive.count(pii(it->first+1, it->second-1)) && alive.count(pii(it->first+1, it->second)))
					die2.insert(pii(it->first+1, it->second));
			}
			die.swap(die2);
			born.swap(born2);
			born2.clear();
			die2.clear();
		}
		printf("Case #%d: %d\n",t+1, time);
	}
}
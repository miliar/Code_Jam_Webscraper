#include <cstdio>
#include <vector>
#include <algorithm>
#include <map>

using namespace std;

typedef long long ll;


int main(){
	int lz;
	scanf("%d", &lz);
	for(int cnt = 1; cnt <= lz; cnt++){
		int n;
		scanf("%d", &n);
		map<ll, int> cor;
		for(int i = 0; i < n; i++){
			ll pos;
			int pe;
			scanf("%lld %d", &pos, &pe);
			cor[pos] = pe;
		}
		ll ret = 0;
		bool zle = 1;
		while(zle){
			zle = 0;
			map<ll, int>::iterator it = cor.begin();
			while(it != cor.end()){
				if((*it).second > 1){
					zle = 1;
					int x = (*it).second/2;
					ret += x;
					ll p0 = (*it).first;
					ll p1 = p0-1;
					ll p2 = p1+2;
					cor[p0] -= 2*x;
					cor[p1] += x;
					cor[p2] += x;
					break; 
				}
				it++;
			}
		}
		printf("Case #%d: %lld\n",cnt, ret);

	}
	return 0;
}

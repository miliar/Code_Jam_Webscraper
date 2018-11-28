#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <queue>
#include <cmath>
#include <algorithm>

using namespace std;

int googlers[200], pode[200], n, p, s;

int main(){
	int casos; scanf("%d", &casos);
	int caso = 0, at;
	while(casos--){ ++caso;
		int total = 0;
		scanf("%d%d%d", &n, &s, &p);
		for(int i = 0; i < n; ++i){
			scanf("%d", &at);
			googlers[i] = at;
		}
		sort(googlers, googlers+n, greater<int>());
		for(int i = 0; i < n; ++i){
			if(googlers[i] >= p*3-2){
				++total;
			} else if (googlers[i]+3 >= p*3-1 && googlers[i] >= 2 && s){
				++total;
				--s;
			}
		}
		
		printf("Case #%d: %d\n", caso, total);
		
	}
	
	return 0;
}
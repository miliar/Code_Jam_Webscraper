#include <cstdio>
#include <algorithm>

using namespace std;

char buf[256];

int main(){
	int tcN;
	scanf("%d", &tcN);
	for(int tc=0; tc<tcN; ++tc){
		int sum = 0, x=0, m=123456, n, t;
		scanf("%d", &n);
		while(n--){
			scanf("%d", &t);
			x ^= t;
			sum += t;
			m = min(m, t);
		}
		if(!x){
			printf("Case #%d: %d\n", tc+1, sum-m);
		}else{
			printf("Case #%d: NO\n", tc+1);
		}
	}
}

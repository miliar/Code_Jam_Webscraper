#include <cstdio>
using namespace std;

int main(){
	int T;
	scanf("%d",&T);
	for(int c=1; c<=T; c++){
		int N, x, cnt=0;
		scanf("%d",&N);
		for(int i=1; i<=N; i++){
			scanf("%d",&x);
			if(x!=i) cnt++;
		}
		printf("Case #%d: %.9f\n", c, (double)cnt);
	}
	return 0;
}

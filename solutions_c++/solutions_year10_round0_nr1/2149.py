#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

int main(){
	int lz;
	scanf("%d", &lz);
	for(int i = 0; i < lz; i++){
		int n, k;
		scanf("%d%d", &n, &k);
		if(k&(1<<(n-1))) printf("Case #%d: ON\n", i+1);
		else printf("Case #%d: OFF\n", i+1);
	}
	return 0;
}

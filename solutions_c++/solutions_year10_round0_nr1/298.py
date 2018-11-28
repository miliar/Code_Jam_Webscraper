#include <iostream>
using namespace std;

int n, k;

int main(){

	//freopen("test", "r", stdin);
	//freopen("out", "w", stdout);
	int cases, c = 0;
	scanf("%d", &cases);
	while(cases--){
		scanf("%d %d", &n, &k);
		k = k % (1<<n);
		if(k == (1<<n)-1)	printf("Case #%d: ON\n", ++c);
		else				printf("Case #%d: OFF\n", ++c);
	}
	return 0;
}

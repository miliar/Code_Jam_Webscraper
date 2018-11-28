#include <iostream>
#include <vector>
#include <cstdio>
using namespace std;
typedef double lf;

int tests, n, a, diff;

int main(){
	scanf("%d",&tests);
	for(int test=1; test<=tests; test++){
		scanf("%d",&n);
		diff=0;
		for(int i=1; i<=n; i++){
			scanf("%d",&a);
			if(a!=i) diff++;
		}
		printf("Case #%d: %d.000000\n",test,diff);
	}
}

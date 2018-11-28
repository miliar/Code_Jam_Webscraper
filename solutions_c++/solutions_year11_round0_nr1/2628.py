#include <cstdio>
#include <algorithm>

using namespace std;

int main(){
	int tcN;
	scanf("%d", &tcN);
	for(int tc=0; tc<tcN; ++tc){
		int pb=1, po=1, tb=0, to=0, n, d, t, sum=0;
		char c[10];
		scanf("%d", &n);
		for(int i=0; i<n; ++i){
			scanf("%s", c);
			scanf("%d", &t);
			if(c[0] == 'O'){
				d = abs(po - t);
				sum = max(sum, to + d) + 1;
				to = sum;
				po = t;
			}else{
				d = abs(pb - t);
				sum = max(sum, tb + d) + 1;
				tb = sum;
				pb = t;
			}
		}
		printf("Case #%d: %d\n", tc+1, sum);
	}

}

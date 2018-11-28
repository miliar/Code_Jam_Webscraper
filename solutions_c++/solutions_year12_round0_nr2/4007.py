#include <iostream>
#include <vector>
#include <math.h>

using namespace std;

int store(int t){
	if (t%3 == 0)
		    return t/3;
		return t/3+1;
}

int sup(int t){
	int n = t/3;
		if (t%3 == 2){
			if (n+2 > 10)
				return -1;
			return n+2;
		}
		if (n-1 < 0 || n+1 > 10)
			return -1;
		return n+1;
}



int main() {
	int T;
	scanf("%d", &T);
	int cases = 0;
	while(T--) {
		cases++;
		int ret = 0;
		int N, S, p;
		scanf("%d %d %d", &N, &S, &p);
		for(int i=0; i < N; i++) {
			int temp;
			scanf("%d", &temp);
			if(store(temp) >= p) {
				ret++;
			} else {
				if(sup(temp) >= p && S > 0) {
					ret++;
					S--;
				}
			}
		}
		printf("Case #%d: %d\n",cases, ret);
	}
    return 0;
}
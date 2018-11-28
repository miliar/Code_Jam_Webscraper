#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

int main(){
	int tc, tcn;
	scanf("%d", &tcn);
	for(tc=0; tc<tcn; ++tc){
		int o=0, m=0, n, p, t, s;
		scanf("%d %d %d", &n, &s, &p);
		int b0 = p*3-2;
		int b1 = p*3-4;
		b1 = max(b1, 2);
		for(int i=0; i<n; ++i){
			scanf("%d", &t);
			if(t >= b0)
				++o;
			else if(t >= b1)
				++m;
		}
		printf("Case #%d: %d\n", tc+1, o + min(m, s));
	}
}


#include <cstdio>

int min(int a, int b){
	return (a < b) ? a : b;
}
int main(){
	
	int testcase; scanf("%d", &testcase);
	int pos[10000];
	int len[10000];
	int r[10000];

	for(int t=1; t<=testcase; ++t){
		int n; scanf("%d", &n);
		for(int i=0; i<n; ++i){
			scanf("%d %d", &pos[i], &len[i]);
		}
		int d; scanf("%d", &d);
		int x;
		r[0] = pos[0];
		for(int i=1; i<n; ++i){
			r[i] = -1;
			for(int j=0; j<i; ++j){
				if(r[j] >= pos[i]-pos[j]){
					x = min(pos[i]-pos[j], len[i]);
					if(x > r[i]){
						r[i] = x;
					}
				}
			}
		}
		//printf("%d %d %d\n", r[n-1], pos[n-1], d);
		int ans = 0;
		for(int i=0; i<n; ++i){
			if(r[i] != -1 && r[i]+pos[i] >= d){
				//printf("%d %d %d\n", i, r[i], pos[i]);
				ans = 1;
				break;
			}
		}
		printf("Case #%d: ", t);
		if(ans == 0){
			printf("NO\n");
		}else{
			printf("YES\n");
		}
	}
	return 0;
}

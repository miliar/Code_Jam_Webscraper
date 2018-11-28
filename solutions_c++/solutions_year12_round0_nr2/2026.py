#include <stdio.h>
int t[110], use[110];
int main(){
	int c, n, s, p;
	scanf("%d", &c);
	for(int i=1;i<=c;++i){
		scanf("%d%d%d", &n, &s, &p);
		for(int j=0;j<n;++j){
			scanf("%d", &t[j]);
			use[j] = -1;
		}
		int max = 0;
		if(p == 0) max = n;
		else if(p == 1){
			for(int j=0;j<n;++j){
				if(t[j] >= p*3-2){
					++max;
				}
			}
		}
		else{
			for(int j=0;j<n;++j){
				if(t[j] >= p*3-2){
					++max;
					use[j] = 1;
				}
			}
			for(int j=0, cnt=0;j<n && cnt<s;++j){
				if(use[j] == -1 && (t[j] == p*3-4 || t[j] == p*3-3)){
					use[j] = 1;
					++max;
					++cnt;
				}
			}
		}
		printf("Case #%d: %d\n", i, max);
	}
	return 0;
}

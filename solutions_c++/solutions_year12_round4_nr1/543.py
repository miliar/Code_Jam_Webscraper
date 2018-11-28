#include <stdio.h>
#include <algorithm>
using namespace std;
int d[10000], l[10000];
int t[10000];
int main(){
	int T;
	scanf("%d", &T);
	for(int TT = 1; TT <= T; TT++){
		int n, D;
		scanf("%d", &n);
		for(int i = 0; i < n; i++){
			scanf("%d%d", &d[i], &l[i]);
		}
		scanf("%d", &D);
		
		t[0] = 2*d[0];
		
		int last = 0;
		bool ok = false;
		for(int i = 1; i < n; i++){
			while(last < i){
				if(t[last] >= d[i]){
					t[i] = d[i] + min(d[i] - d[last], l[i]);
					if(t[i] >= D){
						ok = true;
					}
					break;
				}else{
					last++;
				}
			}
			if(last == i)
				break;
		}
		if(t[0] >= D)
			ok = true;
		printf("Case #%d: ", TT);
		if(ok){
			printf("YES\n");
		}else{
			printf("NO\n");
		}
	}
}
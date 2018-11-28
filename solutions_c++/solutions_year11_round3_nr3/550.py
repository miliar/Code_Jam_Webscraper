#include<iostream>
using namespace std;

int input[110];

int main(){
	int cas;
	freopen("C.in", "r", stdin);
	freopen("C.out", "w", stdout);
	scanf("%d", &cas);
	for(int t = 0; t < cas; t++){
		int n, l, h, i;
		scanf("%d%d%d", &n, &l, &h);
		for(i = 0; i < n; i++)
			scanf("%d", &input[i]);
		bool chk = 1;
		int pos = 0;
		for(i = l; i <= h; i++){
			int j;
			for(j = 0; j < n; j++){
				if((i % input[j] != 0) && (input[j] % i != 0)){
					break;
				}
			}
			if(j == n) {pos = i; break;}
		}
		if(i == h + 1) printf("Case #%d: NO\n", t + 1);
		else printf("Case #%d: %d\n", t + 1, pos);
	}
	return 0;
}
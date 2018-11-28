#include <stdio.h>

int abs(int a){
	if( a < 0 ) return -a;
	return a;
}

int main(){
	int T;
	scanf("%d", &T);
	for( int t = 1; t <= T; t++ ){
		int ans = 0;
		char ob[] = {'O', 'B'};
		char pob = 0;
		int ploc[] = {1, 1};
		int prev = 0;
		int P;
		scanf("%d", &P);
		while(P--){
			char color[5];
			int button;
			scanf("%s %d", color, &button);
			for( int j = 0; j < 2; j++ ){
				if( ob[j] == color[0] ){
					int cur = abs( button - ploc[j] );
					if( ob[j] == pob ){
						ans += cur;
						prev += cur;
					}
					else{
						cur -= prev;
						if( cur < 0 ) cur = 0;
						ans += cur;
						prev = cur;
					}
					pob = ob[j];
					ploc[j] = button;
					ans++;
					prev++;
				}
			}
		}
		printf("Case #%d: %d\n", t, ans);
	}
	return 0;
}

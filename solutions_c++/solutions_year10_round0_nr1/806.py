#include <cstdio>

int main(){
	int n, k, t;
	bool on;
	
	scanf("%d",&t);
	
	for (int tt=1; tt<=t; tt++){
		scanf("%d%d",&n,&k);
		
		on = true;
		
		for (int i=0; i<n; i++){
			on = on && ( (k&1) == 1 );
			k >>= 1;
		}
		
		if ( on == true ) printf("Case #%d: ON\n", tt);
		else printf("Case #%d: OFF\n", tt);
	}

	return 0;
}

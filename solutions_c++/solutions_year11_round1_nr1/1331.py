// kronig 	thiagokronig@gmail.com

#include <cstdio>

int main() {

	int tt;
	int T;
	
	scanf("%d", &T);
	
	for (tt=1; tt<=T; tt++) {

		int n, pd, pg;
		int broken;
		scanf("%d %d %d", &n, &pd, &pg);
		
		if ((pg == 100 && pd != 100) || (pg == 0 && pd != 0)) {
			broken = true;
		} 
		
		else if (( pg == 100 && pd == 100) || (pg == 0 && pd == 0)) {
			broken = false;
		}
		
		else {	
			int i,j,x;
			broken = true;
			for (i=1; i<=n && broken; i++) {
				x = i * pd;
				broken = (x % 100) != 0; // nao é inteiro
			}
		}
		
		if (broken) 
			printf("Case #%d: Broken\n", tt);
		else
			printf("Case #%d: Possible\n", tt);
	}

	return 0;
}
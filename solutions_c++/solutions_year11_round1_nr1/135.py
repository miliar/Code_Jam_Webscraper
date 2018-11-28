#include<stdio.h>
#include<string.h>
#include<stdlib.h>

int gcd(int a, int b){
	return b? gcd(b, a%b) : a;
}

int main(){
	//freopen("in.txt", "r", stdin);
	//freopen("out.txt", "w", stdout);

	int test, pd, pg;
	int da, db, ga, gb;
	int n, r;
	scanf("%d", &test);
	for(int t=1; t<=test; t++){
		scanf("%d %d %d", &n, &pd, &pg);
		da = pd, db = 100 - pd;
		ga = pg, gb = 100 - pg;
		r = gcd(da, db);
		da /= r, db /= r;
		r = gcd(ga, gb);
		ga /= r, gb /= r;
		printf("Case #%d: ", t);
		if(da + db > n){
			printf("Broken\n");
			continue;
		}
		if((0==ga&&0!=da) || (0==gb&&0!=db)){
			printf("Broken\n");
			continue;
		}
		printf("Possible\n");
	}
	fclose(stdout);
	return 0;
}
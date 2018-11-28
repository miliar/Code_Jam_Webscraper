#include <cstdio>

int num, n, k;

int main (){
	scanf("%d", &num);
	for(int casenum = 0; casenum < num; ++casenum){
		scanf("%d%d", &n, &k);
		printf("Case #%d: ", casenum+1);
		int t = k % (1 << n);
		if(t == (1 << n) - 1) printf("ON\n");
		else printf("OFF\n");
	}
	return 0;
}

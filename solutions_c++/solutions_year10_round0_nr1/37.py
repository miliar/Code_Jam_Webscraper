#include <cstdio>

int main() {
    int t;
    scanf("%d", &t);
    for(int casenum = 1; casenum <= t; casenum++) {
	int n, k;
	scanf("%d", &n);
	scanf("%d", &k);
	printf("Case #%d: ", casenum);
	int a = (1 << n);
	if(k % a == a - 1)
	    printf("ON\n");
	else
	    printf("OFF\n");
    }
}

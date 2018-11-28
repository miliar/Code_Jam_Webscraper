#include <cstdio>

int main(){
    int t, l, p, c;

    scanf("%d", &t);
    for (int icas = 1; icas <= t; icas ++){
	scanf("%d %d %d", &l, &p, &c);

	int s = 0;
	long long L = l;
	while (L < p){
	    s ++;
	    L *= c;

	}
	int a, b;
	b = s;
	int ans = 0;

	while (b > 1){
	    a = b / 2;
	    b = b - a;
	    ans ++;
	}
	printf("Case #%d: %d\n", icas, ans);
    }
    return 0;
}
	

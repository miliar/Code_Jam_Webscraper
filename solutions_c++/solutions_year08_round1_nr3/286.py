#include <cstdio>
#include <algorithm>


int f(int n){
    int a = 2, b = 6;
    int c;
    for (int i = 2; i <= n; i ++){
	c = (6 * b - 4 * a + 4 * 10000) % 10000;
	a = b;
	b = c;
    }
    return c;
}
	
int main(){
    
    int t;
    int n;
    
    scanf("%d", &t);
    for (int cas = 1; cas <= t; cas ++){
	scanf("%d", &n);
	printf("Case #%d: %03d\n", cas, (f(n) - 1 + 10000) % 10000 % 1000);
    }
    return 0;
}

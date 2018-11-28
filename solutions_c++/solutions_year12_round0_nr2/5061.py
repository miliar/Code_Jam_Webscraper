#include <stdio.h>
#include <string.h>

int main() {
    int numT; scanf("%d ", &numT);
    
    char instr[200];
    for(int cno = 1; cno <= numT; cno++) {
    	int n, s, p;
    	scanf("%d %d %d", &n, &s, &p);
    	int ans = 0;
    	int t20 = 0;
    	for(int i = 0; i < n; i++) {
	   int k;
	   scanf("%d", &k);
	   if(k >= 3*(p-1) + 1) ans++;
	   else {
	   	int v = 3*(p-2)+2;
	   	if(v < n) v = n;
	   	if(k >= v) t20++;
	  }
    	}
    	if(t20 < s) ans += t20;
    	else ans += s;
    	printf("Case #%d: %d\n", cno, ans);
    }
    
    return 0;
}

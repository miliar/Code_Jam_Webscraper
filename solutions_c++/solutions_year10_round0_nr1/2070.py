#include <stdlib.h>
#include <stdio.h>
#include <string.h>
/*
 * 
 */
int main() {
    int t = 0;
    
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    
	scanf("%d",&t);
	for(int i = 1;i <= t;i++)
    {
        int n,k;
        scanf("%d %d",&n,&k);
        int tmp = 1 << (n);
        int d = k % tmp;
        printf("Case #%d: ",i);
        if(d == tmp-1)  puts("ON");
        else    puts("OFF");
    }
    return 0;
}

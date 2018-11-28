/* 
 * File:   main.cpp
 * Author: ubuntu
 *
 * Created on 2010年5月9日, 上午1:35
 */

#include <stdlib.h>
#include <stdio.h>
#include <string.h>

int main() {
		freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);


    int n,k;
    int ans;
    int t;
    scanf("%d",&t);
    for(int c = 1;c <= t;c ++)
    {
        scanf("%d%d",&n,&k);
        printf("Case #%d: ",c);
        ans = 1 << n;
        if(k % ans == ans - 1)printf("ON\n");
        else printf("OFF\n");

    }
    return 0;
}


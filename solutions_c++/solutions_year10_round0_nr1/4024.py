/* 
 * File:   main.cpp
 * Author: ubuntu
 *
 * Created on 2010年5月9日, 上午1:27
 */

#include <stdlib.h>
#include<stdio.h>
/*
 * 
 */
int main(int argc, char** argv) {
    int n,k;
    int T;
    int CS=1;
    scanf("%d",&T);
    while(T--)
    {
        scanf("%d%d",&n,&k);
        int m=1<<n;
        k%=m;
        printf("Case #%d: ",CS++);
        if(k==m-1)
            puts("ON");
        else puts("OFF");
    }
    return (EXIT_SUCCESS);
}

/*
4
1 0
1 1
4 0
4 47

Case #1: OFF
Case #2: ON
Case #3: OFF
Case #4: ON
 */


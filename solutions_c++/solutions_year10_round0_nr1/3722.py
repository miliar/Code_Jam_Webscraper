/* 
 * File:   snapper.cpp
 * Author: Jiangwei Yu
 *
 * Created on May 8, 2010, 4:57 PM
 */

#include <stdlib.h>
#include <stdio.h>

/*
 * 
 */
int main() {
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);
    int task;
    scanf("%d", &task);
    for (int tn = 1; tn <= task; tn++)
    {
        int N, K;
        printf("Case #%d: ", tn);
        scanf("%d %d", &N, &K);
        int m = (1<<N);
        K = K % m;
        if (K == m-1)
        {
            printf("ON\n");
        }else
        {
            printf("OFF\n");
        }
    }
    return 0;
}


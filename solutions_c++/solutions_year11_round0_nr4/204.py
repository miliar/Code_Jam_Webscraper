/* 
 * File:   main.cpp
 * Author: Prowindy
 *
 * Created on 2011年5月7日, 下午2:21
 */

#include <stdlib.h>
#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <algorithm>
#include <set>
#include <math.h>
#include <string.h>
#include <iostream>
#include <sstream>
#include <vector>
using namespace std;
/*
 * 
 */
int A[2000],B[2000];
bool cmp(int i,int j){
    return A[i]<A[j];
}
int main(int argc, char** argv) {
    int tt,cas = 1,i;
    freopen("D-large.in", "r", stdin);
    freopen("C.out", "w", stdout);
    scanf("%d",&tt);
    while(tt--){
        int N;
        scanf("%d",&N);
        for (i=0;i<N;i++)
            scanf("%d",&A[i]),B[i] = A[i];
        sort(A,A+N);
        double sum = 0;
        for (i=0;i<N;i++)
            if (A[i]!=B[i])
                sum++;
        printf("Case #%d: %.6lf\n", cas++,sum);
    }
    return (EXIT_SUCCESS);
}


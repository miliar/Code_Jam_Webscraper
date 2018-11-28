/* 
 * File:   A.cc
 * Author: GongZhi
 * Problem:
 * Created on 2010年5月8日, 下午1:16
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <queue>
#include <algorithm>
using namespace std;

/*
 *
 */
bool di(int n,int k){
    long long t=1<<n;
    k%=t;
    if(k==t-1)return true;
    else return false;
}
int main() {
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int kase;
    int kases=1;
    int n,k;
    scanf("%d",&kase);
    while(kase--){
        scanf("%d%d",&n,&k);
        printf("Case #%d: %s\n",kases++,di(n,k)?"ON":"OFF");
    }
    return 0;
}


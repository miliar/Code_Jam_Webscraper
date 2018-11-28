/*
 * Author: fatboy_cw
 * Created Time:  2011/5/7 11:56:02
 * File Name: D.cpp
 */
#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <vector>
using namespace std;
#define SZ(v) ((int)(v).size())

const int maxn = 1000;
int test,ca,n;
int num[maxn+5];
int sum;

int main() {
    freopen("D.out","w",stdout);
    scanf("%d",&test);
    while(test--){
        scanf("%d",&n);
        for(int i=1;i<=n;i++)   scanf("%d",num+i);
        sum=0;
        for(int i=1;i<=n;i++){
            if(num[i]!=i)   sum++;
        }
        printf("Case #%d: ",++ca);
        printf("%.6lf\n",sum*1.0);
    }
    return 0;
}


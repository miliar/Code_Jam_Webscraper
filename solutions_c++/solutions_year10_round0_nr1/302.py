#include<iostream>
#include<stdlib.h>
#include<stdio.h>
#include<cstring>
#include<string.h>
#include<algorithm>
#include<math.h>
#include<cmath>
using namespace std;

int main(){
    int t, n, k;
    scanf("%d",&t);
    for(int i=1; i<=t; i++){
        scanf("%d%d",&n,&k);
        printf("Case #%d: %s\n",i,((k+1)%(1<<n))==0 ? "ON":"OFF");
    }
    return 0;
}
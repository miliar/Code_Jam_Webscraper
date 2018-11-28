#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<iostream>
#include<algorithm>
#include<vector>
#include<queue>
using namespace std;
double ven[1000005];
double vpos[1000005];
double ABSs(double a){
    if(a < 0)return -1*a;
    return a;
}
int main (){
    int T,ca = 0;
    int n,D,i,now,j,v,pos;
    double mid,left,right,tmp;
    double old,next;
    int flag;
    scanf("%d",&T);
    while(T--){
        scanf("%d%d",&n,&D);
        now = 0;
        for(i=0;i<n;i++){
            scanf("%d%d",&pos,&v);
            for(j=0;j<v;j++){
                ven[now] = pos;
                now++;
            }
        }
//        printf("now %d\n",now);
        left = 0;
        right = 1000000000;
        while(right - left > 1e-2){
            mid = (right+left)/2;
            old = ven[0] - mid;
            flag = 1;
            for(i=1;i<now;i++){
                if(ven[i] > old){
                    if(ven[i] - mid - old < D)
                        next = old+D;
                    else
                        next = ven[i] - mid;
                }else{
                    if(ven[i] - mid - old < D)
                        next = old+D;
                    else
                        next = ven[i] + mid;
                }
                if(ABSs(ven[i] - next) > mid){
                    flag = 0;
                    break;
                }
                old = next;
                tmp += D;
            }
            if(flag == 0)left = mid;
            else right = mid;
        }
        ca++;
        
        printf("Case #%d: %.1lf\n",ca,left);
        
    }
    return 0;
}
/*
2
3 2
0 1
3 2
6 1
2 2
0 3
1 1
*/

/* 
 * File:   D.cc
 * Author: GongZhi
 * Problem:
 * Created on 2009年9月27日, 上午12:40
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
#include <math.h>
using namespace std;
/*
 *
 */
struct node{
    double x,y,r;
}data[10];
int main() {
    freopen("D-small-attempt0.in","r",stdin);
    freopen("D-small-attempt0.out","w",stdout);
    int kase,kases=1;
    int n,i;
    double ans;
    scanf("%d",&kase);
    while(kase--){
        scanf("%d",&n);
        for(i=0;i<n;i++)scanf("%lf%lf%lf",&data[i].x,&data[i].y,&data[i].r);
        if(n==1){
            ans=data[0].r;
        }
        else if(n==2){
            ans=max(data[1].r,data[0].r);
        }
        else{
            ans=1e30;
            double temp;
            temp=max((sqrt((data[0].x-data[1].x)*(data[0].x-data[1].x)+(data[0].y-data[1].y)*(data[0].y-data[1].y))+data[1].r+data[0].r)/2,data[2].r);
            //printf("%lf\n",temp);
            ans=min(ans,temp);
            temp=max((sqrt((data[2].x-data[1].x)*(data[2].x-data[1].x)+(data[2].y-data[1].y)*(data[2].y-data[1].y))+data[1].r+data[2].r)/2,data[0].r);
            ans=min(ans,temp);
            temp=max((sqrt((data[0].x-data[2].x)*(data[0].x-data[2].x)+(data[0].y-data[2].y)*(data[0].y-data[2].y))+data[2].r+data[0].r)/2,data[1].r);
            ans=min(ans,temp);
        }
        printf("Case #%d: %.10f\n",kases++,ans);
    }
    return 0;
}


/* 
 * File:   main.cpp
 * Author: perpetuity
 *
 * Created on 2011年5月22日, 上午1:10
 */

#include <cstdlib>
#include<cstdio>
#include<queue>
#include<cmath>

using namespace std;
int q[1000010],cnt=0;
int c,d;
/*
 * 
 */

bool Test(double dis){
    double tmp=q[0]-dis;
    for(int i=1;i<cnt;i++){
        tmp=max(tmp+d,q[i]-dis);
        //printf("%f %d\n",tmp,q[i]);
        if(fabs(tmp-q[i])>dis) return false;
    }
    return true;
}

int main(int argc, char** argv) {
    int t;
    scanf("%d",&t);
    for(int cas=1;cas<=t;cas++){
        scanf("%d%d",&c,&d);
        cnt=0;
        for(int i=0;i<c;i++){
            int p,v;
            scanf("%d%d",&p,&v);
            for(int j=0;j<v;j++){
                q[cnt++]=p;
            }
        }
        double l=0,r=2*1e5;
        while(r-l>1e-6){
            double mid=(r+l)/2;
            //printf("%f\n",mid);
            if(Test(mid)){
                r=mid;
            //printf("%f %d\n",mid,Test(mid));
            }
            else{
                l=mid;
            //printf("%f %d\n",mid,Test(mid));
            }
        }
        printf("Case #%d: %f\n",cas,(r+l)/2);
    }
    return 0;
}


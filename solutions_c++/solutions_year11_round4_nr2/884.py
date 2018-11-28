/*
 * Author: fatboy_cw
 * Created Time:  2011/6/4 23:21:36
 * File Name: B.cpp
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
const int maxn = 15;
int T,r,c,base,ca;
char d[maxn][maxn];

const double eps=1e-8;

int sgn(double x){
    return (x>eps)-(x<-eps);
}

double getx(int x,int y){
    return x+0.5;
}

double gety(int x,int y){
    return (r-y-1)+0.5;
}

bool could(int x,int y,int k){
    double mx=0.0,my=0.0;
    int cnt=0;
    for(int i=x;i<x+k;i++){
        for(int j=y;j<y+k;j++){
            if(i==x && j==y)    continue;
            if(i==x && j==y+k-1)    continue;
            if(i==x+k-1 && j==y)    continue;
            if(i==x+k-1 && j==y+k-1)    continue;
            mx+=getx(i,j)*(d[i][j]-'0'+base);
            my+=gety(i,j)*(d[i][j]-'0'+base);
            cnt+=d[i][j]-'0'+base; 
        }
    }
    if(!cnt)    return false;
    mx/=cnt;
    my/=cnt;
    double sx=(getx(x,y)+getx(x+k-1,y))/2.0,sy=(gety(x,y)+gety(x,y+k-1))/2.0;
    return sgn(sx-mx)==0 && sgn(sy-my)==0;
}
    

bool check(int k){
    for(int i=0;i<=r-k;i++){
        for(int j=0;j<=c-k;j++){
            if(could(i,j,k)){
                return true;
            }
        }
    }
    return false;
}
        

int main() {
    freopen("B.out","w",stdout);
    scanf("%d",&T);
    //cout<<(0.04*9+1.04*9+0.04*10-0.96*11+0.04*11)<<endl;
    //cout<<(1.46*9+1.46*9+1.46*10+1.46*11+1.46*11)<<endl;
    //cout<<(1.5*9+2.5*9+1.5*10+0.5*11+1.5*11)<<endl;
    //return 0;
    while(T--){
        scanf("%d%d%d",&r,&c,&base);
        for(int i=0;i<r;i++){
            scanf("%s",d[i]);
        }
        int ans=-1;
        for(int k=10;k>=3;k--){
            if(check(k)){
                ans=k;
                break;
            }
        }
        printf("Case #%d: ",++ca);
        if(ans==-1) printf("IMPOSSIBLE\n");
        else{
            printf("%d\n",ans);
        }
    }
    return 0;
}


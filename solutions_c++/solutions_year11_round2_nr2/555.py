/*
 * Author: fatboy_cw
 * Created Time:  2011/5/22 0:46:58
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

const int maxn = 1000005;

int ca,t,d,c;
int pos[maxn],cnt;
int np[maxn];

bool check(int mid){
    np[0]=pos[0]-mid;
    for(int i=1;i<cnt;i++){
        int dis=pos[i]-np[i-1];
        if(dis>=d){
            int tmp=dis-d; //最多移动的距离
            if(mid>=tmp){
                np[i]=pos[i]-tmp;
            }
            else{
                np[i]=pos[i]-mid;
            }
        }
        else{
            int tmp=d-dis; //最少向右走多远
            if(mid>=tmp){
                np[i]=pos[i]+tmp;
            }
            else{
                return false;
            }
        }
    }
    return true;
}

int main() {
    freopen("B.out","w",stdout);
    scanf("%d",&t);
    while(t--){
        scanf("%d%d",&c,&d);
        d*=2;
        cnt=0;
        for(int i=0;i<c;i++){
            int p,v;
            scanf("%d%d",&p,&v);
            p*=2;
            for(int j=0;j<v;j++){
                pos[cnt++]=p;
            }
        }
        sort(pos,pos+cnt);
        int ans,l=0,r=1000000000,mid;
        while(l<=r){
            mid=(l+r)>>1;
            if(check(mid)){
                ans=mid;
                r=mid-1;
            }
            else{
                l=mid+1;
            }
        }
        printf("Case #%d: ",++ca);
        printf("%.7lf\n",ans/2.0);
    }
    return 0;
}


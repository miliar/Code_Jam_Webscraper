/*
 * Author: xg1990
 * Created Time:  2010-5-8 16:25:33
 * File Name: gcjc.cpp
 */
#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <queue>
using namespace std;
#define out(v) cerr << #v << ": " << (v) << endl
#define SZ(v) ((int)(v).size())
const int maxint = -1u>>1;
template <class T> bool get_max(T& a, const T &b) {return b > a? a = b, 1: 0;}
template <class T> bool get_min(T& a, const T &b) {return b < a? a = b, 1: 0;}

int g[1001],size;
int re[1001],next[1001];

int main() {
freopen("C-large.out", "w", stdout);
freopen("C-large.in", "r", stdin);
    int t,tt,r,k,n;
    long long money,gn;
    scanf("%d",&t);tt=0;
    while(tt++<t){
        scanf("%d%d%d",&r,&k,&n);
        size=0;
        for(int i=0,tmp;i<n;++i){
            scanf("%d",&g[size++]);
        }
        money=0;
        memset(re,-1,sizeof(re));
        memset(next,-1,sizeof(next));
        
        for(int i=0,p=0,j;i<r;++i){
            if(re[p]!=-1){
                
                money+=re[p];
                p=next[p];
            }
            else{
                j=0;gn=0;
                int tp=p;
                re[tp]=0;
                while(j+g[p]<=k&&gn<size){
                    j+=g[p];
                    re[tp]+=g[p];
                    p=(p+1)%size;
                    gn++;
                }
                next[tp]=p;
                money+=j;
            }
        }
        printf("Case #%d: %I64d\n",tt,money);
    }
    return 0;
}


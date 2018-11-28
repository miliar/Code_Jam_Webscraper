/* 
 * File:   B.cc
 * Author: GongZhi
 * Problem:
 * Created on 2010年6月5日, 下午10:29
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
queue<int> Q;
int main() {
    freopen("B-small-attempt0.in","r",stdin);
    freopen("B-small-attempt0.out","w",stdout);
    int kase,kases=1;
    scanf("%d",&kase);
    while(kase--){
        while(!Q.empty())Q.pop();
        int p;
        scanf("%d",&p);
        p=1<<p;
        for(int i=0;i<p;i++){
            int u;
            scanf("%d",&u);
            Q.push(u);
        }
        int t;
        for(int i=0;i<p-1;i++)scanf("%d",&t);
        int ans=0;
        while(!Q.empty()){
            int a=Q.front();
            Q.pop();
            int b;
            if(Q.empty()){
                break;
            }else{
                b=Q.front();
                Q.pop();
            }
            int c=min(a,b);
//            printf("aaa%d\n",c);
            if(c==0)ans++;
            else c--;
            Q.push(c);
        }
        printf("Case #%d: %d\n",kases++,ans);
    }
    return 0;
}


/* 
 * File:   C.cc
 * Author: GongZhi
 * Problem:
 * Created on 2010年5月23日, 上午1:13
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
const int MOD=100003;
int dp[510][510];
int c[510][510];
void C(int k,int n){
    if(c[k][n]!=-1)return;
    if(k==0 || k==n){
        c[k][n]=1;
        return;
    }
    C(k,n-1);
    C(k-1,n-1);
    c[k][n]=(c[k][n-1]+c[k-1][n-1])%MOD;
}
void di(int i,int j){
    if(dp[i][j]!=-1)return;
    if(j==1){
        dp[i][j]=1;
        return;
    }
    int t=0;
    for(int k=1;k<j;k++){
        if(i-j-1<j-k-1)continue;
        di(j,k);
        C(j-k-1,i-j-1);
        t+=dp[j][k]*c[j-k-1][i-j-1];
        t%=MOD;
    }
    dp[i][j]=t%MOD;
    return;
}
int main() {
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("C-small-attempt0.out", "w", stdout);
    int kases,kase=1;
    cin >> kases;
    memset(dp,-1,sizeof(dp));
    memset(c,-1,sizeof(c));
    for(int i=2;i<=500;i++)
        for(int j=1;j<i;j++)
            if(dp[i][j]==-1)di(i,j);
    while(kases--){
        int ans=0;
        int n;
        cin >> n;
        for(int i=1;i<n;i++){
            //printf("===%d %d %d\n",n,i,dp[n][i]);
            ans+=dp[n][i];
            ans%=MOD;
        }
        printf("Case #%d: %d\n", kase++,ans);
    }
    return 0;
}


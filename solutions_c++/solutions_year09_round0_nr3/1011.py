/* 
 * File:   c.cpp
 * Author: GongZhi
 * Problem:
 * Created on 2009年9月3日, 下午9:35
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
#define MOD 10000
char data[100]="welcome to code jam";
char a[1000];
int dp[1000][50];
int main() {
    freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);
    int n,l,m;
    m=strlen(data);
    scanf("%d",&n);
    gets(a);
    for(int k=1;k<=n;k++){
        gets(a);
        l=strlen(a);
        memset(dp,0,sizeof(dp));
        if(a[0]==data[0])dp[0][0]=1;
        for(int i=1;i<l;i++){
            for(int j=0;j<m;j++)dp[i][j]=(dp[i][j]+dp[i-1][j])%MOD;
            if(a[i]==data[0])dp[i][0]=(dp[i][0]+1)%MOD;
            for(int j=1;j<m;j++)if(data[j]==a[i])dp[i][j]=(dp[i][j]+dp[i-1][j-1])%MOD;
        }
        dp[l-1][m-1]%=MOD;
        printf("Case #%d: %04d\n",k,dp[l-1][m-1]);
    }
    return 0;
}


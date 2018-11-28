/*************************************************************************
Author: aMR
Created Time: 2010/5/23 1:36:32
File Name: c.cpp
Description: 
************************************************************************/
#include <cstdio>
#include <cstring>
#include <cmath>
#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <map>
#include <sstream>
#include <queue>
using namespace std;
#define out(x) (cout<<#x<<": "<<x<<endl)
const int maxint=0x7FFFFFFF;
typedef long long lint;
template<class T>void show(T a, int n){for(int i=0; i<n; ++i) cout<<a[i]<<' '; cout<<endl;}
template<class T>void show(T a, int r, int l){for(int i=0; i<r; ++i)show(a[i],l);cout<<endl;}

const int mod = 100003;

int c[512][512];
int dp[512][512];
int ans[512];

void init() {
    memset(c, 0, sizeof(c));
    c[0][0] = c[1][0] = c[1][1] = 1;
    for(int i=2; i<=500; ++i) {
        c[i][0] = 1;
        for(int j=1; j<=i; ++j) {
            c[i][j] = (c[i-1][j-1] + c[i-1][j]) % mod;
        }
    }
}

void work() {
    memset(dp, 0, sizeof(dp));
    for(int i=2; i<=500; ++i) {
        dp[i][1] = 1;
        for(int j=2; j<i; ++j) {
            for(int k=1; k<j; ++k) {
                dp[i][j] += dp[j][k] * c[i-j-1][j-k-1];
                dp[i][j] %= mod;
            }
        }
    }
    memset(ans, 0, sizeof(ans));
    for(int i=2; i<=500; ++i) {
        for(int j=1; j<i; ++j) {
            ans[i] += dp[i][j];
            ans[i] %= mod;
        }
    }
}

int main()
{
    int z, t;
    init();
    work();
    cin >> z;
    for(int ca=1; ca<=z; ++ca) {
        cin >> t;
        printf("Case #%d: %d\n", ca, ans[t]);
    }
    return 0;
}


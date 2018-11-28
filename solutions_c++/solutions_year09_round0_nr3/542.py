/*************************************************************************
Author: aMR
Created Time: 2009-9-3 15:20:46
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
const int maxint=0x7fffffff;
char c[] = "welcome to code jam";
char ch[1010];
int dp[1010][32];
int main()
{
    freopen("c.txt", "w", stdout);
    int ca = 0, z;
    scanf("%d", &z);
    gets(ch);
    while(z--) {
        gets(ch+1);
        int len = strlen(ch+1);
        memset(dp, 0, sizeof(dp));
        dp[0][0] = 1;
        for(int i=1; i<=len; ++i) {
            dp[i][0] = 1;
            for(int j=1; j<20; ++j) {
                dp[i][j] = dp[i-1][j];
                if(ch[i] == c[j-1]) {
                    dp[i][j] += dp[i-1][j-1];
                }
                dp[i][j] %= 10000;
            }
        }
        printf("Case #%d: %04d\n", ++ca, dp[len][19]);
    }
    return 0;
}

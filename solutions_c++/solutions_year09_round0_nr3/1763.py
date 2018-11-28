/**********************************************************************
Author: hanshuai
Created Time:  2009-09-03 18:40:43
File Name: 3.cpp
Description: 
**********************************************************************/
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <vector>

using namespace std;

typedef long long int64;
const int maxint = 0x7FFFFFFF;
const int64 maxint64 = 0x7FFFFFFFFFFFFFFFLL;
char s[1000];
char x[]={" welcome to code jam"};
int cnt[20];
int main() {
    freopen("3.out", "w", stdout);
    int test;
    scanf("%d\n", &test);
    for(int cas = 1; cas <= test; cas ++){
        gets(s);
        memset(cnt, 0, sizeof(cnt));
        cnt[0] = 1;
        int len = strlen(s);
        for(int i = 0; i < len; i ++){
            for(int j = 19; j >= 1; j --){
                if(s[i] == x[j]){
                   cnt[j] = (cnt[j] + cnt[j-1])%10000;
                }
            }
        }
        printf("Case #%d: %04d\n", cas, cnt[19]);
    }
    return 0;
}


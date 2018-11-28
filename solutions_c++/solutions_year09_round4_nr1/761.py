/**********************************************************************
Author: hanshuai
Created Time:  2009-09-27 0:31:55
File Name: aa.cpp
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
char s[50][50];
int cc[50], vis[50], p[50];
int main() {
    freopen("aa.out", "w", stdout);
    int test, n, cas = 0;
    scanf("%d", &test);
    while(test--){
        scanf("%d", &n);
        memset(vis, 0, sizeof(vis));
        for(int i = 0; i < n; i ++){
            scanf("%s", s[i]);
            cc[i] = 0;
            for(int j = 0; j < n; j ++){
                if(s[i][j] == '1') cc[i] = j;
            }
        }
        for(int i = 0; i < n; i ++){
           for(int j = 0; j < n; j ++){
              if(vis[j]) continue;
              if(cc[j] <= i){
                  p[i] = j;
                  vis[j] = 1;
                  break;
              }
           }
        }
        int ans = 0;
        for(int i = 0; i < n; i ++){
            for(int j = i + 1; j < n; j ++){
                if(p[i] > p[j]) ans ++;
            }
        }
        printf("Case #%d: %d\n", ++cas, ans);
    }
}

/**********************************************************************
Author: hanshuai
Created Time:  2009-09-03 16:11:55
File Name: 1.cpp
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
int a[5005][16], x[16];
char buf[100];
int main() {
    freopen("1.out", "w", stdout);
    int l, d, n, len;
    scanf("%d%d%d", &l, &d, &n);
    for(int i = 0; i < d; i ++){
        scanf("%s", buf);
        for(int j = 0; j < l; j ++){
            a[i][j] = 1<<(buf[j]-'a');
        }
    }
    for(int i = 0; i < n; i ++){
        scanf("%s", buf);
        len = strlen(buf);
        int cc = 0, t = 0, cnt = 0;
        for(int j = 0; j < len; j ++){
            if(buf[j] == '('){
                cc ++;
            }
            else if(buf[j] == ')'){
                x[cnt++] = t; t = 0;
                cc --;
            }else{
                if(cc == 0){
                    x[cnt++] = 1<<(buf[j]-'a');
                } 
                else t |= (1<<(buf[j]-'a'));
            }
        }
        
        int ans = 0;
        for(int j = 0; j < d; j ++){
            bool ok = true;
            for(int k = 0; k < l; k ++){
                if(!(x[k]&a[j][k])){
                    ok = false; break;
                }
            }
            if(ok) ans ++;
        }
        printf("Case #%d: %d\n", i + 1, ans);
    }
    return 0;
}


/**********************************************************************
Author: hanshuai
Created Time:  2010/5/8 18:46:54
File Name: a.cpp
Description: 
**********************************************************************/
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <vector>

using namespace std;


int main() {
    freopen("a.out", "w", stdout);
    int test, n, k, cas = 0;
    scanf("%d", &test);
    while(test --){
        scanf("%d%d", &n, &k);
        printf("Case #%d: ", ++cas);
        int x = (1<<n)-1;
        if((k&x) == x){
            printf("ON\n");
        }else printf("OFF\n");
    }
    return 0;
}


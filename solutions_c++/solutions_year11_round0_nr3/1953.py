/*
    Author : Akai
    Problem : C
*/

#include<iostream>
#include<cstdio>
#include<fstream>
#include<algorithm>
#include<cmath>
#include<vector>
#include<map>
#include<cstring>

using namespace std;

int testcases , cases , ans , tmp  , t  , n ;

int main(){
    //freopen("C.in" , "r" , stdin);
    //freopen("C.out" , "w" , stdout);
    scanf("%d" , &testcases);
    for (cases = 1 ; cases <= testcases ; cases++){
        scanf("%d" , &n);
        t = 0 ; tmp = 10000001 ; ans = 0 ;
        for (int i = 1 ; i <= n ; i++){
            int x ;
            scanf("%d" , &x);
            tmp = min(x , tmp);
            ans += x ;  
            t = t ^ x ;
        }
        printf("Case #%d: " , cases);
        if (t !=0 )puts("NO"); else printf("%d\n" , ans - tmp);
    }
}

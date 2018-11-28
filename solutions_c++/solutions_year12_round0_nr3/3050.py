/*
 * Author:  kymo
 * Created Time:  2012/4/14 13:35:10
 * File Name: C.cpp
 */
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <time.h>
using namespace std;
const int maxint = -1u>>1;
int A ,B ;
int n;
int bits(long long n)
{
    if(n < 10)
        return 1 ;
    else if(n < 100)
        return 2 ;
    else if(n < 1000)
        return 3 ;
    else if(n < 10000)
        return 4 ;
    else if(n < 100000)
        return 5 ;
    else if(n < 1000000)
        return 6 ;
    else if(n < 10000000)
        return 7 ;
}
int temp[10] ;
long long ten(int n)
{
    if(n == 0) return 1 ;
    else return 10 * ten(n - 1) ;
}
void solve()
{
    cin>>n ;
    for(int i = 0;i < n ;i ++)
    {
        cin>>A>>B;
        
        long long ans = 0 ;
        for(long long j = A;j <= B ;j ++)
        {
            int bit = bits(j) ;
            int num[10] ;
            int st = 0 ;
            for(int k = 0 ;k < bit - 1;k ++)
            {
                int tenS = ten(k + 1) ;
                int mod = j % tenS ;
                int div = j / tenS ;
                long long final = mod * ten(bit - k - 1) + div ;
                if(final > j && final <= B)
                {
                    num[st ++] = final ;
                    ans ++ ;
                }
            }
            for(int k = 0 ;k < st - 1 ;k ++)
            {
                for(int l = k + 1;l < st ;l ++)
                {
                    if(num[k] == num[l])
                        ans -- ;
                }
            }
        }
        printf("Case #%d: %d\n",i + 1 ,ans) ;
    }
}
int main() {
    freopen("3.out" ,"w" ,stdout) ;
    solve() ; 
    return 0;
}


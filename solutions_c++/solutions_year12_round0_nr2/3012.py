/*
 * Author:  kymo
 * Created Time:  2012/4/14 10:13:17
 * File Name: B.cpp
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
#define max 101
int T,S,P,N,t[max] ;
int judge[max] ;
int maxResult ,trt ;
void solve()
{
    cin>>N ;
    for(int i = 0 ;i < N ;i ++)
    {
        scanf("%d",&T) ;
        scanf("%d",&S) ;
        scanf("%d",&P) ;
        trt = 3 * P - 2 ;
        int five = 0 ;
        memset(judge ,0 ,sizeof(judge)) ;
        if(P <= 1)
        {
            for(int j = 0 ;j < T;j ++)
            {
                scanf("%d",&t[j]) ;
            }
            int one = 0 ;
            int two = 0 ;
            for(int j = 0; j < T;j ++)
            {
                if(t[j] >= 2)
                    two ++ ;
                if(t[j] >= 1)
                    one ++ ;
            }
            printf("Case #%d: " ,i + 1) ;
            if(P == 0)
                if(two < S)
                    cout<<0<<endl ;
                else 
                    cout<<T<<endl ;
            else
                if(two < S)
                    cout<<0<<endl ;
                else
                    cout<<one<<endl ;
                    
        }
        else{
            for(int j = 0 ;j < T;j ++)
            {
                scanf("%d",&t[j]) ;
                if(t[j] >= 2 && t[j] < trt - 2)
                    judge[j] = 1 ;
                if(t[j] >= trt - 2 && t[j] < trt)
                    judge[j] = 2;
                if(t[j] >= trt)
                    judge[j] = 3 ;
                if(t[j] >= 2)
                    five ++ ;
            }
            int one,two,three,four;
            one = two = three =0 ;
            for(int j = 0 ;j < T ;j ++)
            {
                one = (judge[j] != 1)?one : one + 1 ;
                two = (judge[j] != 2)?two : two + 1 ;
                three = (judge[j] != 3)?three : three + 1 ;
            }
             printf("Case #%d: " ,i + 1) ;
            if(two >= S)
            {
                cout<< three + S  <<endl ;
            }
            else
            {
                if(one + two >= S)
                    cout<<three + two <<endl ;
                else
                {
                    if(one + two + three >= S)
                        cout<<two + three<<endl ;
                    else
                        cout<<0<<endl ;
                }
            }
            
        }
    }
}
int main() {
    freopen("2.out" ,"w" ,stdout) ;
    solve() ;
    return 0;
}


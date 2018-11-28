/*
 * Author:  kymo
 * Created Time:  2012/4/14 9:27:31
 * File Name: A.cpp
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
int n ; 
char lang[101] ;
char tran[27] = {'y','h','e','s','o','c','v','x','d','u','i','g','l','b',
    'k','r','z','t','n','w','j','p','f','m','a','q'} ;
void solve()
{
    cin>>n ;
    
    getchar() ;
    for(int i = 0 ;i < n ;i ++)
    {
        gets(lang) ;
        printf("Case #%d: " ,i + 1) ;
        for(int j = 0 ;j < strlen(lang) ; j ++)
        {
            if(lang[j] != ' ')
                printf("%c" ,tran[lang[j] - 'a']) ;
            else
                printf(" ") ;
        }
        printf("\n") ;
    }
}
int main() {
    freopen("1.out" ,"w",stdout) ;
    solve() ;
    return 0;
}


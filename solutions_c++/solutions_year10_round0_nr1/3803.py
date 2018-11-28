/* 
 * File:   googleJam_A.cpp.cpp
 * Author: lenovo
 *
 * Created on 2010年5月8日, 下午7:29
 */

#include<stdlib.h>
#include<iostream>
using namespace std;
bool check( int n, int k )
{
    for( int i=0; i < n; i++ )
    {
        if( !( k & 1 ) ) return false;
        k>>=1;
    }
    return true;
}
int main(int argc, char** argv)
{
    freopen("A-large.in","r",stdin);
    freopen("out1.txt","w",stdout);
    int t,n,k,j=1;;
    scanf("%d",&t);
    while( t-- )
    {
        scanf("%d%d",&n,&k);
        printf("Case #%d: ",j++);
        if( check( n, k ) )printf("ON\n");
        else printf("OFF\n");
    }
    return (EXIT_SUCCESS);
}


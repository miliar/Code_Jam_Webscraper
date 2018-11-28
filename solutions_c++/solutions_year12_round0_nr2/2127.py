/* 
 * File:   main.cpp
 * Author: liuyubo
 *
 * Created on April 15, 2012, 1:22 AM
 */

#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cctype>

#include <utility>
#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <queue>
#include <map>

using namespace std;

void loadData( void );
void proc( void );
void printRes( int,int );

int N,S,p;

int main(int argc, char** argv) {

    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    loadData();
    
    return 0;
}

void proc( void ){
    
    return ;
}

void loadData( void ){

    int T;
    scanf("%d",&T);
    for( int cases = 1 ; cases <= T ; cases ++ ){
        
        scanf("%d%d%d",&N,&S,&p);
        
        int sure = 0;
        int not_sure = 0;
        int sum;
        for( int i = 0 ; i < N ; i ++ ){
            scanf("%d",&sum);
            if( sum >= p ){
                if( sum - p >= 2*(p-1) )
                    sure ++;
                else if( sum - p >= 2*(p-2) )
                    not_sure ++;
            }
        }
        
        printRes( cases , sure + min( not_sure , S ) );
    }
    return;
}

void printRes( int index , int res ){

    printf("Case #%d: %d\n",index,res);
    return;
}


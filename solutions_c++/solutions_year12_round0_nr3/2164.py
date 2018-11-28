/* 
 * File:   main.cpp
 * Author: liuyubo
 *
 * Created on April 15, 2012, 1:34 AM
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
int proc( void );
void printRes( int,int );

int A,B;
bool visited[2000001];

int calc( int num );

bool lyb_debug = true;

int main(int argc, char** argv) {

    //freopen("C-small-attempt0.in","r",stdin);
    //freopen("C-small.out","w",stdout);
    freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);
    loadData();
    
    return 0;
}

int calc( int num ){
    
    /*
    if( lyb_debug ){
        printf("check %d: the digits are:",num);
    }
    */ 
    
    vector<int> v;
    while( num ){
        v.push_back( num%10 );
        num/=10;
    }
    
    reverse( v.begin() , v.end() );
    /*
    if( lyb_debug ){
        for( int i = 0 ; i < v.size() ; i ++ )
            printf("%d ",v[i]);
        printf("\n");
    }
    */
    int res = 0;
    for( int i = 0 ; i < v.size() ; i ++ )
        if( v[i] != 0 ){
        
            int n = 0;
            int index = 0,p=i;
            while( index < v.size() ){
                n = n*10+v[p];
                p = (p+1)%v.size();
                index ++;
            }
            
            if( n >= A && n <= B && !visited[n] ){
                visited[n] = true;
                res ++;
            }
        }
    /*
    if( lyb_debug && res > 1){
        printf("can generate %d nums.\n",res);
    }
    */
    
    return (res-1)*res/2;
}

int proc( void ){
    
    memset( visited , false , sizeof( visited ) );
    int res = 0;
    
    for( int i = A ; i <= B ; i ++ )
        if( !visited[i] ){
        
            res += calc( i );
        }
    return res;
}

void loadData( void ){

    int T;
    scanf("%d",&T);
    for( int cases = 1 ; cases <= T ; cases ++ ){
        
        scanf("%d%d",&A,&B);
        printRes( cases , proc() );
    }
    return;
}

void printRes( int index , int res ){

    printf("Case #%d: %d\n",index,res);
    return;
}


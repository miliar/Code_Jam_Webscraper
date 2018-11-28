/* 
 * File:   GCJ_A.cpp
 * Author: Bill
 *
 * Created on 2009年9月3日, 下午7:10
 */

#include <stdlib.h>
#include <set>
#include <string>
#include <iostream>
using namespace std ;

/*
 * 
 */
int L , D , N , Ans ;
set<string> Hash;
char st[20] ;
string Tst , word ;
int Lef[20] , Rig[20] ;

void Doit( int t ){
    if( t > L ){
        Ans++ ;
        return ;
    }
    string old = Tst ;
    for( int i = Lef[t] ; i <= Rig[t] ; ++i ){
        Tst = old + word[i] ;
        if( Hash.find( Tst ) != Hash.end() ){
            Doit( t+1 ) ;
        }
    }
}
void pro(){
    int now = 0 ;
    int Len = word.length() ;
    for( int i = 0 ; i < Len ; ++i ){
        now++ ;
        if( word[i] == '(' ){
            Lef[now] = i+1 ;
            for( int j = i+2 ; j < Len ; ++j )
                if( word[j] == ')' ){
                    Rig[now] = j-1 ;
                    i = j ;
                    break ;
                }
        }else{
            Lef[now] = i ;
            Rig[now] = i ;
        }
    }
}
void solve(){
    Hash.clear();
    for( int i = 0 ; i < D ; i++ ){
        scanf("%s",st);
        string tmp = "" ;
        for( int j = 0 ; j < L ; ++j ){
            tmp = tmp + st[j] ;
            if( Hash.find( tmp ) == Hash.end() ){
                Hash.insert( tmp ) ;
            }
        }
    }
    for( int i = 1 ; i <= N ; ++i ){
        Ans = 0 ;
        cin>>word ;
        pro();
        Tst = "" ;
        Doit( 1 ) ;
        printf("Case #%d: %d\n",i,Ans);
    }
}
int main(int argc, char** argv) {
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    scanf("%d%d%d",&L,&D,&N);
    solve();
    return (EXIT_SUCCESS);
}


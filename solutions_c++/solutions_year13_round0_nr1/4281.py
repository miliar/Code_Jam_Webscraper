#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>
#include <cstring>
#include <string>
#include <map>
#include <set>
#include <cstdlib>

using namespace std ; 

typedef long long int64; 

void open_file(){
    string s = "1.txt" ; 
    freopen(s.c_str(),"r", stdin); 
    freopen( (s + "out.txt").c_str(), "w", stdout); 
}

char s[10][10];

bool gao ( char c ){
    int res1 = 0,res2=0 ;
    for(int i=0; i< 4; ++i){
        int res3=0,res4=0; 
        
        res1 +=( s[i][i] ==c || s[i][i] =='T');  
        res2 +=( s[i][3-i] == c || s[i][3-i]=='T') ;
        for(int j=0; j < 4; ++j){ 
            res3 += (s[i][j] == c|| s[i][j]=='T') ;
            res4 += (s[j][i] ==c || s[j][i]=='T') ; 
        } 
        if( res3 == 4 || res4 ==4  ) return true ; 
    }
    if( res1 ==4 || res2==4 ) return true ;
    return false; 
}
    
int cal(){
    if( gao('X') ) return 1; 
    if( gao('O') ) return -1; 
    int res = 0 ; 
    for(int i=0; i < 4; ++i){
        for(int j=0; j < 4; ++j){
            res += s[ i ][ j ] != '.' ;
        }
    }
    return res ==16 ? 0 : 2  ;
}
int main (){
   // open_file() ; 
    int T ; 
    cin >> T  ; 
    for(int Cas=1 ;Cas<= T; ++Cas){ 
        for(int i= 0 ; i < 4 ; ++i) 
            scanf ("%s", s+i)  ;
        int ans = cal() ;
        cout <<"Case #"<<Cas<<": "; 
        if(ans==0){
            puts("Draw") ;
        }
        else if( ans == 1 ){
            puts("X won") ;
        }
        else if( ans == -1 ){
            puts("O won") ; 
        }
        else puts("Game has not completed") ;
    }
    return 0;
}

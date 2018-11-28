/*
   Problem: A
   Author: Akai
   Date: 2013/4/13
   Meaning£º
   Algorithm£º
*/
#include <algorithm>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <utility>
#include <vector>

using namespace std;

char s[5][5] ;
int T , tot ;

int checkox(int x){
    int cnt = 0 ;
    for (int i = 0 ; i <= 3 ; i++){ 
        if (s[x][i] != 'O' && s[x][i] != 'T') return 0 ;
        if (s[x][i] == 'T') cnt ++ ;
    }
    if (cnt > 1) return 0 ;
    return 1 ;
}
int checkoy(int x){
    int cnt = 0 ;
    for (int i = 0 ; i <= 3 ; i++){ 
        if (s[i][x] != 'O' && s[i][x] != 'T') return 0 ;
        if (s[i][x] == 'T') cnt ++ ;
    }
    if (cnt > 1) return 0 ;
    return 1 ;
}

int checkoz(){
    bool flag1 = 1 , flag2 = 1 ;
    int cnt = 0 ;
    for (int i = 0 ; i <= 3 ; i++){ 
        if (s[i][i] != 'O' && s[i][i] != 'T') flag1 = 0 ;
        if (s[i][i] == 'T') cnt ++ ;
    }
    if (cnt > 1) flag1 = 0 ;
    cnt = 0 ;
    for (int i = 0 ; i <= 3 ; i++){ 
        if (s[i][3-i] != 'O' && s[i][3-i] != 'T') flag2 = 0 ;
        if (s[i][3-i] == 'T') cnt ++ ;
    }
    if (cnt > 1) flag2 = 0 ;
    return flag1 || flag2 ;
}
    

int checkxx(int x){
    int cnt = 0 ;
    for (int i = 0 ; i <= 3 ; i++){ 
        if (s[x][i] != 'X' && s[x][i] != 'T') return 0 ;
        if (s[x][i] == 'T') cnt ++ ;
    }
    if (cnt > 1) return 0 ;
    return 1 ;
}
int checkxy(int x){
    int cnt = 0 ;
    for (int i = 0 ; i <= 3 ; i++){ 
        if (s[i][x] != 'X' && s[i][x] != 'T') return 0 ;
        if (s[i][x] == 'T') cnt ++ ;
    }
    if (cnt > 1) return 0 ;
    return 1 ;
}
int checkxz(){
    bool flag1 = 1 , flag2 = 1 ;
    int cnt = 0 ;
    for (int i = 0 ; i <= 3 ; i++){ 
        if (s[i][i] != 'X' && s[i][i] != 'T') flag1 = 0 ;
        if (s[i][i] == 'T') cnt ++ ;
    }
    if (cnt > 1) flag1 = 0 ;
    cnt = 0 ;
    for (int i = 0 ; i <= 3 ; i++){ 
        if (s[i][3-i] != 'X' && s[i][3-i] != 'T') flag2 = 0 ;
        if (s[i][3-i] == 'T') cnt ++ ;
    }
    if (cnt > 1) flag2 = 0 ;
    return flag1 || flag2 ;
}
    

int main(){
//	freopen("A-small-attempt0.in", "r", stdin);
//	freopen("A-small-attempt0.out", "w", stdout);
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
    scanf("%d" , &T);
    for (int cases = 1 ; cases <= T ; cases++){
          printf("Case #%d: " , cases);
          memset(s , 0 ,sizeof(s)) ;
          for (int i = 0 ; i < 4 ; i++) scanf("%s" , s[i]);
          tot = 0 ;
          for (int x = 0 ; x < 4 ; x++) for(int i = 0 ; i < 4 ; i++)
          if (s[x][i] == '.') tot = 1 ;
          bool s = 0 ;
          for (int i = 0 ; i < 4 ; i++){
              s = s || checkox(i);
              s = s || checkoy(i) ;
          }
          s = s || checkoz() ;
          if (s == 1) {
                puts("O won") ;
                continue ;
          } 
          s = 0 ;
          for (int i = 0 ; i < 4 ; i++){
              s = s || checkxx(i);
              s = s || checkxy(i) ;
          }
          s = s || checkxz() ;
          if (s == 1) {
                puts("X won") ;
                continue ;
          } 
          if (tot == 1) puts("Game has not completed") ; 
          else puts("Draw");
    }
          

	return 0;
}

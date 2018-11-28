#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;
const int inf = 1<<29;
int judge(char ch) {
    if(ch == 'X') {
        return 0;      
    } else if(ch == 'O') {
        return 1;
    } else if(ch == 'T') {
        return 2;
    }
    return 3;
}
bool yes(int ar[], string& ans) {
      if(ar[0] + ar[2] == 4) {
                ans = "X won";
                return true;
      } else if(ar[1] + ar[2] == 4) {
                ans = "O won";
                return true;
      }
      return false;
}

int main() {
    int T;
    freopen("C:/Users/wangkun/Downloads/A-large.in", "r" , stdin);
    freopen( "D:/result.out",  "w",stdout); 
    cin >> T;
    int cas = 0;
    while(T--) {
         cas++;
         string g[4] ;
         string ans = "Game has not completed";
         bool  full = true ,flag = false;
         for(int i = 0; i < 4; i ++) {
             cin >>g[i];
         }
         
         for(int i = 0; i < 4; i++) {
             for(int j =0 ; j < 4; j++){
               if(g[i][j] == '.') {
                   full = false;
               }
             }
         }
         
         int ar[4] = {0};
         for(int i =0; i <4 ; i++) {
            // int x = 0 , o = 0 , t = 0;
            
            memset(ar, 0 ,sizeof(ar));
            for(int j = 0 ; j < 4 ; j++) {
                ar[judge(g[i][j])] ++;
            }
            if(yes(ar, ans)){
               flag =true;
               break;
            }
          
            
            memset(ar, 0 ,sizeof(ar));
            
            for(int j = 0 ; j < 4 ; j++) {
                ar[judge(g[j][i])] ++;
            }
            
            if(yes(ar, ans)){
               flag =true;
               break;
            }
         }
         memset(ar, 0 ,sizeof(ar));
         for(int i = 0; !flag && i < 4 ; i++) {
             ar[judge(g[i][i])] ++;
         }
         if(!flag && yes(ar, ans)){
              flag =true;
         }
         
         memset(ar, 0 ,sizeof(ar));
         for(int i = 0; !flag && i < 4 ; i++) {
             ar[judge(g[i][i])] ++;
         }
         if(!flag && yes(ar, ans)){
              flag =true;
         }
         
         memset(ar, 0 ,sizeof(ar));
         for(int i = 0; !flag && i < 4 ; i++) {
             ar[judge(g[i][3-i])] ++;
         }
         if(!flag && yes(ar, ans)){
              flag =true;
         }
         if(!flag && full) {
            ans = "Draw";
         }
         cout << "Case #"<<cas<<": " << ans << endl;
    }
    return 0;
}

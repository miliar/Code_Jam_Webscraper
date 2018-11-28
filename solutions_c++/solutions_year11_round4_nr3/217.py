/*
    Author : Akai
    Problem : C
*/

#include<iostream>
#include<cstdio>
#include<fstream>
#include<algorithm>
#include<cmath>
#include<vector>
#include<map>
#include<cstring>

using namespace std;
const long long Mxn = 1000001 ;

bool f[1100001] ; 
long long testcases , cases , mx , mn , n; 

int main(){
    freopen("C-large.in" ,"r", stdin);
    freopen("C-large.out" , "w" ,stdout);
 //   freopen("C-small0.in" ,"r", stdin);
 //   freopen("C-small1.out" , "w" ,stdout);
    for (long long i = 2;  i<= 1000000 ; i++) if (!f[i])
        for (long long j = i * i ; j <= 1000001 ; j += i) f[j] = 1 ;
    cin >> testcases ;
    while (testcases--){
          cin >> n ;
          cout << "Case #" << ++ cases << ": " ;
          if (n == 1){
                cout << "0" << endl ;
                continue ; 
          }
          mx = 1 ; mn = 0 ;
          for (long long i = 2 ;  
          i <= (long long)(sqrt(n)) ;i ++) if (!f[i]){
              mn ++; 
              long long tmp = n ;
              while (tmp >= i){
                    mx ++ ;
                    tmp = tmp / i ; 
              }
       //       cout << i << endl; 
          }
          
          cout << mx - mn << endl ;
    }
}

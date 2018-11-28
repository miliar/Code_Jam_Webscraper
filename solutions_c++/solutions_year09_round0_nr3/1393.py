#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cctype>
#include <string>
#include <iostream>
#include <algorithm>
#include <queue>
#include <vector>
#include <list>
#include <numeric>
#include <sstream>
#include <functional>
#include <utility>

#define INFINITO  (1<<30)

using namespace std;

string frase = "welcome to code jam";
long long modulo = 10000,total=0;
long long dp[503][20];
int T;
string cadena;

int main(){
 
 
   scanf("%d",&T);
   getchar();
   
    for(int caso=1;caso<=T;caso++){
    
      getline(cin,cadena);
      memset(dp,0,sizeof(dp));
      
      for(int i=0;i<cadena.size();i++) dp[i][0] = cadena[i]==frase[0]?1:0;
      
      
      for(int i=1;i<cadena.size();i++){
        for(int j=1;j<frase.size();j++){
           if( cadena[i] == frase[j]){
             
             for(int k=1;k<=i;k++) dp[i][j] = (dp[i][j] + dp[i-k][j-1])%modulo; 
              
           }     
        }
      }
     total = 0;
     for(int i=0;i<cadena.size();i++) total = (total + dp[i][18])%modulo ;
     
     
     printf("Case #%d: %04lld\n",caso,total);  
    }
  
}


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

int L,D,N,cont,inde,adic;
string dic[5003],q;
bool ok;

int main(){

  scanf("%d%d%d",&L,&D,&N);
  
  for(int i=0;i<D;i++) cin>>dic[i]; 
  
   for(int caso=1;caso<=N;caso++){
     cin>>q;
     cont = 0;
     inde = -1;
     adic = 1;
     bool matrix[20][30]={false}; // i-esima posicion en cadena y letra
     
      for(int i=0;i<q.size();i++)
       if( islower(q[i]) ) inde+=adic,matrix[inde][q[i]-'a'] = true;
       else if( q[i] == '(') inde+=adic,adic=0;
       else if( q[i] == ')') adic=1;inde+=adic;
       
      for(int i=0;i<D;i++){
       ok = true;
        for(int j=0;j<L && ok;j++)
         if( !matrix[j][dic[i][j]-'a']) ok = false;
       
       if(ok) cont++;
      } 
       
       
     printf("Case #%d: %d\n",caso,cont);
   }


}


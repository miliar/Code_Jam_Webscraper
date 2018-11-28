#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <algorithm>
#include <vector>
#include <list>
#include <map>
#include <utility>
#include <sstream>
#include <string>
#include <cstring>
#include <cctype>
#include <cmath>
#include <queue>
#include <stack>
#include <set>

#define all(v) v.begin(),v.end()
#define INFINITO (1LL<<62)
#define eps 1e-07
#define PI  acos(-1.0)
#define REP(i,n) for(int _n=n, i=0;i<_n;++i)
#define FOR(i,a,b) for(int i=(a),_b=(b);i<=_b;++i)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;--i)
#define SGN(x) ((x)<-eps?-1:(x)>eps?1:0)
#define ABS(x) ((x)>0?(x):(-1*(x)))

using namespace std;


int T,N,aux;
string cad;
int A[50];

int main(){
 
  scanf("%d",&T);
  
   for(int caso=1;caso<=T;caso++){
      cin>>N;
      memset(A,0,sizeof(A));
       for(int i=0;i<N;i++){
         cin>>cad;
         for(int j=0;j<N;j++)
          if( cad[j]=='1') A[i]=j;
        }
        bool ok = true;
        int cont=0;
        
        for(int i=0;i<N;i++){
          
          if( A[i]<=i) continue; 
          for(int j=i+1;j<N;j++){
            if( A[j]<=i){
              aux = A[j];
              for(int k=j;k>i;k--) A[k] = A[k-1]; 
              A[i] = aux; 
              cont+=j-i;
              break;
            } 
          }
        }
         
     printf("Case #%d: %d\n",caso,cont);  
   }
 
}


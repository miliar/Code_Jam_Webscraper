#include <iostream>
#include <string>
#include <memory>
#include <cmath>

using namespace std;
typedef long long int LL;

#define SIZE(a) (int)(a.size())
#define LENGTH(a) (int)(a.length())
#define REP(i,n) for(int i=0;i<(n);i++)
#define REPD(i,n) for(int i=(n);i>=0;i--)
#define FOR(i,n,m) for(int i=(n);i<=(m);i++)
#define FORD(i,n,m) for(int i=(n);i>=(m);i--)
#define MIN(a,b) ((a)<(b) ? (a) : (b))
#define MAX(a,b) ((a)<(b) ? (b) : (a))
#define ABS(a) ( (a)<0 ? -(a) : (a))

int main(){
   string vS[101],vQ[1001],aux;
   int tS[101],n,s,q,ini,cambios,may,posmay,band;
   cin>>n;
   REP(cas,n){
      cin>>s; getline(cin,aux);
      REP(i,s) getline(cin,vS[i]);
      cin>>q; getline(cin,aux);
      REP(i,q) getline(cin,vQ[i]);
      ini=0; cambios=0; band=0;
      while(1){
         memset(tS,0,sizeof(tS));
         REP(i,s) 
            FOR(j,ini,q)
               if(vS[i]==vQ[j]){
                  tS[i]=j+1; break;
               }
         may=tS[0]; posmay=0;
         REP(i,s){
            if(tS[i]==0){band=1; break;}         
            if(tS[i]>may){may=tS[i]; posmay=i;}
         }
         if(band==1) break;
         cambios++;
         ini=may-1;         
      }
      cout<<"Case #"<< cas+1 <<": "<<cambios<<endl;           
   }
   return 0;    
}

#include <iostream>
#include <string>
#include <memory>
#include <cmath>
#include <vector>
#include <cctype>
#include <map>

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
#define FOREACH(it,c) for(__typeof((c).begin()) it=(c).begin(); it!=(c).end(); ++it)

int convert(string hora){
   return ((atoi(hora.substr(0,2).c_str())*60)+atoi(hora.substr(3,2).c_str())); 
}

int main(){
   int n,na,nb,t,ma,mb;
   string ini,fin;
   multimap<int,int> INI,FIN,INIR,FINR;

   cin>>n;
   REP(cas,n){
       cin>>t;
       cin>>na>>nb;
       ma=na; mb=nb;
       INI.clear(); FIN.clear();
       INIR.clear(); FINR.clear();
   
       REP(i,na){
          cin>>ini>>fin;
          INI.insert(make_pair(convert(ini),convert(fin)));
          INIR.insert(make_pair(convert(fin),convert(ini)));
       }
       REP(i,nb){
          cin>>ini>>fin;
          FIN.insert(make_pair(convert(ini),convert(fin)));
          FINR.insert(make_pair(convert(fin),convert(ini)));
       }

       FOREACH(itf,FINR)
          FOREACH(iti,INI){
             if((itf->first+t)<=(iti->first)){
                ma--; 
                INI.insert(make_pair(-1,iti->second));
                INI.erase(iti); 
                break;                                                                
             }              
          }
       
       FOREACH(iti,INIR)
          FOREACH(itf,FIN){
             if((iti->first+t)<=(itf->first)){
                mb--; 
                FIN.insert(make_pair(-1,itf->second));
                FIN.erase(itf); 
                break;                                                                
             }              
          }   
          
       cout<<"Case #"<< cas+1 <<": "<<ma<<" "<<mb<<endl;   
       
   }
   return 0;    
}


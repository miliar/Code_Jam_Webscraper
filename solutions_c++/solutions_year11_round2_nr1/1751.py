 #include <algorithm>  
#include <iostream>  
#include <sstream>  
#include <string>  
#include <vector>  
#include <queue>  
#include <set>  
#include <map>  
#include <cstdio>  
#include <cstdlib>  
#include <cctype>  
#include <cmath>  
#include <list>  
#include <inttypes.h>
using namespace std;  

#define PB push_back  
#define MP make_pair  
#define SZ(v) ((int)(v).size())  
#define FOR(i,a,b) for(int i=(a);i<(b);++i)  
#define REP(i,n) FOR(i,0,n)  
#define FORE(i,a,b) for(int i=(a);i<=(b);++i)  
#define REPE(i,n) FORE(i,0,n)  
#define FORSZ(i,a,v) FOR(i,a,SZ(v))  
#define REPSZ(i,v) REP(i,SZ(v))  
typedef unsigned long long int ll;  

vector<string> v;
vector<double> voowp;
vector<double> vowp;
vector<double> vwp;

void run(int casenr) {
	int t;scanf("%d",&t);
    double wp,owp,oowp,awp,rpi;
    int w,l,p;
    v.clear();
    voowp.clear();
    vowp.clear();
    vwp.clear();
    string cad;
	FORE (i,1,t){
         cin>>cad;
         v.push_back(cad);
         }
	printf("Case #%d:\n",casenr);
	FORE (i,0,t-1){
         w=0;l=0;
         cad=v[i];
         FORE (j,0,cad.size()-1){
              if (cad.at(j)=='1')w++;
              if (cad.at(j)=='0')l++;
              }
         wp=(double)w/(double)(w+l);
         vwp.push_back(wp);
         
	     awp=0;
	     p=0;
         FORE (k,0,t-1){
             w=0;l=0;              
             if (k!=i){
                 cad=v[k];
                 if (cad.at(i)!='.'){
                     p++;
                     FORE (j,0,cad.size()-1){
                          if (j!=i){
                             if (cad.at(j)=='1'&&j!=i)w++;
                             if (cad.at(j)=='0'&&j!=i)l++;
                             }
                          }
                     awp+=(double)w/(double)(w+l);
                     }
                 }
             }
         if (p>0)owp=(double)awp/(double)p;else owp=0;
         vowp.push_back(owp);
         }
         
	FORE (i,0,t-1){         
         awp=0;
	     p=0;       
         FORE (k,0,t-1){
              if (k!=i){
                 cad=v[k];
                 if (cad.at(i)!='.'){
                     p++;
                     awp+=vowp[k];
                     }
                 }               
              }
         if (p>0)oowp=(double)awp/(double)p;else oowp=0;
         voowp.push_back(oowp);       
         }

	FORE (i,0,t-1){     
         rpi = (0.25 * vwp[i]) + (0.50 * vowp[i]) + (0.25 * voowp[i]);
         //cout << vwp[i] << "\t" << vowp[i] << "\t" <<voowp[i] << " ) ";
         cout << rpi << endl;
         }         
         
}

int main() {
	int n; scanf("%d",&n); FORE(i,1,n) run(i);
	return 0;
}

 

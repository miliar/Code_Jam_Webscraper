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



void run(int casenr) {
     char m[51][51];
     char car;
    int r,c; scanf("%d %d",&r,&c);
    FORE (i,0,r-1)scanf("%s",&m[i]);
    FORE (i,0,r-1)
         FORE (j,0,c-1){
              if (m[i][j]=='#'){
                    FORE (i2,0,1)
                         FORE (j2,0,1){          
                             switch (2*i2+j2){
                                    case 0:car='/'; break;
                                    case 1:car='\\'; break;
                                    case 2:car='\\'; break;
                                    case 3:car='/'; break;                                                                                                                        
                                    }
                             if (m[i+i2][j+j2]=='#'||m[i+i2][j+j2]==car)
                                m[i+i2][j+j2]=car;
                                else
                                    goto adios;
                             }
                    }
              
              }
         
    
	printf("Case #%d:\n",casenr);
    FORE (i,0,r-1)printf("%s\n",m[i]);
	goto salir;
	
	adios:
         	printf("Case #%d:\nImpossible\n",casenr);
    
    salir:
    ;
 }

int main() {
	int n; scanf("%d",&n); FORE(i,1,n) run(i);
	return 0;
}

 

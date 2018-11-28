#pragma warning(disable:4018)  // signed/unsigned mistatch
#pragma warning(disable:4244)  // w64 to int cast
#pragma warning(disable:4267)  // big to small -- possible loss of data
#pragma warning(disable:4786)  // long identifiers
#pragma warning(disable:4800)  // forcing int to bool
#pragma warning(disable:4996)  // deprecations
#include "assert.h"
#include "ctype.h"
#include "float.h"
#include "math.h"
#include "stdio.h"
#include "string.h"
#include "stdlib.h"
#include "stdarg.h"
#include "time.h"
#include "algorithm"
#include "numeric"
#include "functional"
#include "utility"
#include "bitset"
#include "vector"
#include "list"
#include "set"
#include "map"
#include "queue"
#include "stack"
#include "string"
#include "sstream"
#include "iostream"
#define all(v) (v).begin(), (v).end()
typedef long long i64;
template <class T> void make_unique(T& v) {sort(all(v)); v.resize(unique(all(v)) - v.begin());}
using namespace std;

int sol(vector < pair <char,int> > &v , int n){
    int ro1=1,ro2=1,sig=0,res=0,t=0; 
    char m=v[0].first;
    
    for(int i=0; i<n; ++i){
            if(v[i].first==m){
                              if(v[i].first=='O'){
                                                 sig += abs(ro1 - v[i].second)+1;
                                                  ro1=v[i].second;
                                                  }
                              else{
                                                  sig += abs(ro2 - v[i].second)+1;
                                                  ro2=v[i].second;        
                                   }
                              
                              }
            else {
                              res += sig;
                              t= sig;
                              m=v[i].first; 
                              if(m=='O'){
                                         sig= max(0, abs(ro1 - v[i].second)-t)+1; 
                                         ro1=v[i].second;
                                         }
                              else{
                                         sig= max(0, abs(ro2 - v[i].second)-t)+1; 
                                         ro2=v[i].second;
                                   
                                   }
                                   }
                                   }
    
    res+= sig; 
    return res; 
    }



int main(){
    freopen("data.in","r",stdin);
	freopen("data.out", "w", stdout);
    int casos, n;
    scanf("%d",&casos); 
    for (int p=1;p<=casos; ++p ){
        scanf("%d",&n); 
        vector < pair <char,int> > g(n); 
        for(int i=0; i<n; i++){
                scanf(" %c %d", &g[i].first, &g[i].second);} 
        int k= sol(g,n);
        //printf("%d\n",res); 
        printf("Case #%d: %d\n",p,k);
        }
    
    
    
return 0;     
}

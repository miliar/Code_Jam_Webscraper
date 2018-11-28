#include <cstring>
#include <string>
#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <map>
#include <set>

using namespace std;

#define MAXN 2000001
#define INF (1<<30)

set <int>  res[MAXN];

void precompute(){
  for(int i=0; i<MAXN; ++i) res[i].clear();
  int s = 1; int e = 10; int pow = 1; 
  for(int i=1; i<=7; ++i){
     for(int j=s; j<e; ++j){
         if(j>=MAXN) return; int num = j;
         for(int k=1; k<i; ++k){
              int d = num%10; num = d*pow+num/10;
              if(d!=0 && num>j) res[j].insert(num);;
         }
   }
   s *= 10; e *= 10; pow *= 10;
  }
  return; 
}
int tcase;
int A,B;
int main(){
    precompute(); scanf("%d",&tcase);
    for(int tc=1; tc<=tcase; ++tc){
        scanf("%d%d",&A,&B); long long r = 0;
        for(int i=A; i<=B; ++i) 
         for(set<int>::iterator it = res[i].begin(); it!=res[i].end(); ++it) 
              if((*it)<=B) ++r; 
        printf("Case #%d: %lld\n",tc,r);
    }
    return 0;
}

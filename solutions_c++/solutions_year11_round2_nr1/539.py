#include <cstring>
#include <string>
#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <queue>
#include <sstream>
#include <cmath>
#include <cstdlib>
#include <climits>

using namespace std;
typedef long long int64;

#define maxn 200
int n;
char A[maxn][maxn];
double W[maxn],OW[maxn],OWW[maxn];

int main(){
  int tcase; scanf("%d",&tcase);
  
  for(int tc=1;tc<=tcase;++tc){
    scanf("%d",&n);
    for(int i=0;i<n;++i) scanf("%s",A[i]);
    for(int i=0;i<n;++i){
       int tc = 0; int wn = 0;
       for(int j=0;j<n;++j) if(A[i][j]=='0' || A[i][j]=='1') {
           ++tc; if(A[i][j]=='1') ++wn;
       }
       W[i] = wn*1.0/tc;
    }
    for(int i=0;i<n;++i){
      int ct = 0;  double sm = 0;
      for(int j=0;j<n;++j) if(A[i][j]!='.') {
         ++ct;
         int tc = 0; int wn = 0;
         for(int k=0;k<n;++k) if(A[j][k]!='.' && k!=i){
             ++tc; if(A[j][k]=='1') ++wn;
         }
         sm += wn*1.0/tc;
      }
      OW[i] = sm / ct;  
    }
    for(int i=0;i<n;++i){
      double sm =0 ; int ct = 0;
      for(int j=0;j<n;++j) if(A[i][j]!='.'){
          sm += OW[j]; ct++;
      }
      OWW[i] = sm/ct;
    }
    printf("Case #%d:\n",tc);
    for(int i=0;i<n;++i) 
      printf("%.9lf\n",0.25*W[i]+0.5*OW[i]+0.25*OWW[i]);
  }

  return 0;
}

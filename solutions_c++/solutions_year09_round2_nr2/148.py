#include <stdio.h>
#include <vector>
#include <algorithm>
#include <string>
#include <sstream>
#include <iostream>
#include <map>
#include <math.h>
#include <set>
#include <queue>
using namespace std;
typedef long long LL;
#define INF 1000000000
#define SZ(v) ((int)(v).size())
#define FOR(i,a,b) for(int i=(a);i<(b);i++)
#define REP(i,n) FOR(i,0,n)
#define FORE(i,a,b) for(int i=(a);i<=(b);i++) 

char L[1000];

int tab[100];
int main(){
   int T;
   scanf("%d\n",&T);
   FORE(test,1,T){
      fgets(L,1000,stdin);
      string s(L);
      int d = 0;
      FOR(i,0,SZ(s)){
         if(s[i]>='0' && s[i]<='9'){
            tab[d++] = s[i]-'0';
         }   
         else break;
      }
      printf("Case #%d: ",test);
      if(next_permutation(tab,tab+d)) FOR(i,0,d) printf("%d",tab[i]);
      else{
         sort(tab,tab+d);
         int p = 0,ind;
         FOR(i,0,d) if(tab[i]==0) p++;
         FOR(i,0,d){
            if(tab[i]!=0){
               printf("%d",tab[i]);
               ind = i;
               break;
            }
         }
         FOR(i,0,p+1) printf("0");
         FOR(i,0,d){
            if(tab[i]!=0 && i!=ind) printf("%d",tab[i]); 
         }
      }
      printf("\n");
   }

}

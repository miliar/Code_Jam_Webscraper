#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
#include <cstdio>
#include <string>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <string.h>
#include <cassert>

using namespace std;

#define GI ({int t;scanf("%d",&t);t;})
#define FOR(i,a,b) for(int i=a;i<b;i++)
#define REP(i,n) FOR(i,0,n)
#define pb push_back
#define sz size()
#define INF (int)1e9

typedef long long LL;
typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<vector<int> > VVI;
typedef pair<char,char> PCC;
typedef map<PCC,char> M;

int main() {
   int t;
   scanf("%d",&t);
   for(int tc=1;tc<=t;tc++) {
      int C,N,D;
      char ANS[200];
      int tos=0;
      M combination;
      map<char,char> oppose;
      
      scanf("%d",&C);
      
      char temp[10];
      for(int i=0;i<C;i++) {
         scanf("%s",temp);
         combination[make_pair(temp[0],temp[1])]=temp[2];
         combination[make_pair(temp[1],temp[0])]=temp[2];
      }
      
      
     scanf("%d",&D);
      
     for(int i=0;i<D;i++) {
         scanf("%s",temp);
         oppose[temp[0]]=temp[1];
         oppose[temp[1]]=temp[0];
      }
 
    
      scanf("%d ",&N);
      
      char ch;
      for(int i=0;i<N;i++) {
         scanf("%c",&ch);
         bool oppose_check=0;
     //    printf("%c",ch);
         
     /*    printf("Printing ANS\n");
         for(int i=0;i<tos;i++) {
            printf("%c ",ANS[i]);         
         }
         printf("\n");*/
         
         if(tos==0) {
         ANS[tos++] = ch;
         continue;
         }
        
         else {
            
            if(combination[make_pair(ch,ANS[tos-1])]) {
            tos--;
            ANS[tos] = combination[make_pair(ch,ANS[tos])];
            tos++;
            continue;
            }
            
            else {
                  for(int i=0;i<tos;i++) {
                        if(oppose[ch]==ANS[i]) {
                        tos=0;
                        oppose_check=1;
                        break;
                        }            
                   }            
            }
            
            if(oppose_check)
            continue;
            else        
            ANS[tos++] = ch;
            
         }      
      }

      printf("Case #%d: [",tc);
      for(int i=0;i<tos;i++) {
         if(i<tos-1)
         printf("%c, ",ANS[i]);
         else
         printf("%c",ANS[i]);
      }
      printf("]\n");

   
   }
   return 0;
}


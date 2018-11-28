#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <string>
#include <vector>
#include <queue>

#define REP(a,b) for (int a=0; a<b; a++)
#define FORU(a,b,c) for (int a=b; a<=c; a++)
#define FORD(a,b,c) for (int a=b; a>=c; a--)
#define RESET(a,b) memset(a,b,sizeof a)

#define PII pair<int,int> 
#define FI first
#define SE second
#define MP make_pair
#define PB push_back

#define __ puts("")
using namespace std;

bool a1,a2;
int nkasus;
int n,perm[20];
int tot1,tot2,ma,tota;

int main(){
//   freopen("in.in", "r", stdin);
//   freopen("ot.out", "w", stdout);
   
   scanf("%d", &nkasus);
   
   REP(jt,nkasus){
      scanf("%d", &n);
      
      REP(i,n){
         scanf("%d", &perm[i]);  
      }
      
      ma=-1;
      REP(i,1<<n){
         tot1=0;
         tot2=0;
         tota=0;
         a1=0;
         a2=0;
         
         REP(j,n){
            if (i & (1<<j)){
               tot1^=perm[j];  
               tota+=perm[j];
               a1=1;
            }else{
               tot2^=perm[j];
               a2=1;
            }  
         } 
         
//         cout <<i<<" : "<< tot1 << " " << tot2 << endl;
         if ((tot1 == tot2) && (a1) && (a2)){
            ma=max(ma, tota);
         } 
      }
      
      printf("Case #%d: ", jt+1);
      if (ma == -1){
         printf("NO\n");
      }else{
         printf("%d\n", ma);
      }
   }  
   
   return 0;  
}

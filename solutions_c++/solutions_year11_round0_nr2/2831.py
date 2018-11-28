#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <string>
#include <vector>

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

int ada[300];
int nkasus,no,ns,nc,u,v,w;
int jadi[300][300],ancu[300][300];
char sc[105];
vector<int> ve;

int main(){
//   freopen("in.txt", "r", stdin);
//   freopen("ot.out", "w", stdout);
   
   scanf("%d", &nkasus);
   REP(jt,nkasus){
      RESET(jadi,-1);
      RESET(ancu,-1);
      
      scanf("%d", &nc);
      REP(i,nc){
         scanf("%s", sc);
         
         u=sc[0];
         v=sc[1];
         w=sc[2];
         
         jadi[u][v]=w;
         jadi[v][u]=w;  
      }
      
      scanf("%d", &no);
      REP(i,no){
         scanf("%s", sc);
         
         u=sc[0];
         v=sc[1];
         
         ancu[u][v]=1;
         ancu[v][u]=1;  
      }
      
      scanf("%d", &ns);
      scanf("%s", sc);
   
      ve.clear();
      RESET(ada,0);
      REP(i,ns){
         v=sc[i];
         if (ve.size() >= 1){
            u=ve.back();
         
            if (jadi[u][v] != -1){
               ada[u]--;
               
               ve.pop_back();
               ve.PB(jadi[u][v]);
               ada[jadi[u][v]]++;
            }else{
               ada[v]++;
               ve.PB(v);  
            }
         }else{
            ada[v]++;
            ve.PB(v);  
         }
      
         //ilang kah?
         if (ve.size() >= 1){
            REP(j,300){
               if ((ada[j]>0) && (ancu[j][ve.back()] == 1)){
                  RESET(ada,0);
                  ve.clear();
                  
                  break;
               } 
            }  
         }
      }
      
      printf("Case #%d: [", jt+1);
      if (ve.size() == 0){
         printf("]\n");
      }else{
         printf("%c", ve[0]);
         
         FORU(i,1,ve.size()-1){
            printf(", %c", ve[i]);  
         }
         printf("]\n");
      }
   }
   return 0;  
}

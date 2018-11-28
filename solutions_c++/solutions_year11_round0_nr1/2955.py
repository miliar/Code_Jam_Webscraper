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

int pa,pb;
queue<int> qa,qb,qq;
int nkasus,dor,ntom,tot,u;
char sc[10];

int main(){
//   freopen("in.in", "r", stdin);
//   freopen("ot.out", "w", stdout);
   
   scanf("%d", &nkasus);
   REP(jt,nkasus){
      scanf("%d", &ntom);
   
      REP(i,ntom){
         scanf("%s%d", sc,&u);
         
         if (sc[0] == 'O'){
            qa.push(u);
            qq.push(0); 
         }else{
            qb.push(u);
            qq.push(1);
         }  
      }  
      
      pa=1;
      pb=1;
      tot=0;
      while (!qq.empty()){
         dor=0;
         if (!qa.empty()){
            if (pa < qa.front()){
               pa++;
            }else if (pa > qa.front()){
               pa--;  
            }else if (qq.front() == 0){
               qa.pop();  
               qq.pop();
               dor=1;
            }   
         }
         
         if (!qb.empty()){
            if (pb < qb.front()){
               pb++;  
            }else if (pb > qb.front()){
               pb--;
            }else if ((qq.front() == 1) && (dor==0)){
               qb.pop();
               qq.pop();
            }
         }
         tot++;
//         printf("%d %d %d\n", tot, pa,pb);
      }
      
      printf("Case #%d: %d\n", jt+1, tot);
   }
   
   return 0;  
}

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
      int N; 
      scanf("%d",&N);
      int ans=0;
      int orange=0;
      int blue=0;
      int prev_blue=1;
      int loc_orange=1;
      int loc_blue=1;
      int prev_orange=1;
      
      
      char bot; int loc;
      
      for(int i=0;i<N;i++) {
         scanf(" %c %d",&bot,&loc);
      //     printf("Case #%d: %d\n",tc,ans);
         
         int temp;
         if(bot=='O') {
              loc_orange = loc;
              temp=(loc_orange-prev_orange);         
         }
         else {
               loc_blue = loc;
               temp=(loc_blue-prev_blue);
         }
         
         if(temp<0)
         temp*=-1;
         
         temp++;
        
         //printf("INITIALLY%c %d=>prev_blue=%d&prev_orange=%d&orange=%d&blue%d&temp=%d\t",bot,loc,prev_blue,prev_orange,orange,blue,temp);
     
         
         if(i==0) {
            ans+=temp;
            if(bot=='O') {
            orange=0;            
            blue = temp;
            }
            else {
            blue=0;
            orange=temp;
            }         
            //continue;
         }
         
         else {
            if(bot=='O') {
               if(temp-orange>0) {
                  ans+=temp-orange; 
                  blue+=temp-orange;
                 }
               else {
                  ans+=1;
                  blue+=1;
               }              
               orange=0;                          
            }
            else {
              if(temp-blue>0) {
                  ans+=temp-blue; 
                  orange+=temp-blue;
               }
               else {
                  ans+=1;
                  orange+=1;
               }              
               blue=0;
            }
         
         }
        prev_orange=loc_orange;         
        prev_blue=loc_blue;         
      //  printf("FINALLY : orange=%d&blue%d&temp=%d\n",orange,blue,temp);
        //printf("%c %d=>%d\n",bot,loc,ans);
      }
      
         
      
     
      printf("Case #%d: %d\n",tc,ans);
     

   
   }
   return 0;
}


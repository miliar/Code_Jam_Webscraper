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
      int C[N]; int sum=0;
      for(int i=0;i<N;i++) {
         scanf("%d",&C[i]);
         sum+=C[i];
      }
      
      int X=(1<<(N))-2;
      
      bool possible=0; int SEAN=0;
      
      for(int A=1;A<=X;A++) {  
       //  printf("%d\n",A);       
         int cnt=0; int patrik=0;int sean=0;
         for(int Y=1;cnt<N;Y*=2) {          
            if(A&Y){
               patrik=patrik^C[cnt];
            }
            else {
               sean+=C[cnt];
            }
            cnt++;      
         }
        // printf("A=%d sean=%d patrik=%d\n",A,sean,patrik);
         if(sean==patrik) {
         possible = 1;
         if(SEAN<sean)
         SEAN=sean;
         if(SEAN<(sum-sean))
         SEAN=sum-sean;
         //break;
         }
      }
      
      
      
      
      
      if(possible)
      printf("Case #%d: %d\n",tc,SEAN);
      else
      printf("Case #%d: NO\n",tc);

   
   }
   return 0;
}


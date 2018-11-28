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
typedef pair<int,int> PII;

int main() {
   int testcases;
   int L,t,N,C,a;
   scanf("%d",&testcases);
   for(int tc=1;tc<=testcases;tc++) {
      scanf("%d %d %d %d",&L,&t,&N,&C);
      int Arr[N];
      for(int i=0;i<C;i++) {
         scanf("%d",&a);
         for(int k=0;(k+i)<N;k=k+C)
         Arr[k+i] = a;
      }

      int sum=0;
  
     for(int i=0;i<N;i++) {
  //       printf("%d ",Arr[i]);
         sum+=Arr[i];
      }
      int ans=sum*2;

   
      
      int Arr_2[N];
      
      for(int i=0;i<N;i++) {
         Arr_2[i]=Arr[i];     
      }
      
      int tmp_sum=0;
      
      for(int i=0;i<N;i++) {
         tmp_sum+=Arr[i];
//         printf("%d ",tmp_sum);
         if((tmp_sum)>(t/2)) {
         Arr[i] = tmp_sum-(t/2);   
         break;         
         }
         Arr[i] = 0;
      }
      
      
      for(int a=0;a<N;a++) {
         for(int i=0;i<(N-1);i++) {
            if(Arr_2[i]<Arr_2[i+1]) {
               int temp=Arr_2[i+1];
               Arr_2[i+1] = Arr_2[i];
               Arr_2[i] = temp;
               temp=Arr[i+1];
               Arr[i+1] = Arr[i];
               Arr[i] = temp;               
            }      
         }
      }
      
    /*  for(int i=0;i<N;i++) {
         printf("%d ",Arr[i]);
      }
      printf("\n");
      for(int i=0;i<N;i++) {
         printf("%d ",Arr_2[i]);
      }*/

     for(int a=0;a<N;a++) {
         for(int i=0;i<(N-1);i++) {
            if(Arr[i]<Arr[i+1]) {
               int temp=Arr[i+1];
               Arr[i+1] = Arr[i];
               Arr[i] = temp;               
            }      
         }
      }


      int diff=0;
      
      for(int i=0;i<N && L>0;i++) {
         diff+=Arr[i];
         L--;
      }
      
      ans = ans-diff;
      
      
  
      printf("Case #%d: %d\n",tc,ans);
      
   
   }
   return 0;
}


#include<iostream>
#include<queue.h>
using namespace std;
int main()
{
    int T,R,k,N,ride,Case,i,g,max,count,profit;
    queue<int> q;
    scanf("%d",&T);
    for(Case=1;Case<=T;Case++)
    {
         scanf("%d%d%d",&R,&k,&N);
         profit=max=0;
         for(i=0;i<N;i++){
              scanf("%d",&g);
              max+=g;
              q.push(g);
         }
         count=0;
//         printf("Scanned is %d\n",q.front());
         for(ride=0;ride<R;ride++){
              while(1){
                 count+=q.front();
                 if(count<=k&&count<=max){
                     q.push(q.front());
                     q.pop();
                 } else {
                     break;
                 }
              }
//              printf("Count is %d front is %d\n",count,q.front());
              count-=q.front();
              profit+=count;
//              printf("Profit on round %d is %d\n",ride+1,count);
              count=0;
         }
         printf("Case #%d: %d",Case,profit);
         if(Case!=T) printf("\n");
         while(!q.empty()) q.pop();
    }
   return 0;
}

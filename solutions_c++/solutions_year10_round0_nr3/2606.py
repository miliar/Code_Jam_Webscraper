#include "iostream"
#include "queue"

using namespace std;
int s[1001],p[1001];
queue<int> q;
int r , t ,n ,k;
int make_money()
{
     
     int  i = 0,temp ,person = 0;
     while(!q.empty()&&person <= k)
     {
            temp = q.front();
            if(person + temp > k)
               break;
            q.pop();
            p[i++] = temp;
            person += temp;
           
     }
     for(int j = 0 ; j < i ;j++) 
         q.push(p[j]); 
     return person;
}  
            
int main()
{
     
      freopen("C-small-attempt0.in","r",stdin);
      freopen("C-small-attempt0.out","w",stdout);
      scanf("%d",&t);
      for(int v = 1 ; v <= t ; v++)
      {   
          int sum = 0;
          while(!q.empty())
          {
              q.pop();
          }            
          scanf("%d%d%d",&r ,&k ,&n);    
          for(int i = 0 ; i < n;i++)
          {
              scanf("%d",&s[i]);
              q.push(s[i]);
          }
          while(r--)
          {
              sum += make_money();
          } 
          printf("Case #%d: %d\n",v , sum); 
      }    
     // while(1); 
      return 0;
      
}    

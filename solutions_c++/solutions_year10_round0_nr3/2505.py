#include<iostream>
#include<queue>
using namespace std;
int main()
{
    long long t,r,k,n,i,g[1001],cost,sum,item,count,j;
    cin>>t;
    j=1;
    while(t--)
    {
        queue <long long> q1,q2;
        cin>>r>>k>>n;
        for(i=0;i<n;i++)
        {
            cin>>g[i];
            q1.push(g[i]);
        }
        cost=0;
        while(r--)
        {
          sum=0;
          count=0;
          while(sum<=k && !q1.empty())
          {     
              item=q1.front();
              sum+=item;
              if(sum>k)
              {
                 sum=sum-item;
                 break;
              }
              q1.pop();
              q2.push(item);
              count++;
          }
          while(count--)
          {
             q1.push(q2.front());
             q2.pop();
          }
          cost+=sum;
        }   
        cout<<"Case #"<<j++<<": "<<cost<<endl;
    }
    return 0;
}         

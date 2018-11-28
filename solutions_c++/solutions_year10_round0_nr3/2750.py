#include<iostream>
#include<queue>
#include<vector>
using namespace std;
#define pb push_back
int main()
{
   int t,c1=0;
   cin>>t;
   while(t--)
   {
      c1++;
      long long ch,sum=0,i,gi,j,r,k,n,c=0,nt=0,ts=0,r1;
      queue<long long>g,qn;
      vector<long long>e;
      cin>>r>>k>>n;
      for(i=0;i<n;i++)
        {cin>>gi;   
         g.push(gi); 
         qn.push(c);
         c++;
        }
      r1=r;  
      //cout<<"r k"<<r<<" "<<k<<endl;
     do{
         sum=0;
         nt++;
         queue<long long>b;
         for(i=0;i<n && sum+g.front()<=k;i++)
           {sum+=g.front();
            ch=g.front();
            b.push(ch);
            g.pop();
           }
        // cout<<"sum="<<sum<<endl;  
         for(j=0;j<i;j++)
            { ch=b.front();
              b.pop();
              g.push(ch);
              ch=qn.front();
              qn.pop();
              qn.push(ch);
             
            }
         e.pb(sum);
         r1--;
         ts+=sum;
       }while(r1>0);    
     // for(i=0;i<e.size();i++) cout<<e[i]<<" "<<endl;
      //cout<<"\n";
     /*if(r1)
     {
        ts=ts*(r/nt);
        r=r%nt;
        if(r) ts+=e[r-1];
     }*/
      cout<<"Case #"<<c1<<": "<<ts<<endl;
   }
   return 0;
}
   
             
         
         

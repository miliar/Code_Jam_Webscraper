#include<iostream>
using namespace std;
int sc[110];
int main()
{  
    int t,a=1;
    cin>>t;
    while(t--)
    {
         int n,s,p,ans=0;
         cin>>n>>s>>p;         
         for(int i=0;i<n;i++) 
           cin>>sc[i];
         if(p==0)
         {
            ans=n;
         }
         else
         {
            for(int i=0;i<n;i++)
            {
               int normalbest=sc[i]/3+(sc[i]%3!=0);     
               if(normalbest>=p)
               {
                 ans++;
                 sc[i]=0;
               }
               if(sc[i]==29 || sc[i]==30 || sc[i]==1 || sc[i]%3==1) sc[i]=0;
            } 
            sort(sc,sc+n);
            //for(int i=n-1;i>=0;i--) cout<<sc[i]<<" ";
            //cout<<"\n";
            for(int i=n-1;i>=0;i--)
            {
               if(sc[i]!=0 && s>0)
               {
                 int surbest=sc[i]/3+(sc[i]%3!=0)+1;     
                 if(surbest>=p)
                 {
                   ans++;                           
                   s--;
                 }
               }     
            }
         }
         printf("Case #%d: %d\n",a++,ans);
              
    }
}

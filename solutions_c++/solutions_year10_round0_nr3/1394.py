#include <iostream>
#include <stdio.h>

using namespace std;


long long inp[1004];
long long t,r,k,n,cur;
long long top,tor,curp;
int main()
{
     freopen("c.in","r",stdin);
    freopen("c.txt","w",stdout);
    scanf("%d",&t);
    
    for(int gl=1;gl<=t;gl++)
    {
        scanf("%d%d%d",&r,&k,&n);
        top=0;tor=0;curp=0;
        
        for(int i=0;i<n;i++)   scanf("%d",&inp[i]);            
            
        long long ct=0,pct=0;    
         while(tor<r)
        {
            if(ct>=n) ct=0; 
            cur= inp[ct];
            
                if(  pct==n || (curp+cur)>k )
                {
                   // cout<<curp<<" "<<tor<<endl;
                    top+=curp;
                    curp=cur;
                    tor++;
                    pct=1;
                }
                else 
                {
                    curp+=cur;
                    pct++;
                }
                
                ct++;
            
         }
         
         //if(tor<r) top+=curp;
         
         cout<<"Case #"<<gl<<": "<<top<<endl;
    }
    return 0;
}

            
            
    

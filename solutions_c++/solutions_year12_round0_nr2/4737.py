#include<iostream>
#include<cmath>
using namespace std;

int main()
{
    long n,s,t,p,pts[1100],i,j,k,cs;
    
    
    freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
    cin>>t;
    
    cs=0;
    while(t--)
    {
       cin>>n>>s>>p;
       for(i=0;i<n;i++) cin>>pts[i];
       k=0;   
       for(i=0;i<n;i++)
       {
           j=pts[i]/3;
           
           if(j>=p) k++;
           else if(p-j==1 && pts[i]%3>=1)
           {
               k++;     
           }
           else if(s && p-j==1 && (pts[i]%3==0 && pts[i]))
           {
               s--;
               k++;     
           }
           else if(s && p-j==2 && pts[i]%3==2)
           {
               k++;
               s--;     
           }
           
               
       }
       cout<<"Case #"<<++cs<<": "<<k<<endl;
                 
    }

    return 0;    
}


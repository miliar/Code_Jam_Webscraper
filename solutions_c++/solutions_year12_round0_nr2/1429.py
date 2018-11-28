#include<iostream>
using namespace std;
int main()
{
     freopen("A3.in","r",stdin);
    freopen("GCJO2L.txt","w",stdout);
    
    int t,x=0;
    cin>>t;
    while(t--)
    {
           int n,s,p,i,j,ans=0,ones=0;
           cin>>n>>s>>p;
           int a[101];  
           
           for(i=0;i<n;i++)
           {
                  cin>>a[i];
                  if(a[i]) ones++;
           } 
           
           if(p==0)
           {
                cout<<"Case #"<<++x<<": "<<n<<endl;
                continue;
           }  
           
           if(p==1)
           {
                   cout<<"Case #"<<++x<<": "<<ones<<endl;
                   continue;
           
           }
           
           for(i=0;i<n;i++)
           {
                    if(a[i]<(p*3-4)) continue;
                    if(a[i]>=(p*3-2))
                    {
                             ans++;
                             continue;
                    }
                    if(s==0) continue;
                    ans++;
                    s--;
           }
           cout<<"Case #"<<++x<<": "<<ans<<endl; 
    }
}              
                    

#include<iostream>
using namespace std;
int main()
{int t,i,l,p,c,k,ans;
    cin>>t;
    for(i=0;i<t;i++)
    {
                    cin>>l>>p>>c;
                    ans=0;
                    k=l;
                    k=k*c;
                    while(k<p)
                    {ans++;
                    k=k*c;
                    c=c*c;}
                    cout<<"Case #"<<i+1<<": "<<ans<<endl;
                    }
                    return 0;
                    }
                    

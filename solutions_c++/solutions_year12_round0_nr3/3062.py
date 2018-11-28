#include<iostream>
#include<cstring>
using namespace std;
int tonum(string s, int n)
{
    int num=0,i;
    for(i=0;i<n;i++)
                    num=num*10+(s[i]-'0');
    return num;
}
    
int main()
{
    int t;
    cin>>t;
    int cases=0;
    while(t--)
    {
              
              string str1,str2;
              int ans=0;
              cin>>str1>>str2;
              int k=str1.length();
             // cout<<k;
              if(k==1)
              {
              }
              else if(k==4)
              {
              }
              else if (k==2)
              {
                   int n1=tonum(str1,2);
                   int n2=tonum(str2,2);
                   //cout<<n1<<"  "<<n2<<endl;
                   int i;
                   for(i=n1;i<=n2;i++)
                   {
                           int mod=i%10;
                           mod=mod*10;
                           int l=i/10;
                           int p=mod+ l;
                           if(p>i&&p<=n2)
                          { ans++;
                          //cout<<p<<endl;
                          }
                   }
              }
              else if (k==3)
              {
                   int n1=tonum(str1,3);
                   int n2=tonum(str2,3);
                    //cout<<n1<<"  "<<n2<<endl;
                   int i;
                   for(i=n1;i<=n2;i++)
                   {
                           int mod=i%10;
                           mod=mod*100;
                           int l=i/10;
                           int p=mod+ l;
                           if(p>i&&p<=n2)
                           ans++;
                           mod=i%100;
                           mod=mod*10;
                           l=i/100;
                           p=mod+l;
                           if(p>i&&p<=n2)
                           ans++;
                           
                   }
              }
              cout<<"Case #"<<++cases<<": "<<ans<<endl;
    }
}            
                   

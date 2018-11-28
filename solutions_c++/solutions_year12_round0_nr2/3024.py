#include<iostream>
using namespace std;
int main()
{
    int t;
    cin>>t;
    int cases=0;
    while(t--)
    {
              int n,s,p,ar[100],i;
              cin>>n>>s>>p;
              for(i=0;i<n;i++)
              cin>>ar[i];
              int c1=0,c2=0,c3=0,c4=0,c5,ans=0;
              int cnt=0;
              for(i=0;i<n;i++)
              {
                              if(ar[i]>=3*p)
                              {
                                            ans++;
                                            c1++;
                              }
                              if(ar[i]==3*p-1 &&p-1>=0)
                              {
                                             ans++;
                                             c2++;
                              }
                              if(ar[i]==3*p-2 && p-1>=0)
                              {
                                              ans++;
                                              c3++;
                              }
                              if(ar[i]==3*p-3 &&p-2>=0)
                              {
                                              ans++;
                                              c4++;
                                              cnt++;
                              }
                              if(ar[i]==3*p-4 &&p-2>=0)
                              {
                                              ans++;
                                              c5++;
                                              cnt++;
                              }
              }
              if (cnt<=s)
               cout<<"Case #"<<++cases<<": "<<ans<<endl;
            else
                cout<<"Case #"<<++cases<<": "<<ans-(cnt-s)<<endl;
}
}                              
                              

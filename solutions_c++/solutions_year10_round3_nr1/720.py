#include<iostream>
using namespace std;
int main()
{int t,k,i,j,ans,a[1002],b[1002],n;
    cin>>t;
    for(k=0;k<t;k++)
    {cin>>n;
    ans=0;
    for(i=0;i<n;i++)
    {
                    cin>>a[i]>>b[i];
                    }
                    for(i=0;i<n;i++)
                    {
                                    for(j=0;j<n;j++)
                                    {
                                                    if(((a[i]-a[j])*(b[i]-b[j]))<0)
                                                    ans++;
                                                    }}
                                                    cout<<"Case #"<<k+1<<": "<<ans/2<<endl;
                                                    }
                                                    return 0;
                                                    }
                                                    

#include<iostream>
#include<cstdio>
#include<conio.h>
#include<string.h>
using namespace std;

int main()
{
    freopen("input.in","r",stdin);
    freopen("output.out","w+",stdout);
    
    int t;
    cin>>t;
    int count[31];
    int ccount[31];
    int temp;
    int i,j;
    int n,s,p;
    
    for(i=0;i<t;i++)
    {
                    cout<<"Case #"<<(i+1)<<": ";
                    for(j=0;j<31;j++)
                    {
                                     count[j]=0;
                                     ccount[j]=0;
                    }
                    
                    cin>>n;
                    cin>>s;
                    cin>>p;
                    
                    for(j=0;j<n;j++)
                    {
                                    cin>>temp;
                                    count[temp]++;
                    }
                    
                    ccount[30]=count[30];
                    for(j=29;j>=0;j--)
                    {
                                      ccount[j]=count[j]+ccount[j+1];
                    }
                    
                    /*for(j=0;j<31;j++)
                    {cout<<j<<" "<<ccount[j]<<endl;}*/
                    
                    if(p==0)
                    {
                            cout<<ccount[0]<<endl;
                    }
                    else if(p==1)
                    {
                         cout<<ccount[1]<<endl;
                    }
                    else if(p>1)
                    {
                        int p1=0,p2=0,p3=0;
                        int n1=0,n2=0;
                        p1=3*p-2;
                        p2=3*p-3;
                        p3=3*p-4;
                        
                        n1=ccount[p1];
                        n2=count[p2]+count[p3];
                        
                        if(s<=n2)
                        {
                                 n2=s;
                        }
                        
                        n1=n1+n2;
                        cout<<n1<<endl;
                    }
    }
}
                    
                    

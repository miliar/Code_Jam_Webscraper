#include<iostream>
#include<cstdio>
#include<conio.h>
#include<string.h>
using namespace std;

int main()
{
    freopen("input.in","r",stdin);
    freopen("output.out","w+",stdout);
    int n,s,p;
    int t;
    cin>>t;
    int c[31];
    int cc[31];
    int tmp;
    int i,j;
    
    
    for(i=0;i<t;i++)
    {
                    cout<<"Case #"<<(i+1)<<": ";
                    for(j=0;j<31;j++)
                    {
                                     c[j]=0;
                                     cc[j]=0;
                    }
                    
                    cin>>n;
                    cin>>s;
                    cin>>p;
                    
                    for(j=0;j<n;j++)
                    {
                                    cin>>tmp;
                                    c[tmp]++;
                    }
                    
                    cc[30]=c[30];
                    for(j=29;j>=0;j--)
                    {
                                      cc[j]=c[j]+cc[j+1];
                    }
                    
                    /*for(j=0;j<31;j++)
                    {cout<<j<<" "<<cc[j]<<endl;}*/
                    
                    if(p==0)
                    {
                            cout<<cc[0]<<endl;
                    }
                    else if(p==1)
                    {
                         cout<<cc[1]<<endl;
                    }
                    else if(p>1)
                    {
                        int p1=0,p2=0,p3=0;
                        int n1=0,n2=0;
                        p1=3*p-2;
                        p2=3*p-3;
                        p3=3*p-4;
                        
                        n1=cc[p1];
                        n2=c[p2]+c[p3];
                        
                        if(s<=n2)
                        {
                                 n2=s;
                        }
                        
                        n1=n1+n2;
                        cout<<n1<<endl;
                    }
    }
}
                    
                    

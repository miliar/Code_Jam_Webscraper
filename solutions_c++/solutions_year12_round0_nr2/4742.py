#include<iostream>
#include<stdio.h>
using namespace std;
int g[100]={0},q[100]={0},r[100]={0};
int main()
{
    int t=0;
    cin>>t;
    int n=0,s=0,p=0,i=1,j=0,c=0;
    while(t--)
    {
                    c=0;
                    cin>>n>>s>>p;
                    for(j=0;j<n;j++)
                    {
                                    cin>>g[j];
                    q[j]=g[j]/3;
                    r[j]=g[j]%3;
                    }
                    for(j=0;j<n;j++)
                    {
                                    if(q[j]>=p)
                                    c++;
                                    else if(s>0 && r[j]==0 && p-q[j]==1 && q[j]>0)
                                    {
                                        c++;
                                        s--;
                                    }
                                    else if(p-q[j]==1 && r[j]>0)
                                    c++;
                                    else if(p-q[j]==2 && r[j]==2 && s>0)
                                    {
                                         c++;
                                         s--;
                                    }
                    }
            cout<<"Case #"<<i<<": "<<c<<endl;
            i++;
    }
    return 0;
}

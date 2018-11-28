#include<cstdio>
#include <iostream>
#include<math.h>
using namespace std;

int main ()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int t,a[100][100],s[100],p[100],n[100],i,j,count,min,k;
    cin>>t;
    for(i=0;i<t;i++)
    {
    cin>>n[i];
    cin>>s[i];
    cin>>p[i];
    for(j=0;j<n[i];j++)
    {
    cin>>a[i][j];
    }
    }
    for(i=0;i<t;i++)
    {
                    count=0;
                    
                    min=(p[i]*3)-2;
                    for(j=0;j<n[i];j++)
                    {
                    if((p[i]-2)<0)
                    k=0;
                    else
                    k=p[i]-2;
                    k=p[i]+k+k;
                    if(a[i][j]>=min)
                    count++;
                     else if(a[i][j]>=k && s[i]>0 )
                    {
                         
                         s[i]--;
                         count++;
                    }
                    else
                    {
                        continue;
                    }
                    }
                    cout<<"Case #"<<i+1<<": "<<count<<"\n";
                    }
               //  system("pause");
                    return 0;
                    }
                    

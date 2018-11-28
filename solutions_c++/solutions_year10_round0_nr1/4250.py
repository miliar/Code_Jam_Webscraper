#include<iostream>
using namespace std;
int main()
{
long long test,count;
bool n[31],p[31];
long long s,t;
cin>>test;
count=1;
while(test--)
{
cin>>s>>t;
p[1]=1;
n[1]=0;
for(int i=2;i<=30;i++)
{
n[i]=p[i]=0;
}
for(int i=1;i<=t;i++)
{
    for(int j=1;j<=s;j++)
    {
        if(p[j]==1)
        {
            if(n[j]==0)
            {
            n[j]=1;
            }
            else
            {
            n[j]=0;
                for(int k=j+1;k<=s;k++)
                {
                 if(p[k]==1)
                 {
                     if(n[k]==0)
                     {
                            n[k]=1;
                     }
                     else
                     {
                         n[k]=0;
                     }
                    p[k]=0;
                 }

                }
            }
        }
        else if(p[j]==0 && n[j-1]==1)
        p[j]=1;
        else
        {
            break;
        }
    }
}
if(p[s]==1&&n[s]==1)
cout<<"Case #"<<count<<": ON"<<endl;
else
cout<<"Case #"<<count<<": OFF"<<endl;
count++;
}
return 0;
}

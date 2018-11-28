
#include<iostream>
#include<cmath>
using namespace std;


int main()
{
freopen("A1.in", "rt", stdin);
  freopen("res(large).txt", "wt", stdout);
unsigned long long int t,n,k,res,count=0;

cin>>t;
while(t--)
{count++;
cin>>n>>k;
if(k%2==0)
res=0;
else if(k>=n)
{
     unsigned long long int temp=n;
    temp=1<<n;
    if((k+1)%(temp)==0)
    res=1;
    else
    res=0;
    }
    else
    {
        res=0;
        }
        if(res==0)
    cout<<"Case #"<<count<<": "<<"OFF"<<endl;
    else
    cout<<"Case #"<<count<<": "<<"ON"<<endl;
}
return 0;
    }

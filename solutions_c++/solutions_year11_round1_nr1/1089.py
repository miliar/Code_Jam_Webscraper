#include<iostream>
#include<math.h>
#include<stdio.h>
using namespace std;
int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
long long t,n,pd,pg,cn=1;
cin>>t;
while(t--)
{
    cin>>n>>pd>>pg;
    if(pd!=pg&&pg==100)cout<<"Case #"<<cn++<<": Broken"<<endl;
    else if(pd!=pg&&pg==0)cout<<"Case #"<<cn++<<": Broken"<<endl;
    else
    {
        if(n<100)
        {
            long long i;
            long long x;
            for(i=1;i<=n;i++)
            {

                x=(pd*i)/100;


                if(x*100==pd*i)break;
                if((x+1)*100==pd*i)break;
                if((x-1)*100==pd*i)break;

            }
            if(i==n+1)
            {
                cout<<"Case #"<<cn++<<": Broken"<<endl;
            }
            else
            {
               // cout<<i<<" "<<pd<<" "<<x<<endl;
                cout<<"Case #"<<cn++<<": Possible"<<endl;
            }
        }
        else
        {
            cout<<"Case #"<<cn++<<": Possible"<<endl;
        }
    }
}
return 0;
}

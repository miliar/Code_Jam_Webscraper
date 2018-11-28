#include <cstdlib>
#include <iostream>
#include<fstream>
#include<cmath>
using namespace std;

long gcd(long a,long b){
    if(a<b)swap(a,b);
	return b?gcd(b,a%b):a;
}

int main()
{
    long a[200],b[10],t2;
	ifstream cin("B-small-attempt11.in");
	ofstream cout("B-small-attempt11.out");
    long i,j,k,n,m,Min,ans,t,t1,w,Max;
    cin>>t;
    for(k=1;k<=t;k++)
    {
        cin>>n;
        cin>>a[0];
        //cout<<a[0]<<' ';
        Min=a[0];
        for(i=1;i<n;i++)
        {
            cin>>a[i];
            //cout<<a[i]<<" ";
            Min=min(a[i],Min);
        }
        //cout<<endl;
        if(n==2)
        {
            t1=labs(a[0]-a[1]);
            for(i=0;i<=t1;i++)
            {
                if((a[0]+i)%t1==0&&(a[1]+i)%t1==0)
                {
                    ans=i;
                    break;
                }
            }
        }
        else if(n==3)
        {
            Max=labs(a[0]-a[1]);
            Max=max(Max,labs(a[1]-a[2]));
            Max=max(Max,labs(a[0]-a[2]));
            for(i=Max;i>0;i--)
            {
                w=1;
                t1=a[0]%i;
                for(j=1;j<n;j++)
                {
                    if(a[j]%i!=t1)
                    {
                        w=0;
                    }
                }
                if(w==1)
                {
                    ans=i;
                    break;
                }
            }
            t1=ans;
            for(i=0;i<=t1;i++)
            {
                if((a[0]+i)%t1==0&&(a[1]+i)%t1==0&&(a[2]+i)%t1==0)
                {
                    ans=i;
                    break;
                }
            }
        }
        cout<<"Case #"<<k<<": "<<ans<<endl;
    }
    return 0;
}

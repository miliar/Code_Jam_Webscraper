#include <iostream>
#include<cstdio>

using namespace std;
const long long inf=10000000;
long long gcd(long long a,long long b){
	return b?gcd(b,a%b):a;
}
int main()
{
    freopen("in1.txt","r",stdin);
    freopen("out.txt","w",stdout);
    long long t,n,d,g,l,x,tt,temp,z,y;
    bool flag;
    cin>>t;
    for(l=1;l<=t;l++)
    {
        cin>>n>>d>>g;
        //scanf("%d%d%d",&n,&d,&g);
        x=gcd(d,100);
        tt=100/x;
        temp=d/x;
        if(n<tt)
        {
            flag=false;
            goto out;
        }
        x=gcd(g,100);
        y=g/x;
        z=100/x;
        if(y<=z&&(y*inf-temp)<=(z*inf-tt)&&y*inf-temp>=0)
        {
            flag=true;
        }
        else
        {
            flag=false;
        }
        out:if(flag)
        {
            printf("Case #");
            cout<<l;
            printf(": Possible\n");
        }
        else
        {
            printf("Case #");
            cout<<l;
            printf(": Broken\n");
        }
    }
    return 0;
}

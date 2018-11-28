#include<iostream>
#include<stdio.h>
#include<math.h>
#include<string.h>
#include<algorithm>
#include<string>
#include<vector>
#include<map>
#include<queue>
#include<stack>
#include<sstream>
using namespace std;
#define FOR(i,n) for(i=0;i<n;i++)
#define FOR1(i,n) for(i=1;i<=n;i++)
#define FORab(i,a,b) for(i=a;i<=b;i++)
double arr[1000010];
double FABS(double a)
{
    if(a<0)return -a;
    return a;
}
int main()
{
    int t,c,d,n,i,j,p,v,cn=1;
    freopen("input.txt","r",stdin);
    freopen("output1.txt","w",stdout);
	cin>>t;
	while(t--)
	{
        cin>>c>>d;
        n=0;
        FOR(i,c)
        {
            cin>>p>>v;
            FOR(j,v)arr[n++]=p;
        }

        double lo=0,hi=1e9,mid;
        while(FABS(hi-lo)>1e-9)
        {
            mid=(lo+hi)/2.0;
            //cout<<mid<<endl;
            double last=-1e9;

            FOR(i,n)
            {
                //if(last>arr[i])break;
                if(arr[i]-mid>=last+d)last=arr[i]-mid;
                else
                {
                    if(arr[i]+mid>=last+d)last=last+d;
                    else break;
                }
            }
            if(i==n)hi=mid;
            else lo=mid;
        }
            double last=-1e9;
            FOR(i,n)
            {
                //cout<<"dasdasd "<<arr[i]<<" "<<mid<<" "<<last<<" "<<d<<endl;
                if(last>arr[i])break;
                if(arr[i]-mid>last+d)last=arr[i]-mid;
                else
                {
                    if(arr[i]+mid>=last+d)last=last+d;
                    else break;
                }
                //cout<<"last "<<last<<" "<<n<<endl;
            }
            cout<<"Case #"<<cn++<<": ";
        printf("%.15lf\n",lo);

	}
	return 0;
}

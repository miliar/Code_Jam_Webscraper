#include<iostream>
#include<cstdio>
#include<cstring>
#include<fstream>
#include<cstdlib>
#include<cmath>
using namespace std;
#define fr(i,n) for(long i=0;i<n;i++)

long power(int n)
{
     long ret=1;
     for(int i=0;i<n;i++) ret*=10;
     return ret;
}
long shft(long i,long d,long digits)
{
     long x,y,p;
     p=power(d-digits);
     x=i%p;
     y=i/p;
     x*=power(digits);
     x+=y;
     return x;
     
}
bool flag[2000001];
int main()
{
    //freopen("clI.in","r",stdin);
    //freopen ("clO.txt","w",stdout);
    long i,j,a,d,b,t,cas=1,curr,n,res;
    cin>>t;
    
    while(t--)
    {
              res=0;
              cin>>a>>b;
              d=0;
              while(1)
              {
                      d++;
                      if(a%power(d)==a) break;
              }
              
              for(i=a;i<=b;i++)
              {
                 curr=i;
                for(j=1;j<d;j++)
                {
                                n=shft(curr,d,j);
                                if(n==curr) break;
                                if(n>i && n<=b) {
                                        flag[n]=true;
                                        res++;
                        //                cout<<curr<<" "<<n<<endl;
                                        }
                }
              }
              //long res=0;
              //for(i=a;i<=b;i++) if(flag[i]) res++;
              printf("Case #%ld: %ld\n",cas++,res);
              fr(i,b+1) flag[i]=false;
    }
    return 0;
}

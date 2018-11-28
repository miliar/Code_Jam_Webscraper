#include<iostream>
using namespace std;
long long d[1100000];
long long c[1100];
long long i,j,k,l,m,n,t,xys,ysc,sb,cc,sum;
bool cmp(int i,int j){return i>j;}
int main()
{
    freopen("b.in","r",stdin);
    freopen("output.txt","w",stdout);
    cin>>ysc;
    for (xys=1;xys<=ysc;++xys){
        if (xys==100){
           i=1;
        }
           
        cin>>l>>t>>n>>cc;
        for (i=0;i<cc;++i) cin>>c[i];
        sum=0;sb=0;j=0;
        for (i=0;i<n;++i){
            d[i]=c[j]*2;sum+=d[i];
            ++j;if (j==cc) j=0;
        }
        i=-1;
        while (i<n&&t>=0){
              ++i;
              t-=d[i];
        }
        if (t<0){
           m=i;d[m]=-t;
           sort(d+m,d+n-1,cmp);
           for (i=m;i<n;++i){
               if (l==0) break;
               sb+=d[i];
               --l;
           }
        }
        cout<<"Case #"<<xys<<": "<<sum-sb/2<<endl;
    }
    return 0;
}
        

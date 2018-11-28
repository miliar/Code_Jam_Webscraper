#include <iostream>
#include <string>
#include <string.h>
#include <algorithm>

using namespace std;
typedef long long int64;
int T[256];
int main()
{
    freopen("A-large.in","r",stdin);  freopen("p1.out","w",stdout);
    int kase,i,j,k,n;
    char d[100];
    int64 d2[100];
    cin>>kase;
    for(i=1;i<=kase;i++) {
       cout<<"Case #"<<i<<": ";
       cin>>d;
       n=strlen(d);
       memset(T,0,sizeof(T));
       int b=0;
       for(j=0;j<n;j++) 
          if(T[d[j]]==0) T[d[j]]=1,b++;
       memset(T,255,sizeof(T));
       if(b==1) b=2;
       T[d[0]]=1;  d2[1]=1;  int c=1,tot=0;
       for(j=1;j<n;j++) {
         if(T[d[j]]==-1) {
            T[d[j]]=tot;
            if(tot==0) tot=2;
            else tot++;
         }
         d2[++c]=T[d[j]];
       }
       int64 s=1,ans=0;
       for(j=c;j>=1;j--) {
         ans=ans+d2[j]*s;
         s=s*b;
       }
       cout<<ans<<endl;
    }
    return 0;
}

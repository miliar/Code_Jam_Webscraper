#include<iostream>

using namespace std;


long long tt;
int T,l,n,c,d,td;
int a[2000];
long long t[2000];

int main()
{
    freopen("b.in","r",stdin);
    freopen("b.out","w",stdout);
    
    cin>>T;
    for (int ii=1;ii<=T;ii++) {
        cout<<"Case #"<<ii<<": ";
        cin>>l>>tt>>n>>c;
        for (int i=0;i<c;i++)
            scanf("%d",&a[i]);
        t[0]=0;
        for (int j=1;j<=n;j++)
            t[j]=t[j-1]+a[(j-1)%c]*2;
        d=0;
        if (l>0) {
           for (int j=0;j<n;j++)
               if (t[j]<tt) {
                  if (t[j+1]>=tt && t[j+1]>tt+d*2)
                     d=(t[j+1]-tt)/2;
               } else {
                  if (t[j]+d+d<t[j+1])
                     d=(t[j+1]-t[j])/2;
               }
        }
        if (l>1) {
           for (int j=0;j<n-1;j++) 
               for (int k=j+1;k<n;k++) {
                   int td=0;
                   if (t[j]<tt) {
                      if (t[j+1]>tt) td=(t[j+1]-tt)/2;
                   } else td=(t[j+1]-t[j])/2;
                   if (t[k]<tt) {
                      if (t[k+1]>tt) 
                         td+=((t[k+1]-tt)/2);
                   } else td+=((t[k+1]-t[k])/2);
                   if (d<td) d=td;
               }
        }
        cout<<t[n]-d<<endl;
    }
    
    return 0;
}

#include<iostream>

using namespace std;

int T,N,L,H;
int a[20000];

int main()
{
    freopen("c.in","r",stdin);
    freopen("c.out","w",stdout);
    
    cin>>T;
    for (int ii=1;ii<=T;ii++) {
        cout<<"Case #"<<ii<<": ";
        cin>>N>>L>>H;
        for (int i=1;i<=N;i++)
            scanf("%d",&a[i]);
        bool ff=false;
        for (int i=L;i<=H;i++) {
            bool flag=true;
            for (int j=1;j<=N;j++)
                if (a[j]%i==0 || i%a[j]==0) continue;
                   else flag=false;
            if (flag) {ff=true;cout<<i<<endl;break;}
        }
        if (!ff) cout<<"NO\n";
    }
                                
    return 0;
}

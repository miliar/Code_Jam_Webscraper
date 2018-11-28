#include<iostream>

using namespace std;

int T,N;

int main(){
    freopen("d.in","r",stdin);
    freopen("d.out","w",stdout);
    
    cin>>T;
    for (int ii=1;ii<=T;ii++) {
        cin>>N;
        int ans=0;
        for (int i=1;i<=N;i++) {
            int x;
            scanf("%d",&x);
            if (x!=i) ans++;
        }
        cout<<"Case #"<<ii<<": "<<ans<<".000000\n";
    }
    //system("pause");
    return 0;
}

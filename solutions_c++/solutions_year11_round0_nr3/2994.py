#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>

using namespace std;

int T,N,a[2000];

int main(){
    freopen("C.in","r",stdin);
    freopen("C.out","w",stdout);
    
    cin>>T;
    for (int i=1;i<=T;i++) {
        cin>>N;
        for (int j=1;j<=N;j++)
             cin>>a[j];
        sort(a+1,a+N+1);
        int t=a[1];
        int sum=0;
        for (int j=2;j<=N;j++)
             t^=a[j];
        if (t!=0) cout<<"Case #"<<i<<": NO\n";
           else {
                for (int j=N;j>=2;j--)
                    t+=a[j];
                cout<<"Case #"<<i<<": "<<t<<"\n";
           } 
    }
    //system("pause");
    return 0;
}

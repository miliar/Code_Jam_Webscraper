#include <iostream>
#include <cstdio>
using namespace std;

int main(){
    freopen("1.in","r",stdin);
    freopen("1.out","w",stdout);
    int t;
    cin>>t;
    for (int t1 = 1; t1 <= t; ++t1){
        int n,x,y=100000000,s1=0,s=0;
        cin>>n;
        for (int i = 0; i < n; ++i){
            cin>>x;
            s += x;
            s1 ^= x;
            if (x < y) y = x;
        }
        printf("Case #%d: ",t1);
        if (s1==0) cout<<s-y;
            else cout<<"NO";
        cout<<endl;
        //cout<<s<<" "<<y<<" "<<s1<<endl<<endl;
    }
}

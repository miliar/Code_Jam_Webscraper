#include <iostream>
using namespace std;

int main(){
    //freopen("in.txt","r",stdin);
    //freopen("out.txt","w",stdout);
    int t,i,n,k,v;
    cin >> t;
    for(i=1;i<=t;i++){
        cin >> n >> k;
        cout << "Case #" << i << ": ";
        v=(1<<n)-1;
        if((k&v)==v) cout << "ON" << endl;
        else cout << "OFF" << endl;
    }
}

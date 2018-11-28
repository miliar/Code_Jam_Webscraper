#include<iostream>
using namespace std;
int u; int n, k;

void init(){
    cin >> n >> k;
}

int main(){
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int i, T;
    cin >> T;
    for (i=1;i<=T;i++){
        init();
        cout << "Case #" << i << ": ";
        u = (1 << n) - 1;
        if ((k&u)==u) cout << "ON";
        else cout << "OFF";
        cout << endl;

    }
}

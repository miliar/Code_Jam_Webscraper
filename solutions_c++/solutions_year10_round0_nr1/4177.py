#include <iostream>
using namespace std;

typedef long long ent;

int main() {
    int t;
    cin >> t;
    for (int cas = 1; cas <= t; ++cas) {
        ent N, K;
        cin >> N >> K;
        cout << "Case #" << cas << ": ";
        if((K & ((1LL<<N) - 1)) == (1LL<<N) - 1) cout<<"ON"<<endl;
        else cout<<"OFF"<<endl;
    }
}

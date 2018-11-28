#include <iostream>
using namespace std;

int gcd(int a, int b) {
    if(b == 0) return a;
    return gcd(b,a%b);
}

int main() {
    int T;
    cin>>T;
    for(int i = 1; i <= T; ++i) {
        long long N, pd, pg;
        cin>>N>>pd>>pg;
        // eka luku mahdollinen
        if(pd != 0 && 100/gcd(pd,100) > N) goto fail;
        if(pd > 0 && pg == 0) goto fail;
        if(pd < 100 && pg == 100) goto fail;

        cout<<"Case #"<<i<<": Possible"<<endl;
        continue;
fail:
        cout<<"Case #"<<i<<": Broken"<<endl;
        continue;
    }
    return 0;
}

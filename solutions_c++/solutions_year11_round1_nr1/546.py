#include <iostream>
using namespace std;

int gcd(int x, int y) {
    if(x==0) return y;
    return gcd(y%x, x);
}

int main() {
    int CASEN;
    cin>>CASEN;
    for(int ci=1;ci<=CASEN;ci++) {
        long long n,pd,pg;
        cin>>n>>pd>>pg;
        bool res = false;
        if(pd==0 && pg<100) res = true;
        else if(pd==100 && pg==100) res=true;
        else if(pg==100 && pd<100) res = false;
        else if(pg==0 && pd>0) res = false;
        else if(n>=100ll) res = true;
        else {
            int d = gcd(pd,100);
            int x = pd/d, y = 100/d;
            if(n>=y) res = true;
            else res = false;
        }
        cout<<"Case #"<<ci<<": ";
        if(res) cout<<"Possible"<<endl;
        else cout<<"Broken"<<endl;
    }

    return 0;
}


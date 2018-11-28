#include <iostream>
#include <cmath>
#include <cstring>
#include <algorithm>

using namespace std;
typedef long long LL;
LL N,pd,pg;
LL gcd(LL a, LL b)
{
    if(b==0) return a;
    return gcd(b,a%b);
}
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-small.out","w",stdout);
    int T;
    cin>>T;
    for(int tc=1;tc<=T;tc++) {
        cin>>N>>pd>>pg;
        cout<<"Case #"<<tc<<": ";
        LL g = gcd(100,pd);
        if((100/g)>N ) {
            cout<<"Broken"<<endl;
            continue;
        }
        if(pg==100&&pd<100) {
            cout<<"Broken"<<endl;
            continue;
        }
        if(pg==0&&pd>0) {
            cout<<"Broken"<<endl;
            continue;
        }

        cout<<"Possible"<<endl;

    }
    return 0;
}

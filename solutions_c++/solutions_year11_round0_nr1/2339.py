#include <iostream>
using namespace std;

int func() {
    int n;
    cin>>n;
    int os=0, bs = 0;
    int op = 1, bp = 1;
    char c;
    int pos;
    int now = 0;
    for (int i=0;i<n;i++) {
        cin>>c>>pos;
        if (c == 'O') {
            int diff = pos - op;
            op = pos;
            if (diff < 0) diff = -diff;
            if (os + diff < now) { 
                os = now + 1;
                now++;
            } else {
                os += diff + 1;
                now = os;
            }
        } else {
            int diff = pos - bp;
            bp = pos;
            if (diff < 0) diff = -diff;
            if (bs + diff < now) { 
                bs = now + 1;
                now++;
            } else {
                bs += diff + 1;
                now = bs;
            }
        }
    }
    return now;
}
int main() {
    int t = 0;
    cin>>t;
    for (int i=0;i<t;i++) cout<<"Case #"<<(i+1)<<": "<<func()<<endl;
    return 0;
}


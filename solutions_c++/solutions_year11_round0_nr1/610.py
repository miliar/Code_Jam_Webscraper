#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    int CASEN;
    cin>>CASEN;
    for(int ci=1;ci<=CASEN;ci++) {
        int N;
        int ot,op;
        int bt,bp;
        int c=0;

        ot = bt = 0;
        op = bp = 1;
        cin>>N;
        for(int i=0;i<N;i++ ) {
            char color;
            int button;
            cin >> color >> button ;
            if(color == 'O') {
                int dis = abs(button-op);
                int tdif = c - ot;
                if( tdif >= dis ) {
                    c++;
                    ot = c;
                    op = button;
                } else {
                    c = ot+dis+1;
                    ot = c;
                    op = button;
                }
            } else {
                int dis = abs(button-bp);
                int tdif = c - bt;
                if (tdif>=dis) {
                    c++;
                    bt = c;
                    bp = button;
                } else {
                    c=bt+dis+1;
                    bt = c;
                    bp = button;
                }
            }

        }

        cout<<"Case #"<<ci<<": "<<c<<endl;;
    }

    return 0;
}


#include <iostream>
#include <vector>

using namespace std;



int main() {
    int cases;
    cin >> cases;

    for(int c=0; c<cases; c++) {
        int n;
        cin >> n;
        int opos = 1, otm = 0, bpos = 1, btm = 0;
        for(int i=0; i<n; i++) {
            char who;
            int newpos;
            cin >> who >> newpos;
            if (who == 'O') {
                otm = ((otm + abs(newpos-opos)) >? btm) + 1;
                opos = newpos;
            }
            else {
                btm = ((btm + abs(newpos-bpos)) >? otm) + 1;
                bpos = newpos;
            }
        }
        cout << "Case #" <<(c+1) << ": " << (otm>?btm) << endl;
    }
}

#include <iostream>
#include <algorithm>
#include <cstdlib>

using namespace std;

int main() {
    int c, d, v;
    int fst, scd;
    int fpos, spos;
    char r;
    cin >> c;
    for(int j=0; j<c; j++) {
        cin >> d;
        fst = scd = 0;
        fpos = spos = 1;
        for(int i=0; i<d; i++) {
            cin >> r >> v;
            if( r == 'B' ) swap(fst, scd);
            if( r == 'B' ) swap(fpos, spos);

            fst += ( abs(v - fpos) + 1);
            if( fst <= scd ) fst = scd+1;
            fpos = v;

            if( r == 'B' ) swap(fpos, spos);
            if( r == 'B' ) swap(fst, scd);
        }
        cout << "Case #" << j+1 << ": " << (fst < scd ? scd : fst) << endl;

    }
}

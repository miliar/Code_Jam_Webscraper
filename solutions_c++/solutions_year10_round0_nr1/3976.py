#include <iostream>
using namespace std;

int masks[] = { 0, 1,3,7,15,31,63,127,255,511,1023,2047,4095,8191,16383,32767,65535,131071,262143,524287,1048575,2097151,4194303,8388607,16777215,33554431,67108863,134217727,268435455,536870911,1073741823 };

int main() {
    int t, n, k;

    cin >> t;
    for(int tt=1; tt<=t; tt++) {
        cin >> n >> k;
        k = k & masks[n];
        //cout << k<< " " << ((k+1)& masks[n]) << endl;;
        cout << "Case #" << tt  << ": ";
        if (((k+1)& masks[n]) == 0) cout << "ON";
        else cout << "OFF";
        cout << endl;
    }
}

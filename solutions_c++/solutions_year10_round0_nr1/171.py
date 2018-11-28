#include <iostream>
#include <vector>

using namespace std;



int main() {
    int cases;
    cin >> cases;

    for(int c=0; c<cases; c++) {
        long N, K;
        cin >> N >> K;

        long mask = ((1L<<N)-1);

        string ans = (mask & K) == mask ? "ON" : "OFF";
        cout << "Case #" <<(c+1) << ": " << ans << endl;
    }
}

#include <iostream>
using namespace std;

char on[3]="ON";
char off[4]="OFF";
int main() {
    int T, N, K;
    char* status;
    // cout << (1 << 0);
    cin>>T;
    int i = 0;
    while(i++ < T) {
        cin >> N;
        cin >> K;
        status = ((( 1 << N ) - 1 ) & K) == (( 1 << N ) - 1 ) ? on : off;
        cout << "Case #" << i << ": " << status << endl;

    }
    return 0;
}

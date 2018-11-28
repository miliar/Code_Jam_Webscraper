#include <iostream>
#include <cstdio>
#include <string>
#include <cstring>
#include <iomanip>
#define MAX 19
using namespace std;

int T[MAX];

int main() {
    string ref = "welcome to code jam";

    int t, tt=0;
    cin >> t;
    string s;
    getline(cin, s);

    while(tt++<t) {
        getline(cin, s);
        memset(T, 0, sizeof(T));
        for(int i=s.size()-1; i>=0; i--) {
            for(int j=MAX-1; j>=0; j--) {
                if (j<MAX-1 && T[j+1] == 0) break;

                if (ref[j] == s[i]) T[j] += ((j==MAX-1)?1:T[j+1]);
                T[j] = T[j] % 10000;
            }
        }

        cout << "Case #" << tt << ": ";
        cout.fill('0');
        cout << setw(4) << T[0] << endl;
    }
}

#include <iostream>
#include <string>
#include <sstream>

using namespace std;

int main() {
    int T;
    cin >> T;
    string dummy;std::getline(cin, dummy);
    for(int i = 0; i < T; i++ ) {
        int A, B;
        cin >> A >> B;
        cerr << A << ", " << B << endl;
        int counter = 0;
        for(int n = A ; n < B ; n++) {
            for(int m = n+1 ; m <= B; m++) {
                stringstream nss, mss;
                nss << n;
                mss << m;
                string ns = nss.str();
                string ms = mss.str();
                for(int j = 1; j < int(ns.length()) ; j++) {
                    if (ns.substr(ns.length() - j) ==  ms.substr(0, j) &&
                        ns.substr(0, ns.length() - j) == ms.substr(j)) {
                        counter++;
                        break;
                    }
                }
            }
        }
        std::cout << "Case #" << (i+1) << ": " << counter << std::endl;
    }
}

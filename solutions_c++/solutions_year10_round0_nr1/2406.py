#include <iostream>
#include <cmath>

using namespace std;

int main() {
        int cases;
        int digits;
        int snaps;

        cin >> cases;
        for (int i=0; i<cases; i++) {
                cin >> digits;
                cin >> snaps;

                cout << "Case #" << i+1 << ": ";
                if (digits==0) {
                        cout << "OFF" << endl; 
                        continue;
                }

                int exponentiated = pow(2,digits);
                while (snaps-exponentiated>0)
                        snaps-=exponentiated;

                if (snaps == (pow(2, digits)-1))
                        cout << "ON";
                else
                        cout << "OFF";

                cout << endl;
        }
}

#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main() {
    int T,N,S,p;
    
    cin >>T;
    for (int t=0; t < T; t++) {
        cin >>N >>S >>p;
        int max,val;
        max = 0;
        val = 0;
        
        for (int n=0;n < N;n++) {
            cin >>val;
            if (val/3 >= p) {
                max ++;
            } else if (p - (val/3) == 2 && S > 0 && 2 == val%3) {
                S--;
                max++;
            } else if (p - (val/3) == 1 && val%3 != 0) {
                max++;
            } else if (p - (val/3) == 1 && val != 0 && S > 0) {
                 max++;
                 S--;
            }
        }
        cout <<"Case #" <<t+1 <<": " <<max <<endl;
    }
}

#include <iostream>
#include <cmath>
using namespace std;

int main() {
    
    // read cases
    int c;
    cin >> c;
	
    // read each case
	
    for (int k = 0; k< c; k++) {
        // read
        int n;
        cin >> n; 
        long long event[n];
        // read events
        for (int i = 0;i<n;i++) {
            
            cin >> event[i];
        }
        //calculate diff between two
        long long gc = event[0]-event[1];
        gc = abs(gc);
        for (int i = 0; i<n-1; i++) {
            for (int j = i+1; j<n; j++) {
                long long diff = event[i] - event[j];
                gc = __gcd(gc,abs(diff));
            }
        }
        long long result;
        if (gc == 1) result =0;
        if (event[0] % gc == 0) result = 0;
        else result =gc -  event[0] % gc;
        cout << "Case #" << 1+k<<": " << result <<endl;
    }
}
// to compile : g++ namefile
// to run : ./a.out < text.in >text.out



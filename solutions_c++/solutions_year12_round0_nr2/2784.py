
#include <cstdlib>
#include <iostream>
#include <cmath>

using namespace std;

int main(int argc, char** argv) {
    int count, n, s, p, sum, result;
    double temp;
    int i, j;
    
    
    cin >> count;
   // lines
    for (i=0; i<count; i++) {
        result = 0;
        
        cin >> n >> s >> p;
        
       // values
        for (j=0; j<n; j++) {
            cin >> sum;
            
            temp = sum/3.0;
            if (sum%3 != 0) {temp += 1;}
            
            if (temp >= p) {
                result++;
            } else if (s > 0 && round(temp+1) >= p && (temp - (int)temp == 0 || temp-(int)temp > 0.5) && sum > 1 && sum < 29) {
                result++; s--;
            }
        }
        
        cout << "Case #" << i+1 << ": " << result << endl;;
    }
    
    return 0;
}


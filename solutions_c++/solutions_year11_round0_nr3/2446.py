#include <iostream>
#include <algorithm>
#include <limits>
#include <vector>
#include <boost/foreach.hpp>
#include <iterator>

using namespace std;

int main(int argc, const char* argv[])
{
    size_t T, N;
    cin >> T;
    for (size_t test = 1; test <= T; ++test) {
        cin >> N;
        vector<unsigned long> ar(N);
        unsigned long allXor = 0;
        unsigned long allSum = 0;
        unsigned long min = numeric_limits<unsigned long>::max();

        for (size_t i = 0; i < N; ++i) {
            cin >> ar[i];
            allXor ^= ar[i];
            allSum += ar[i];
            if (ar[i] < min)
                min = ar[i];
        }
        
        cout << "Case #" << test << ": ";
        if (allXor == 0)
            cout << allSum - min << endl;
        else
            cout << "NO" << endl;
    }
    
    return 0;
}

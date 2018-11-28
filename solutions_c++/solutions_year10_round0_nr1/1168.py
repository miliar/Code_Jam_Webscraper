#include <cstdio>
#include <iostream>
#include <cassert>
#include <cstdlib>
#include <cstring>
#include <cmath>

using namespace std;

int main()
{
    int T;
    
    cin >> T;

    for(int i=1; i<=T; i++) {
        unsigned int N, K;
        cin >> N;
        cin >> K;
        N = (((unsigned int)1)<<N) - 1;
        K = K & N;
        
        if( K == N )
            cout << "Case #" << i << ": " << "ON" << endl;
        else
            cout << "Case #" << i << ": " << "OFF" << endl;
    }
    
    cin >> T;
    return 0;
}

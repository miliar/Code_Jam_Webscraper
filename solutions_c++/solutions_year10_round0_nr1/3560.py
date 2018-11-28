#include <iostream>
#include <vector>

using namespace std;

int main(int argc, char** argv)
{
    int T;
    cin >> T;
    
    for (int i = 1; i <= T; ++i)
    {
        long long N, K;
        cin >> N >> K;
        
        long long answer = K;
        if (N > K)
            answer = 1;
        else
            answer = (K + 1) % (1 << N);
            
        cout << "Case #" << i << ": " << (answer ? "OFF" : "ON") << endl;
    }
    return 0;
}

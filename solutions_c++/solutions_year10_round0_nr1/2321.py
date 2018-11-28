#include <iostream>
using namespace std;

int main()
{
    int T;
    cin >> T;
    for(int t = 0; t < T; t++)
    {
        int N, K;
        cin >> N >> K;
        if(K % (1 << N) == (1 << N) - 1)
            cout << "Case #" << t + 1 << ": " << "ON" << endl;
        else
            cout << "Case #" << t + 1 << ": " << "OFF" << endl;
    }
    return 0;
}


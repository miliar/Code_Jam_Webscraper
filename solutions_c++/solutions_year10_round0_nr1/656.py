#include <iostream>
#include <algorithm>
using namespace std;

int main(int argc, char *argv[])
{
    int T, N, K;
    cin >> T;
    for(int i = 1; i <= T; i++)
    {
        cin >> N >> K;
        int t = 1;
        for(int j = 0; j < N; j++){
            t <<= 1;
        }
        K++;
        cout << "Case #" << i << ": ";
        if(K%t == 0) cout << "ON" << endl;
        else cout << "OFF" << endl;
    }
    return 0;
}

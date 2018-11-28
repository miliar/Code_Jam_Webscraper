#include <iostream>

using namespace std;

int main(int argc, char **argv)
{
	int T, N, K, i;

    cin >> T;
    for (i = 1; i <= T; i++)
    {
        cin >> N >> K;
        N = ~(0xffffffff << N);
        cout << "Case #" << i << ": " << ((K & N) == N ? "ON" : "OFF") << endl;
    }
    return 0;
}


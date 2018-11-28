#include<iostream>

using namespace std;

int main()
{
    int T; cin >> T;
    for(int t = 1; t <= T; ++t) {
        int N; cin >> N;
        int _xor = 0, sum = 0, smallest = (1<<20);
        for(int i = 0; i < N; ++i) {
            int x; cin >> x;
            _xor ^= x;
            sum += x;
            smallest = min(x, smallest);
        }

        if(_xor == 0)
            cout << "Case #" << t << ": " << sum - smallest << endl;
        else
            cout << "Case #" << t << ": NO" << endl;
    }

    return 0;
}

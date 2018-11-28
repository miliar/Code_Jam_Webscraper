#include <iostream>
#include <fstream>

using namespace std;

int main(void)
{
    ifstream f("C-small.in");
    ofstream of("C-small.out");
    int T;
    f >> T;
    cout << T << endl;
    for (int i = 0; i < T; ++i)
    {
        int R, k, N;
        int arr[N+1];
        f >> R >> k >> N;
        cout << R << k << N << endl;
        for (int j = 0; j < N; ++j)
            f >> arr[j];
        int p = 0;
        int sum = 0;
        for(int j = 0; j < R; ++j)
        {
            int t = 0;
            int c = 0;
            while (t+arr[p] <= k && c+1 <= N)
            {
                t += arr[p];
                ++p;
                if (p >= N)
                    p = 0;
                ++c;
            }
            sum += t;
        }
        of << "Case #" << i+1 << ": " << sum << endl;
    }
    
    return 0;
}


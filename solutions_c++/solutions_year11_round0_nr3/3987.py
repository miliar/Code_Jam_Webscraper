#include <iostream>
using namespace std;

int N;
int C[16];

int solve()
{
    int sum = 0;
    int xsum1 = 0;
    int xsum2 = 0;
    int max  = 0;
    int csum = 0;
    for (int i = 0; i < N; i++)
        sum += C[i];

    for (int i = 1; i < (1<<N); i++) {
        xsum1 = 0;
        xsum2 = 0;
        csum = 0;
        for (int j = 0; j < N; j++) {
            if (i&(1<<j)) {
                xsum1 ^= C[j];
                csum += C[j];
            } else {
                xsum2 ^= C[j];
            }
        }
        csum = sum - csum;
        
        if ( (xsum1 == xsum2) &&
             (csum > max) )
            max = csum;
    }
    return max;
}

int main(int argc, char **argv)
{
    int T;
    int res = 0;
    cin >> T;
    for (int i = 0; i < T; i++) {
        cin >> N;
        memset(C, 0, sizeof(C));
        for (int j = 0; j < N; j++) {
            cin >> C[j];
        }
        res =solve();
        cout << "Case #" << i+1 << ": ";
        if (res > 0) cout << res;
        else cout << "NO";
        cout << endl;
    }
    return 0;
}

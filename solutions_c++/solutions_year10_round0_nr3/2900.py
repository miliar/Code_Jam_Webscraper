#include <iostream>
#include <cstring>
using namespace std;

//unsigned int N[1000][1000] = { {0,}, };
unsigned int g[1000];
int main() {
    // cout << sizeof(N);
    unsigned int T, R, k, N;
    cin >> T;
    unsigned int i = 1, j, sum, earn, start;
    while(i <= T) {
        // memset(N, 0, sizeof(N));
        // cout << i << endl;
        memset(g, 0, sizeof(g));
        cin >> R >> k >> N;
        j= 0;
        while(j < N) {
            cin >> g[j];
            j++;
        }
        earn= j= 0;
        while(R > 0) {
            start= j;
            sum = g[j];
            j++;
            if(j == N)
                j= 0;
            while(sum + g[j] <= k && start != j) {
                sum+= g[j];
                j++;
                if(j == N) {
                    j= 0;
                }
            }
            earn+= sum;
            R--;
        }
        cout << "Case #" << i << ": " << earn << endl;
        i++;
    }
    return 0;
}

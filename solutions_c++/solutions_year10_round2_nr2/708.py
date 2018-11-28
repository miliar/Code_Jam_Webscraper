#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <bitset>


using namespace std;

int main()
{
    const int MAXN = 50;
    int T;

    cin >> T;

    bitset<MAXN> can;

    for (int Case = 1; Case <= T; ++Case) {
		printf("Case #%d: ", Case);

        can.reset();

        int N, K, B, T;
        cin >> N >> K >> B >> T;

        vector<int> X(N), V(N);
        for (int i = 0; i < N; ++i) {
            cin >> X[i];
        }
        for (int i = 0; i < N; ++i) {
            cin >> V[i];
        }

        for (int i = 0; i < N; ++i) {
            can[i] = (X[i] + V[i] * T) >= B;
        }

        if (can.count() < K) {
            printf("IMPOSSIBLE\n");
            continue;
        }


        int result = 0;
        int chicks = 0;
        for (int i = N-1; i >= 0; --i) {
            if (can[i]) {
                result += chicks;
            }
            else {
                chicks += 1;
            }
        }

        printf("%d\n", result);
    }

    return 0;
}


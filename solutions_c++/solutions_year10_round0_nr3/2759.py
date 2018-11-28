#include <iostream>
#include <vector>

using namespace std;

void step(
    long long& money,
    int& position, 
    const std::vector<int>& g,
    long long k
)
{
    std::vector<int> visited(g.size(), 0);

    while (g[position] <= k && !visited[position]) {
        money += g[position];
        k -= g[position];
        visited[position] = 1;
        position = (position + 1) % g.size();
    }
}

int main()
{
    int T;

    cin >> T;

    for (int Case = 1; Case <= T; ++Case) {
        long long result = 0;
        long long R, k, N;
        int position = 0;

        cin >> R >> k >> N;

        std::vector<int> g(N);

        for (int i = 0; i < g.size(); ++i) {
            cin >> g[i];
        }

        for (int i = 0; i < R; ++i) {
            step(result, position, g, k);
        }

        printf("Case #%d: %lld\n", Case, result);
    }

    return 0;
}


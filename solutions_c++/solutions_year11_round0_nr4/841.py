#include <iostream>
#include <algorithm>
#include <cstring>
#include <cstdlib>
using namespace std;

int v[1001];
bool visited[1001];

int solve(int CASE)
{
    int n;
    cin >> n;
    for (int i = 1; i <= n; i++)
        cin >> v[i];

    memset(visited, 0, sizeof(visited));
    
    int hits = 0;
    for (int i = 1; i <= n; i++)
        if (!visited[i]) {
            int cycle = 0;
            for (int k = i; !visited[k]; k = v[k])
            {
                visited[k] = true;
                cycle++;
            }

            //printf("Cycle of %d\n", cycle);
            if (cycle > 1)
                hits += cycle;
        }

    printf("Case #%d: %.6lf\n", CASE, (double)hits);
}

int main()
{
    int T;
    cin >> T;
    for (int i = 1; i <= T; i++)
        solve(i);

    return 0;
}

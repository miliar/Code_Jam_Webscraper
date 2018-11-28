#include <cmath>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <cstring>

using namespace std;

typedef vector<string> vs;
typedef vector<int> vi;
typedef pair<int, int> pii;

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);

    int N;
    scanf("%d", &N);

    for (int i = 0; i < N; i++)
    {
        int P, K, L;
        scanf("%d%d%d", &P, &K, &L);
        vi data;
        for (int j = 0; j < L; j++)
        {
            int tmp;
            scanf("%d", &tmp);
            data.push_back(tmp);
        }
        sort(data.begin(), data.end());
        long long sum = 0;
        for (int j = 0; j < L; j++)
        {
            int k = j / K + 1;
            sum += (long long)data[L - j - 1] * k;
        }
        printf("Case #%d: %lld\n", i + 1, sum);
    }
 
    return 0;
}

#include <cstdio>
#include <cstring>
#include <algorithm>

#include <vector>

#include <iostream>

typedef long long int64;

using namespace std;

const int maxN = 1024000;

int64 L, T, N, C;

int64 dist[maxN], data[maxN], sum[maxN];

bool cmp(const int64 & a, const int64 & b)
{
    return a > b;
}

int main()
{
    //freopen("B2.in", "r", stdin);
    //freopen("B2.out", "w", stdout);

    int cas;

    scanf("%d", &cas);
    for(int cc = 0; cc < cas; cc++)
    {
        cin >> L >> T >> N >> C;
        for(int i = 0; i < C; i++)
        {
            cin >> data[i];
            data[i] <<= 1;
        }

        int idx = 0;
        int sta = 0;
        memset(sum, 0, sizeof(sum));
        for(int i = 1; i <= N; i++, idx = (idx + 1) % C)
        {
            dist[i] = data[idx];
            sum[i] = sum[i - 1] + dist[i];
            if(sum[i] >= T && sta == 0) sta = i;
        }

        vector<int64> save;

        if(sum[sta] != T) save.push_back(sum[sta] - T);
        for(int i = sta + 1; i <= N; i++)
            save.push_back(dist[i]);

        sort(save.begin(), save.end(), cmp);

        int siz = save.size();

        int64 ans = sum[N];
        for(int i = 0; i < L && i < siz; i++)
            ans -= (save[i] >> 1);

        cout << "Case #" << cc + 1 << ": " << ans << endl;
    }
    return 0;
}

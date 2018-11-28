// Compile by: g++ -O2 thisfile.cc
// Tested with g++ (GCC) 4.3.4 20090804 (release) 1 on Cygwin

#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    int T;
    scanf("%d", &T);
    for (int idxCase = 0; idxCase < T; ++idxCase)
    {
        int R, k, N;
        scanf("%d%d%d", &R, &k, &N);
        vector<int> g(N);
        for (int i = 0; i < N; ++i)
            scanf("%d", &g[i]);
        vector<long long> s(N + 1);
        long long sum = 0;
        for (int i = 0; i < N; ++i)
        {
            s[i] = sum;
            sum += g[i];
        }
        s[N] = sum;
        int pos = 0;
        vector<int> idx(N, -1);
        vector<long long> people;
        people.reserve(N);
        while (idx[pos] < 0)
        {
            idx[pos] = (int)people.size();
            vector<long long>::iterator it = upper_bound(s.begin() + pos + 1, s.end(), s[pos] + k);
            int next;
            if (it != s.end())
            {
                next = it - s.begin() - 1;
                people.push_back(s[next] - s[pos]);
            }
            else
            {
                it = upper_bound(s.begin() + 1, s.begin() + pos, k - (s[N] - s[pos]));
                next = it - s.begin() - 1;
                people.push_back(s[N] - s[pos] + s[next]);
            }
            // printf("%d -> %d (%lld)\n", pos, next, people.back());
            pos = next;
        }
        int head = idx[pos];
        int period = (int)people.size() - head;
        long long ans;
        if (R < head + period)
        {
            ans = 0;
            for (int i = 0; i < R; ++i)
                ans += people[i];
        }
        else
        {
            long long headSum = 0;
            for (int i = 0; i < head; ++i)
                headSum += people[i];
            long long periodSum = 0;
            for (int i = head; i < head + period; ++i)
                periodSum += people[i];
            int periodTimes = (R - head) / period;
            long long tailSum = 0;
            for (int i = head; i < head + (R - head) % period; ++i)
                tailSum += people[i];
            ans = headSum + periodSum * periodTimes + tailSum;
        }
        printf("Case #%d: %lld\n", idxCase + 1, ans);
    }
    return 0;
}

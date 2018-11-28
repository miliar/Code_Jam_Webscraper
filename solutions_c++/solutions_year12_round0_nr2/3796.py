#include <iostream>
#include <algorithm>
#include <vector>
#include <cstring>

int N;
int S;
int p;
std::vector<int> ts;
const int NMAX = 100;
const int SMAX = 100;
int memo[NMAX + 1][SMAX + 1];

void init()
{
    ts.clear();
}

void split(int x, int &a, int &b, int &c)
{
    int ave = x / 3;
    int rem = x % 3;
    if (0 == rem)
    {
        a = ave - 1;
        b = ave;
        c = ave + 1;
    }
    else if (1 == rem)
    {
        a = ave - 1;
        b = ave + 1;
        c = ave + 1;
    }
    else
    {
        a = ave;
        b = ave;
        c = ave + 2;
    }
}

bool valid(int x)
{
    return x >= 0 && x <= 10;
}

bool test_candidate(int x)
{
    int a, b, c;
    split(x, a, b, c);
    return valid(a) && valid(b) && valid(c);
}

int best_surprise(int x)
{
    int a, b, c;
    split(x, a, b, c);
    return c;
}

int best_normal(int x)
{
    return x / 3 + std::min(1, x % 3);
}

int f(int n, int s)
{
    int &result = memo[n][s];
    if (~memo[n][s])
    {
        return result;
    }
    if (0 == n)
    {
        if (0 == s)
        {
            return result = 0;
        }
        return result = -0x7fffffff;
    }
    result = f(n - 1, s) + (best_normal(ts[n - 1]) >= p);
    if (0 == s)
    {
        return result;
    }
    if (test_candidate(ts[n - 1]))
    {
        result = std::max(result, f(n - 1, s - 1) + (best_surprise(ts[n - 1]) >= p));
    }
    return result;
}

int solve()
{
    memset(&memo[0][0], 0xff, sizeof(int) * (NMAX + 1) * (SMAX + 1));
    return f(N, S);
}

int main()
{
    int test_count;
    std::cin >> test_count;
    for (int test_case = 1; test_case <= test_count; ++test_case)
    {
        init();
        std::cin >> N >> S >> p;
        for (int i = 0; i != N; ++i)
        {
            int t;
            std::cin >> t;
            ts.push_back(t);
        }
        std::cout << "Case #" << test_case << ": " << solve() << std::endl;
    }
    return 0;
}

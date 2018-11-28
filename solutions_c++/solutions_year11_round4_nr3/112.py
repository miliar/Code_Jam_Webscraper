#include <iostream>
#include <vector>

using namespace std;

const int N = 1010101;
bool not_prime[N];

int main()
{
    
    not_prime[1] = true;
    vector<int> primes;
    primes.reserve(N);
    for (int i = 2; i < N; ++i)
    {
        if (not_prime[i])
            continue;

        primes.push_back(i);

        for (int j = i + i; j < N; j += i)
        {
            not_prime[j] = true;
        }
    }

    int T;
    cin >> T;

    for (int K = 1; K <= T; ++K)
    {
        long long n;
        cin >> n;
        int ans = 1;
        if (n == 1)
            ans = 0;
        for (size_t i = 0, sz = primes.size(); i < sz; ++i)
        {
            int p = primes[i];
            if (p > n)
                break;
            long long px = p;
            while (px * p <= n)
            {
                px *= p;
                ++ans;
            }
        }
        cout << "Case #" << K << ": " << ans << "\n";
    }
}

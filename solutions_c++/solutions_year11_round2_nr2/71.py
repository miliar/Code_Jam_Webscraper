#include <iostream>
#include <vector>
#include <algorithm>

typedef std::pair<long long, long long> P;
typedef std::vector<P> V;

int main()
{
    int T;
    std::cin >> T;
    for (int t = 1 ; t <= T ; ++t)
    {
        long long max = 0;
        int c;
        long long d;
        std::cin >> c >> d;
        V v(c);
        for (int i = 0 ; i < c ; ++i)
            std::cin >> v[i].first >> v[i].second;
        std::sort(v.begin(), v.end());
        long long x = v[0].first;
        for (int i = 0 ; i < c ; ++i)
        {
            int f = v[i].first;
            int s = v[i].second;
            if (x > v[i].first)
            {
                long long m = x - v[i].first + d * (v[i].second - 1);
                x = v[i].first + m + d;
                if (m > max)
                    max = m;
            }
            else
            {
                long long m = d * (v[i].second - 1);
                x = v[i].first + d * v[i].second;
                if (m > max)
                    max = m;
            }
        }
        std::cout.setf(std::ios::fixed);
        std::cout.precision(7);
        std::cout << "Case #" << t << ": " << (double)max / 2 << "\n";
    }
    return 0;
}

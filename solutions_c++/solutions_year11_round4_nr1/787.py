#include <iostream>
#include <vector>
#include <algorithm>

typedef std::pair<int, int> P;
typedef std::vector<P> V;

int main()
{
    int T;
    std::cin >> T;
    for (int t = 1 ; t <= T ; ++t)
    {
        V v;
        double res = 0;
        int x, s, r, n;
        double tm;
        std::cin >> x >> s >> r >> tm >> n;
        for (int i = 0 ; i < n ; ++i)
        {
            int b, e, w;
            std::cin >> b >> e >> w;
            v.push_back(P(w, e - b));
            x -= e - b;
        }
        v.push_back(P(0, x));
        std::sort(v.begin(), v.end());
        for (size_t i = 0 ; i < v.size() ; ++i)
        {
            double ts = (double)v[i].second / (v[i].first + s);
            double tr = (double)v[i].second / (v[i].first + r);
            if (tm > 0.000000001)
            {
                if (tr > tm)
                {
                    res += tm;
                    double tt = (v[i].second - tm * (v[i].first + r)) / (v[i].first + s);
                    res += tt;
                    tm = 0;
                }
                else
                {
                    tm -= tr;
                    res += tr;
                }
            }
            else 
            {
                res += ts;
            }
        }
        std::cout << "Case #" << t << ": ";
        std::cout.setf(std::ios::fixed);
        std::cout.precision(7);
        std::cout << res << "\n";
    }
	return 0;
}


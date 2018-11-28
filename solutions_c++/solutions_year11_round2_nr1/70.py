#include <iostream>
#include <string>
#include <vector>

int main()
{
    int T;
    std::cin >> T;
    for (int t = 1 ; t <= T ; ++t)
    {
        int n;
        std::cin >> n;
        std::vector<std::string> a(n);
        for (int i = 0 ; i < n ; ++i)
            std::cin >> a[i];

        std::vector<double> wp(n);
        std::vector<double> owp(n);
        std::vector<double> oowp(n);
        for (int i = 0 ; i < n ; ++i)
        {
            int win = 0, lose = 0;
            for (int j = 0 ; j < n ; ++j)
                switch (a[i][j])
                {
                case '0':
                    ++lose;
                    break;
                case '1':
                    ++win;
                    break;
                }
            wp[i] = (double)win / (lose + win);
        }

        for (int i = 0 ; i < n ; ++i)
        {
            double sum = 0;
            int count = 0;
            for (int j = 0 ; j < n ; ++j)
            {
                if (i != j && a[i][j] != '.')
                {
                    int win = 0, all = 0;
                    for (int k = 0 ; k < n ; ++k)
                        if (k != i && k != j && a[j][k] != '.')
                        {
                            ++all;
                            win += a[j][k] - '0';
                        }
                    ++count;
                    sum += (double)win / all;
                }
            }
            owp[i] = (double)sum / count;
        }

        for (int i = 0 ; i < n ; ++i)
        {
            double sum = 0;
            int count = 0;
            for (int j = 0 ; j < n ; ++j)
                if (i != j && a[i][j] != '.')
                {
                    ++count;
                    sum += owp[j];
                }
            oowp[i] = sum / count;
        }

        std::cout.setf(std::ios::fixed);
        std::cout.precision(7);
        std::cout << "Case #" << t << ":\n";
        for (int i = 0 ; i < n ; ++i)
        {
            //std::cout << "WP: " << wp[i] << " OWP: " << owp[i] << " OOWP: " << oowp[i] << "\n";
            std::cout << wp[i] * 0.25 + owp[i] * 0.5 + oowp[i] * 0.25 << "\n";
        }

    }
    return 0;
}

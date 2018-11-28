#include <iostream>
#include <list>

typedef std::list<std::pair<int, int> > B;

int main()
{
    int T;
    std::cin >> T;
    for (int t = 1 ; t <= T ; ++t)
    {
        B b1, b2;
        int res = 0;
        int p1 = 1;
        int p2 = 1;
        int n;
        std::cin >> n;
        for (int i = 0 ; i < n ; ++i)
        {
            char c;
            int p;
            std::cin >> c >> p;
            if (c == 'O')
                b1.push_back(std::make_pair(i, p));
            else
                b2.push_back(std::make_pair(i, p));
        }
        B::iterator i1 = b1.begin(), i2 = b2.begin();
        int cur = 0;
        while (i1 != b1.end() || i2 != b2.end())
        {
            bool inc = false;
            ++res;
            if (i1 != b1.end())
            {
                if (i1->second == p1)
                {
                    if (cur == i1->first)
                    {
                        ++i1;
                        inc = true;
                    }
                }
                else if (i1->second > p1)
                    ++p1;
                else
                    --p1;
            }
            if (i2 != b2.end())
            {
                if (i2->second == p2)
                {
                    if (cur == i2->first)
                    {
                        ++i2;
                        inc = true;
                    }
                }
                else if (i2->second > p2)
                    ++p2;
                else
                    --p2;
            }

            if (inc)
                ++cur;
        }
        std::cout << "Case #" << t << ": " << res << "\n";
    }
}

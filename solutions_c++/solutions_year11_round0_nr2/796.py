#include <iostream>
#include <list>

typedef std::list<int> L;
int cr[36][36];
bool dest[36][36];

int main()
{
    int T;
    std::cin >> T;
    for (int t = 1 ; t <= T ; ++t)
    {
        L res;

        for (int i = 0 ; i < 36 ; ++i)
        {
            for (int j = 0 ; j < 36 ; ++j)
            {
                cr[i][j] = -1;
                dest[i][j] = false;
            }
        }

        int C, D;
        std::cin >> C;
        while (C--)
        {
            char c1, c2, c3;
            std::cin >> c1 >> c2 >> c3;
            cr[c1-'A'][c2-'A'] = c3 - 'A';
            cr[c2-'A'][c1-'A'] = c3 - 'A';
        }

        std::cin >> D;
        while (D--)
        {
            char d1, d2;
            std::cin >> d1 >> d2;
            dest[d1-'A'][d2-'A'] = true;
            dest[d2-'A'][d1-'A'] = true;
        }

        int N;
        std::cin >> N;
        while (N--)
        {
            char c;
            std::cin >> c;
            c -= 'A';
            if (res.empty())
            {
                res.push_back(c);
            }
            else
            {
                if (cr[c][res.back()] >= 0)
                {
                    res.back() = cr[c][res.back()];
                }
                else 
                {
                    for (L::iterator i = res.begin() ; i != res.end() ; ++i)
                        if (dest[c][*i])
                        {
                            res.clear();
                            break;
                        }
                    if (!res.empty())
                        res.push_back(c);
                }
            }
        }

        std::cout << "Case #" << t << ": [";
        bool first = true;
        for (L::iterator i = res.begin() ; i != res.end() ; ++i)
        {
            if (!first)
                std::cout << ", ";
            first = false;
            std::cout << (char)('A' + *i);
        }
        std::cout << "]\n";
    }
}

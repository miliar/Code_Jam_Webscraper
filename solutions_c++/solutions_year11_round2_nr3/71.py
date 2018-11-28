#include <iostream>
#include <vector>
#include <list>
#include <algorithm>
#include <set>

typedef std::vector<int> R;
typedef std::list<R> H;
typedef std::set<int> S;

H h;
int n, m, colors;
bool ok;
int max;
int c;
R f;
R curr;

void f1(int i)
{
    if (i >= n)
    {
        bool b = true;
        for (H::iterator r = h.begin() ; r != h.end() ; ++r)
        {
            S s;
            for (size_t i = 0 ; i < r->size() ; ++i)
                s.insert(curr[(*r)[i] - 1]);
            if (s.size() != c)
            {
                b = false;
                break;
            }
        }
        if (b)
        {
            ok = true;
            f = curr;
        }
        return;
    }
    for (int col = 1 ; col <= c ; ++col)
    {
        curr[i] = col;
        f1(i + 1);
    }
}

int main()
{
    int T;
    std::cin >> T;
    for (int t = 1 ; t <= T ; ++t)
    {
        h.clear();

        std::cin >> n >> m;
        std::vector<int> u(m), v(m);
        for (int i = 0 ; i < m ; ++i)
            std::cin >> u[i];
        for (int i = 0 ; i < m ; ++i)
            std::cin >> v[i];
        R r(n);
        for (int i = 1 ; i <= n ; ++i)
            r[i-1] = i;
        h.push_back(r);
        f.clear();
        f.resize(n, 1);

        for (int i = 0 ; i < m ; ++i)
        {
            for (H::iterator r = h.begin() ; r != h.end() ; ++r)
            {
                R::iterator w1 = std::find(r->begin(), r->end(), u[i]);
                R::iterator w2 = std::find(r->begin(), r->end(), v[i]);
                if (w1 != r->end() && w2 != r->end())
                {
                    R r1;
                    R r2;
                    bool second = false;
                    for (R::iterator j = r->begin() ; j != r->end() ; ++j)
                    {
                        if (second)
                        {
                            r2.push_back(*j);
                            if (w1 == j || w2 == j)
                            {
                                r1.push_back(*j);
                                second = false;
                            }
                        }
                        else
                        {
                            r1.push_back(*j);
                            if (w1 == j || w2 == j)
                            {
                                r2.push_back(*j);
                                second = true;
                            }
                        }
                    }
                    *r = r1;
                    h.push_back(r2);
                    break;
                }
            }
        }

        colors = n;
        for (H::iterator r = h.begin() ; r != h.end() ; ++r)
            if ((int)r->size() < colors)
                colors = (int)r->size();

        curr.clear();
        curr.resize(n, 1);
        ok = false;
        for (c = colors ; c > 0 ; --c)
        {
            f1(0);
            if (ok)
                break;
        }

        std::cout << "Case #" << t << ": " << c << "\n";
        for (size_t i = 0 ; i < f.size() ; ++i)
        {
            if (i)
                std::cout << " ";
            std::cout << f[i];
        }
        std::cout << "\n";

    }
    return 0;
}

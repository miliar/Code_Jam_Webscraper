#include <iostream>

inline void incn(std::string& s)
{
    for (register size_t i = s.length(); i > 0;)
    {
        --i;
        if (++s[i] == ':')
            s[i] = '0';
        else
            return;
    }
    //s = '1' + s;
    s[0] = ':';
}

void tcase(int tc)
{
    std::string a, b;
    std::cin >> a >> b;

    int res = 0;
    const size_t dnum = a.length();

    for (std::string n = a; n <= b; incn(n))
    {
        size_t is = dnum;
        if (dnum == 4 && n[0] == n[2] && n[1] == n[3]) is = 2;
        else if (dnum == 6 && n[0] == n[3] && n[1] == n[4] && n[2] == n[5]) is = 3;
        else if (dnum == 6 && n[0] == n[2] && n[0] == n[4] && n[1] == n[3] && n[1] == n[5]) is = 2;

        for (size_t i = 1; i < is; ++i)
        {
            if (n[i] == '0') continue;

            for (size_t j = 0; j < dnum; ++j)
            {
                if (a[j] > n[(i+j)%dnum]) goto fail;
                else if (a[j] < n[(i+j)%dnum]) break;
            }
            for (size_t j = 0; j < dnum; ++j)
            {
                if (b[j] < n[(i+j)%dnum]) goto fail;
                else if (b[j] > n[(i+j)%dnum]) break;
            }
            for (size_t j = 0; j < dnum; ++j)
            {
                if (n[j] < n[(i+j)%dnum]) goto set;
                else if (n[j] > n[(i+j)%dnum]) goto fail;
            }
            continue;

        set:
            /*std::cout << n << ' ' << i << ' ';
            for (size_t j = 0; j < dnum; ++j) std::cout << n[(i+j)%dnum];
            std::cout << '\n';*/
            ++res;

        fail:
            ;
        }
    }

    std::cout << "Case #" << tc << ": " << res << '\n';
}

int main()
{
    int n;
    std::cin >> n;

    for (int i = 0; i < n; ++i)
      tcase(i+1);
}

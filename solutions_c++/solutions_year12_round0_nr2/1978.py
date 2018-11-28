#include <iostream>

void tcase(int tc)
{
    int n, s, p;
    std::cin >> n >> s >> p;

    int res = 0;
    for (int i = 0; i < n; ++i)
    {
        int score;
        std::cin >> score;

        if ((score+2)/3 >= p) ++res;
        else if (s > 0 && score >= 2 && score % 3 != 1 && (score+5)/3 >= p)
        {
            ++res;
            --s;
        }
    }

    std::cout << "Case #" << tc << ": " << res << '\n';
}

int main()
{
    int n;
    std::cin >> n;

    for (int i = 0; i < n; ++i)
        tcase(i + 1);

    return 0;
}

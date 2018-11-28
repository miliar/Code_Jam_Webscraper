#include <iostream>

int main(void)
{
    int T;
    std::cin >> T;
    for (int t = 1; t <= T; ++t) {
        int N, S, p;
        std::cin >> N >> S >> p;
        int min_no_surprise = p - 1;
        if (min_no_surprise < 0)
            min_no_surprise = 0;
        min_no_surprise = min_no_surprise + min_no_surprise + p;
        int min_surprise = p - 2;
        if (min_surprise < 0)
            min_surprise = 0;
        min_surprise = min_surprise + min_surprise + p;
        int y = 0;
        for (int n = 0; n < N; ++n) {
            int t;
            std::cin >> t;
            if (t >= min_no_surprise) {
                ++y;
            } else if (S > 0 && t >= min_surprise) {
                ++y;
                --S;
            }
        }
        std::cout << "Case #" << t << ": " << y << std::endl;
    }
}

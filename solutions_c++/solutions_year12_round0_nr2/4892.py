#include <iostream>
#include <vector>

int main()
{
    int T; std::cin >> T; std::cin.ignore();

    for (int i = 1; i <= T; i++)
    {
        std::vector<int> vect;
        int N, S, p; std::cin >> N; std::cin >> S; std::cin >> p;
        int total = 0;
        for (int j = 0; j < N; ++j)
        {
            int tmp;
            std::cin >> tmp;
            vect.push_back(tmp);
        }
        for (int j = 0; j < N; ++j)
        {
            if (vect[j] >= 3 * p - 2)
                total++;
            else if (vect[j] >= (3 * p - 4) && S > 0 && vect[j] >= p)
            {
                S--; total++;
            }
        }
        std::cout << "Case #" << i << ": " << total << std::endl;
    }
}

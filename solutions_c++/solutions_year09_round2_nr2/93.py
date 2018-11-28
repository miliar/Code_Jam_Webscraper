#include <iostream>
#include <string>
#include <algorithm>

int main()
{
    int T;
    std::string N;
    std::cin >> T;
    std::getline(std::cin, N);
    for (int t = 1 ; t <= T ; ++t)
    {
        std::getline(std::cin, N);
        bool des = true;
        for (int i = 0 ; i < N.size() - 1 ; ++i)
            if (N[i] < N[i+1])
            {
                des = false;
                break;
            }

        std::string M;
        if (des)
        {
            std::sort(N.begin(), N.end());
            int i = 0;
            for ( ; i < N.size() ; ++i)
                if (N[i] != '0')
                    break;

            M = "00";
            M[0] = N[i];
            if (i > 0)
                M += N.substr(0, i);
            if ((int)N.size() - i - 1 > 0)
                M += N.substr(i + 1, N.size() - i - 1);
        }
        else
        {
            // find the first index, breaking the order
            int i = N.size() - 2;
            for ( ; i >= 0 ; --i)
                if (N[i] < N[i+1])
                    break;
            // i should be replaced with the greater
            for (int j = i + 1 ; j < N.size() && N[j] > N[i] ; ++j)
                ;
            --j;
            std::swap(N[i], N[j]);
            std::sort(N.begin() + i + 1, N.end());
            M = N;
        }
        std::cout << "Case #" << t << ": " << M << "\n";
    }
    return 0;
}

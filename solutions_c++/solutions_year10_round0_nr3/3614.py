#include <iostream>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <memory.h>
#include <vector>
#include <deque>
#include <map>

int main(int argc, char *argv[])
{
    int T = 0;

    std::vector<unsigned long> coaster;

    freopen("C-small-attempt1.in","r",stdin);
    freopen("C-small.out","w",stdout);

    std::cin >> T;

    for (int i = 0; i < T; ++i)
    {
        unsigned long R, K, N;
        uint64_t  euros = 0;
        std::deque<unsigned long> groups;

        std::cin >> R >> K >> N;

        for (size_t j = 0; j < N; ++j)
        {
            size_t gi;
            std::cin >> gi;
            groups.push_back(gi);
        }

        for (size_t j = 0; j < R; ++j)
        {
            unsigned long capacity = 0;

            if (groups.empty())
                break;

            do
            {
                if (groups.empty())
                    break;

                if (K - capacity >= groups[0])
                {
                    capacity += groups[0];
                    coaster.push_back(groups[0]);
                    groups.pop_front();
                }
                else
                    break;
            }
            while (capacity < K);

            euros += capacity;

            for ( size_t m = 0; m < coaster.size(); ++m)
                groups.push_back(coaster[m]);

            coaster.clear();
        }

        std::cout << "Case #" << i+1 << ": " << euros << std::endl;
    }

    return 0;
}

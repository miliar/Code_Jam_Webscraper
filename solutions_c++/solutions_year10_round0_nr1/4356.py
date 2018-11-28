#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <memory.h>
#include <vector>
#include <utility>

int main(int argc, char *argv[])
{
    int T = 0;
    int N = 0;
    unsigned long K = 0;
    int plugs[30];
    std::vector<std::pair<int,int> > tests;

//    freopen("A-small-attempt1.in","r",stdin);
//    freopen("A-small-attempt1.out","w",stdout);

    std::cin >> T;

    for (int i = 0; i < T; ++i)
    {
        std::cin >> N >> K;
        tests.push_back(std::make_pair(N,K));
    }

    for (size_t i = 0; i < tests.size(); ++i)
    {
        memset(plugs,0,sizeof(int)*30);

        for (int j = 0; j < tests[i].second; ++j)
        {
            int idx = 0;
            for ( int m = 0; m < tests[i].first; ++m)
            {
                if (plugs[m])
                    idx++;
                else
                    break;
            }

            for (int m = 0; m <= idx; ++m)
            {
                plugs[m] = plugs[m] ? 0 : 1;
            }
        }

        int idx = 0;
        for (int m = 0; m < tests[i].first; ++m)
        {
            if (plugs[m])
                idx++;
        }

        std::cout << "Case #" << i+1 << ": " << ((idx == tests[i].first) ? "ON" : "OFF") << std::endl;
    }

    return 0;
}

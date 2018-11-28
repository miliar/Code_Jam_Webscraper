/* Song Qiang
 */ 

#include <cmath>

#include <string>
#include <vector>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <limits>
#include <list>
#include <numeric>

using namespace std;

int
main(int argc, const char **argv)
{
    ifstream in(argv[1]);
        
    int T;
    in >> T;

    for (size_t t = 0; t < T; ++t)
    {
        int N;
        in >> N;
        vector<int> candies(N, 0);
        for (size_t i = 0; i < N; ++i)
            in >> candies[i];

        // int sum;
        // int smallest;
        // for (size_t i = 0; i < N; ++i)
        // {
        //     sum += candies[i];
        //     smallest = min(smallest, candies[i]);
        // }
        // int max_candies = sum - smallest;

        const int max_candies =
            accumulate(candies.begin(), candies.end(), int(0)) -
            *min_element(candies.begin(), candies.end());
        
        bool possible = true;
        for (size_t i = 0; i < 21; ++i)
        {
            int s = 0;
            for (size_t j = 0; j < candies.size(); ++j)
                s += (candies[j] >> i) & 1;
            if (s % 2 != 0)
            {
                possible  = false;
                break;
            }
        }

        if (possible)
            cout << "Case #" << t+1 << ": " << max_candies << endl;
        else
            cout << "Case #" << t+1 << ": NO" << endl;
    }
  
    return EXIT_SUCCESS;
}

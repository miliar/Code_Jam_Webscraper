#include <iostream>
#include <fstream>
#include <queue>
#include <vector>
#include <sstream>
#include <string>
#include <algorithm>

#define MAXN 100000
#define MAXH 10000000000000000
const char outfile[] = "harm.out";

long long band[MAXN];

bool testInHarmoney(long long N,long long f)
{
    for (long long i = 0; i < N; ++i)
    {
        if (band[i] < f)
            if((f % band[i]) == 0)
                continue;
            else
                return false;
        else
            if((band[i] % f) == 0)
                continue;
            else
                return false;
    }
    return true;
}

int main(int argc, char** argv)
{
    if (argc != 2)
    {
        return 1;
    }
    std::ifstream file(argv[1]);
    int nCases;
    file >> nCases;
    std::ofstream res(outfile);

    for (int index = 1; index <= nCases; ++index)
    {
        res << "Case #" << index << ": " ;
        long long N, L, H;
        file >> N >> L >> H;

        for (long long i = 0; i < N; ++i)
            file >> band[i];

        int inHarmoney = 0;
        long long f = 0;
        for (f = L; f <= H; ++f)
        {
            if (testInHarmoney(N,f) == true)
            {
                inHarmoney = true;
                break;
            }
        }
        if (inHarmoney)
            res << f << std::endl;
        else
            res << "NO" << std::endl;
    }
    return 0;
}


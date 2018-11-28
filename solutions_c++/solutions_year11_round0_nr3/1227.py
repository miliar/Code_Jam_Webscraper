#include <iostream>
#include <fstream>
#include <queue>
#include <vector>
#include <sstream>
#include <string>
#include <algorithm>

const char outfile[] = "Candies.out";

long VectorSum(const std::vector<long>& v)
{
    long result = 0;
    for (std::vector<long>::const_iterator it = v.begin();
            it != v.end(); ++it)
        result += *it;
    return result;
}

long VectorXor(const std::vector<long>& v)
{
    long result = 0;
    for (std::vector<long>::const_iterator it = v.begin();
            it != v.end(); ++it)
        result ^= *it;
    return result;
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
        int vLength;
        file >> vLength;
        std::vector<long> candies;

        for (int i = 0; i < vLength; ++i)
        {
            long curr;
            file >> curr;
            candies.push_back(curr);
        }

        if (VectorXor(candies) == 0)
        {
            std::sort(candies.begin(), candies.end());
            candies.erase(candies.begin());
            res << "Case #" << index << ": " << VectorSum(candies) << std::endl;
        }
        else
        {
            res << "Case #" << index << ": NO" << std::endl;
        }
    }
    return 0;

}


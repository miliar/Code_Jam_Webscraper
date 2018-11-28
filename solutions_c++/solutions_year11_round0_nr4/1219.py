#include <iostream>
#include <fstream>
#include <queue>
#include <vector>
#include <sstream>
#include <string>
#include <algorithm>

const char outfile[] = "GoroSort.out";

int Solve(std::vector<int>& input)
{
    std::vector<int> forSorting;
    forSorting.insert(forSorting.begin(), input.begin(), input.end());
    std::sort(forSorting.begin(), forSorting.end());

    //Get elements which are in not proper place
    //remaining will be held down every time, no matter what!
    int res = 0;
    for (int i = 0; i < input.size(); ++i)
        if (input[i] != forSorting[i])
            res++;
    return res;
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
        int vecLen;
        file >> vecLen;
        std::vector<int> input;
        for (int i = 0; i < vecLen; ++i)
        {
            int e;
            file >> e;
            input.push_back(e);
        }
        res << "Case #" << index << ": " << Solve(input) << std::endl;
    }

    return 0;
}
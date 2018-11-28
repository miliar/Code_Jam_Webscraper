// \author martin.trenkmann@gmail.com
// $ g++ --std=c++0x gcj2011-rX-pY.cpp

// c std lib
#include <cstdint>
//#include <cstdlib>
//#include <cctype>
//#include <cmath>

// c++ std lib
#include <iostream>
//#include <sstream>
#include <string>

// stl containers
//#inlcude <multimap>
//#inlcude <multiset>
//#include <bitset>
#include <vector>
//#include <deque>
//#include <stack>
#include <list>
//#inlcude <map>
//#inlcude <set>

// stl algorithms / misc
//#include <algorithm>
//#include <utility>
//#include <numeric>
//#include <limits>

int
main(int argc, char* argv[])
{
    unsigned t, r, c;
    std::cin >> t;
    for (unsigned i(0); i != t; ++i)
    {
        std::cin >> r >> c;
        std::vector<std::string> pic;
        for (unsigned j(0); j != r; ++j)
        {
            std::string line;
            std::cin >> line;
            pic.push_back(line);
        }
        
        std::cout << "Case #" << i+1 << ":\n";
        
        try
        {          
            for (auto r(0); r != pic.size(); ++r)
            {
                for (auto c(0); c != pic[r].size(); ++c)
                {
                    if (pic[r][c] == '#')
                    {
                        if (pic.at(r).at(c+1) == '#' &&
                            pic.at(r+1).at(c) == '#' &&
                            pic.at(r+1).at(c+1) == '#')
                        {
                            pic[r][c] = '/';
                            pic[r][c+1] = '\\';
                            pic[r+1][c] = '\\';
                            pic[r+1][c+1] = '/';
                        }
                        else
                        {
                            throw std::exception();
                        }
                    }
                }
            }
            for (auto it(pic.begin()); it != pic.end(); ++it)
            {
                std::cout << *it << std::endl;
            }
        }
        catch (...)
        {
            std::cout << "Impossible" << std::endl;
        }
    }
    return 0;
}


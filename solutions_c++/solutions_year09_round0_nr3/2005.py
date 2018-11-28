////
//// Welcome to Code Jam
////
#include <iostream>
#include <iomanip>
#include <cstdlib> 
#include <fstream>
#include <string>

const std::string WELCOME("welcome to code jam");

int
calc(std::string str, std::string findStr)
{
    if (str.size() < findStr.size())
        return 0;

    std::string::size_type idx;
    int n = 0;

    if (findStr.size() == 1) {
        idx = -1;
        while ((idx = str.find(findStr, idx + 1)) != std::string::npos) 
            ++n;

        return n;
    }
    else {
        idx = -1;
        while ((idx = str.find(findStr[0], idx + 1)) != std::string::npos) {
            n += calc(str.substr(idx + 1), findStr.substr(1));
            n %= 10000;
        }

        return n;
    }
}



int
main (int argc, char **argv)
{
    if (argc < 2) {
        std::cerr << "Usage: " << argv[0] << " filename" << std::endl;
        exit(EXIT_FAILURE);
    }

    std::ifstream fin(argv[1]);

    if (!fin) {
        std::cerr << "cannot open input file: " << argv[1] << std::endl;
        exit(EXIT_FAILURE);
    }

    /// =====================================================================

    std::string inputLine;

    /// number of test cases
    getline(fin, inputLine);
    const int nTestcase = atoi(inputLine.c_str());


    /// for each test case
    std::string testcase;
        
    for (int i = 1; i <= nTestcase; ++i) {
        getline(fin, testcase);

        std::cout << "Case #" << i << ": "
                  << std::setw(4) << std::setfill('0')
                  << calc(testcase, WELCOME)
                  << std::endl;
    }
}
    

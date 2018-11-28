////
//// Watersheds
////
#include <iostream>
#include <cstdlib> 
#include <fstream>
#include <string>

#include "ElevationMap.h"

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

    std::string::size_type idx;
    std::string inputLine;

    /// number of maps
    getline(fin, inputLine);
    const int nMap = atoi(inputLine.c_str());


    /// for each map
    int H = 0;
    int W = 0;

    ElevationMap elevationMap;
        
    for (int i = 1; i <= nMap; ++i) {
        getline(fin, inputLine);

        idx = inputLine.find(' ');
        H = atoi(inputLine.substr(0, idx).c_str());

        inputLine = inputLine.substr(++idx);
        W = atoi(inputLine.c_str());

        std::cout << "Case #" << i << ":" << std::endl;

        /// map initialization
        elevationMap = ElevationMap(H, W);

        /// for each row
        for (int rowNumber = 1; rowNumber <= H; ++rowNumber) {
            getline(fin, inputLine);

            elevationMap.insert(rowNumber, inputLine);
        }

        elevationMap.setAllBasinLabel();

        std::cout << elevationMap;
    }
}
    

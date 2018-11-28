//
//  main.cpp
//  CodeJam
//
//  Created by Nikolay Lukash on 4/14/12.
//  Copyright (c) 2012 Google. All rights reserved.
//

#include <iostream>
#include <utility>
#include <iostream>
#include <fstream>
#include <string>
#include <cmath>
#include <sstream>
#include <algorithm>
#include <stdio.h>
#include <sys/time.h>
#include <time.h>
#include "GCJ_2012.hpp"

using namespace std;

//void read_kernel_from_file(std::string& file_name, std::string& kernel_source){
//    std::ifstream ifs(file_name.c_str(), std::ifstream::in);
//    std::string line;
//    std::ostringstream ost;
//    while (std::getline(ifs, line)) {
//        ost<<line<<std::endl;
//    }
//    kernel_source = ost.str();
//}

int main (int argc, const char * argv[])
{
    string input_file = "/Users/nikolaylukash/Development/GCJ/A-small-attempt0.in";
    string output_file = "/Users/nikolaylukash/Development/GCJ/Qual_A_out.txt";
    //
    std::ifstream ifs(input_file.c_str(), std::ifstream::in);
    std::ofstream ofs(output_file.c_str(), std::ofstream::out);
    //
    SpeakingInTongues speak_in_tongues;
    int nTest;
    string line;
    getline(ifs, line);
    istringstream iss(line);
    iss>>nTest;
    for (int iTest = 1; iTest <= nTest; iTest++) {  
        std::getline(ifs, line);
        string answer = speak_in_tongues.translate(line);
        ofs<<"Case #"<<iTest<<": ";
        ofs<<answer<<std::endl;
    }
    ofs.close();
    return 0;
}


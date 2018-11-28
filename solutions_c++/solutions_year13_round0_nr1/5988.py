//
//  main.cpp
//  GCJA
//
//  Created by Sargo Darya on 13.04.13.
//  Copyright (c) 2013 Sargo Darya. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>

#include "TTT.h"

int testcases = 0;
int testcase = 1;

int main(int argc, const char * argv[])
{
  if(argv[1] == NULL) {
    std::cout << "No filename given" << std::endl;
    exit(0);
  }
  
  // Load testfile
  std::ifstream infile(argv[1]);
  std::vector<std::string> lines;
  for( std::string line; getline( infile, line ); )
  {
    if(testcases == 0) {
      testcases = atoi(line.c_str());
    } else {
      if (line == "") {
        // testcase is done
        // start next one
        TTT::Test(testcase, lines);
        std::cout << std::endl;
        lines.clear();
        testcase++;
      } else {
        lines.push_back(line);
      }
    }
  }
  
  return 0;
}


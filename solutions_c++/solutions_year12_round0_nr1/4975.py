/*
 * =====================================================================================
 *
 *       Filename:  main.cpp
 *
 *    Description:  
 *
 *        Version:  1.0
 *        Created:  
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  Moritz Schaefer (), mollitz@gmail.com
 *        Company:  
 *
 * =====================================================================================
 */

#include <vector>
#include <string>
#include <sstream>
#include <iomanip>
#include <algorithm>
#include <iostream>
#include <map>
#include <cstring>

using namespace std;

char dict[256];


void preCalculation()
{
    memset(dict, 0, 256);
    dict['a'] = 'y';
    dict['o'] = 'e';
    dict['z'] = 'q';
    dict['q'] = 'z';
    std::vector<std::string> input;
    std::vector<std::string> output;
    input.push_back(std::string("ejp mysljylc kd kxveddknmc re jsicpdrysi"));
    input.push_back(std::string("rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd"));
    input.push_back(std::string("de kr kd eoya kw aej tysr re ujdr lkgc jv"));
    output.push_back("our language is impossible to understand");
    output.push_back("there are twenty six factorial possibilities");
    output.push_back("so it is okay if you want to just give up");
    for(int i=0; i<input.size(); i++)
    {
        for(int j=0; j<input[i].size(); j++)
        {
            dict[input[i][j]] = output[i][j];
            //dict[output[i][j]] = input[i][j];
        }
    }
}


string calculate()
{
    stringstream out; //put all to print in out...
    // use setprecision for more floating point digits
    std::string in;
    std::getline(std::cin, in);
    
    for(int i=0; i<in.size(); i++)
    {
        out << dict[in[i]];
    }

    return out.str();
}


int main(int argc, char *argv[])
{
    int cases;
    cin >> cases;
    std::cin.get(); //delete newline
    preCalculation();
    for(int i = 0; i < cases; i++)
    {
        cout << "Case #" << i+1 << ": " << calculate() << endl;
    }
    return 0;
}

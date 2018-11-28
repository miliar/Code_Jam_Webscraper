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

using namespace std;

void preCalculation()
{}

string calculate()
{
    stringstream out; //put all to print in out...
    // use setprecision for more floating point digits
    int n, s, p;
    std::cin >> n >> s >> p;
    int counter = 0;
    for(int i=0; i<n; i++)
    {
        int total; 
        std::cin >> total;
        int divisor = total / 3;
        switch(total % 3)
        {
            case 0:
            if(divisor == 0 && p > 0) break;
            if(divisor >= p) counter++;
            else if(divisor+1 >= p && s) {counter++; s--;}
            break;
            case 1:
            if(divisor+1 >= p) counter++;
            break;
            case 2:
            if(divisor+1 >=p ) counter++;
            else if(divisor+2>=p && s) {counter++; s--;}
            break;
        }
    }
    out << counter;

    return out.str();
}


int main(int argc, char *argv[])
{
    int cases;
    cin >> cases;
    preCalculation();
    for(int i = 0; i < cases; i++)
    {
        cout << "Case #" << i+1 << ": " << calculate() << endl;
    }
    return 0;
}

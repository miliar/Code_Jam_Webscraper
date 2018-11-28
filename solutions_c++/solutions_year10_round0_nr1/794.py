/*
 * =====================================================================================
 *
 *       Filename:  snapperchain.cpp
 *
 *    Description:
 *
 *        Version:  1.0
 *        Created:  05/07/2010 11:06:32 PM
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  YOUR NAME (),
 *        Company:
 *
 * =====================================================================================
 */

#include <iostream>
#include <fstream>
#include <iomanip>
#include <cmath>


using std::cout;
using std::endl;
using std::ifstream;
using namespace std;

bool snapperchain (long nsnappers, long nsnaps) {
    long base = pow(2, nsnappers);
    long num = nsnaps + 1;
    if (num%base == 0)
        return true;
    else
        return false;
}

int main() {
    // ifstream ifs("A-small-attempt0.in");
    ifstream ifs("A-large.in");
    int ntestcases;
    ifs>>ntestcases;

    long N, K;
    bool result;
    for (int i = 0; i < ntestcases; ++i) {
        ifs>>N>>K;
        result = snapperchain(N, K);
        cout<<"Case #"<<i+1<<": "<<(result?"ON":"OFF")<<endl;
    }
}


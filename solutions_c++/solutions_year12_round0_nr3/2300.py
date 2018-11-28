// =========================================================
//
//       Filename:  Recycled Numbers.cpp
//
//    Description:
//
//        Version:  1.0
//        Created:  04/14/2012
//       Revision:  none
//       Compiler:  g++
//
//         Author:  Tao Lin, tlin005@gmail.com
//        Company:  U of California Riverside
//      Copyright:  Copyright (c) 04/14/2012
//
// =========================================================

#include <iostream>
#include <string.h>
#include <math.h>

using namespace std;

#define MAXNUM 200

unsigned int findPairs(unsigned int n, unsigned int upbound)
{
    unsigned int m;
    unsigned int d;

    // leading digit
    d = 1;
    m = n/10;
    while (m > 0)
    {
        m /= 10;
        d *= 10;
    }

    unsigned int result = 0;
    //unsigned int min = n;
    // recycle number
    for (m = (n/10) + (n%10)*d; m != n; m = (m/10) + (m%10)*d)
    {
        if (m < d)  continue;  // leading zero
        if (m > upbound)  continue;  // skip out-bound

        //if (m < min) min = m;
        //result++;
        if (m > n) result++;
    }

    //if (min < n)    result = 0;  // only minimun in the series counts
    //result = result * (result+1) / 2;
    //if (result > 0) cout << n << '\t' << result << endl;

    return result;
}

unsigned int solve(unsigned int A, unsigned int B)
{
    if (A >= B)
        return 0;

    int result = 0;

    for (unsigned int i=A; i<B; ++i)
    {
        result += findPairs(i, B);
    }

    return result;
}

int main()
{
    unsigned int case_no;
    unsigned int A, B;
    unsigned int result;

    // load input
    cin >> case_no;

    for (unsigned int i = 0; i < case_no; i++)
    {
        cin >> A;
        cin >> B;
        // sove problem
        result = solve(A, B);
        cout << "Case #" << i+1 << ": ";
        cout << result << endl;
    }

    return 0;

}

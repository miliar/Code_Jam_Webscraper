///////////////////////////////////////////////////////////////////////
/////    The code is written for Google Code Jam 2012 contest.    /////
/////    You may use any part of this code without exception.     /////
/////    The author is not responsible for any consequences       /////
/////    of using this code.                                      /////
/////                                                             /////
/////    Author: Andrey Rubtsov                                   /////
///////////////////////////////////////////////////////////////////////

#define _CRT_SECURE_NO_WARNINGS
#include <algorithm>
#include <bitset>
#include <complex>
#include <deque>
#include <exception>
#include <fstream>
#include <functional>
#include <hash_map>
#include <hash_set>
#include <iomanip>
#include <ios>
#include <iosfwd>
#include <iostream>
#include <istream>
#include <iterator>
#include <limits>
#include <list>
#include <locale>
#include <map>
#include <memory>
#include <new>
#include <numeric>
#include <ostream>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <stdexcept>
#include <streambuf>
#include <string>
#include <strstream>
#include <utility>
#include <valarray>
#include <vector>
#include <cctype>
#include <cmath>
#include <cstdarg>
#include <cstdio>
#include <cstdlib>
#include <ctime>

using namespace std;

#define PROBLEM_NAME "C"
#define LARGE_INPUT 1

#if LARGE_INPUT
    #define INPUT_FILE PROBLEM_NAME "-large.in"
    #define OUTPUT_FILE PROBLEM_NAME "-large.out"
#else
    #define INPUT_FILE PROBLEM_NAME "-small-attempt.in"
    #define OUTPUT_FILE PROBLEM_NAME "-small.out"
#endif

int numgrp[1000001];
int grp[1000001];

int main()
{
    freopen(INPUT_FILE,"r",stdin);
    freopen(OUTPUT_FILE,"w",stdout);

    int T;
    cin >> T;

    for (int i = 0; i < T; ++i)
    {
        int A, B;
        cin >> A >> B;
        int g = 0;
        int res = 1;

        while (res <= A)
            res *= 10;

        memset(numgrp, 0, sizeof(numgrp));
        memset(grp, 0, sizeof(grp));

        for (int a = A; a <= B; ++a)
        {
            if (numgrp[a - A])
                continue;

            int x = a;
            ++g;

            do
            {
                x += (x % 10) * res;
                x /= 10;

                if (x >= A && x <=B)
                {
                    if (numgrp[x - A])
                        printf("oops\n");

                    numgrp[x - A] = g;
                    ++grp[g];
                }
            }
            while (x != a);            
        }

        int total = 0;

        for (int j = 1; j <= g; ++j)
        {
            total += grp[j] * (grp[j] - 1) / 2;
        }
       
        cout << "Case #" << i + 1 << ": " << total << endl;
    }

    return 0;
}
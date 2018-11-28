///////////////////////////////////////////////////////////////////////
/////    The code is written for Google Code Jam 2011 contest.    /////
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

#define PROBLEM_NAME "A"
#define LARGE_INPUT 1

#if LARGE_INPUT
    #define INPUT_FILE PROBLEM_NAME "-large.in"
    #define OUTPUT_FILE PROBLEM_NAME "-large.out"
#else
    #define INPUT_FILE PROBLEM_NAME "-small-attempt.in"
    #define OUTPUT_FILE PROBLEM_NAME "-small.out"
#endif

int main()
{
    freopen(INPUT_FILE,"r",stdin);
    freopen(OUTPUT_FILE,"w",stdout);

    int T;
    cin >> T;

    for (int i = 0; i < T; ++i)
    {
        int R, C;
        cin >> R >> C;
        vector< string > Pict(R);

        for (int j = 0; j < R; ++j)
        {
            cin >> Pict[j];
        }

        for (int j = 0; j < R - 1; ++j)
        {
            for (int k = 0; k < C - 1; ++k)
            {
                if (Pict[j][k] == '#' &&
                    Pict[j+1][k] == '#' &&
                    Pict[j+1][k+1] == '#' &&
                    Pict[j][k+1] == '#' )
                {
                    Pict[j][k] = '/';
                    Pict[j][k+1] = '\\';
                    Pict[j+1][k] = '\\';
                    Pict[j+1][k+1] = '/';
                }
            }
        }

        bool Possible = true;

        for (int j = 0; j < R; ++j)
        {
            for (int k = 0; k < C; ++k)
            {
                if (Pict[j][k] == '#')
                {
                    Possible = false;
                    break;
                }
            }
        }

        cout << "Case #" << i + 1 << ": "  << endl;

        if (Possible)
        {
            for (int j = 0; j < R; ++j)
                cout << Pict[j] << endl;
        }
        else
            cout << "Impossible" << endl;
    }

    return 0;
}
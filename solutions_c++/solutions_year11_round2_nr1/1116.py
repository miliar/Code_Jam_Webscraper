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

double GetWP(vector<char> const& v, int exc)
{
    int total = 0;
    int win = 0;

    for (size_t j = 0; j < v.size(); ++j)
    {
        if (j == exc)
            continue;

        if (v[j] != '.')
            ++total;

        if (v[j] == '1')
            ++win;
    }

    return (double)win / total;
}

double GetOWP(int i, vector<vector<char> > const& v)
{
    double OWP = 0;
    int total = 0;

    for (size_t j = 0; j < v.size(); ++j)
    {
        if (v[i][j] == '.')
            continue;

        ++total;
        OWP += GetWP(v[j], i);
    }

    return OWP / total;
}

double GetOOWP(int i, vector<vector<char> > const& v)
{
    double OOWP = 0;
    int total = 0;

    for (size_t j = 0; j < v.size(); ++j)
    {
        if (v[i][j] == '.')
            continue;

        ++total;

        OOWP += GetOWP(j, v);
    }

    return OOWP / total;
}

int main()
{
    freopen(INPUT_FILE,"r",stdin);
    freopen(OUTPUT_FILE,"w",stdout);

    int T;
    cin >> T;

    for (int i = 0; i < T; ++i)
    {
        int N;
        cin >> N;
        vector<vector<char> > vec(N, vector<char>(N));

        for (int j = 0; j < N; ++j)
        {
            for (int k = 0; k < N; ++k)
                cin >> vec[j][k];
        }
       
        cout << "Case #" << i + 1 <<":" << endl;

        for (int j = 0; j < N; ++j)
        {
            cout << setprecision(10) << 0.25 * GetWP(vec[j], j) + 0.5 * GetOWP(j, vec) + 0.25 * GetOOWP(j, vec) << endl;

        }
    }

    return 0;
}
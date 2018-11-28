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

#define PROBLEM_NAME "B"
#define LARGE_INPUT 0

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
        int L, N, C;
        unsigned __int64 t;
        cin >> L >> t >> N >> C;

        vector<int> a(C);
        int Total = 0;

        for (int j = 0; j < C; ++j)
        {
            cin >> a[j];
            a[j] *= 2;
            Total += a[j];
        }

        int Block = t / Total;
        int First = Block * a.size();
        unsigned __int64 T = Block * Total;

        for (int j = 0; j < a.size(); ++j)
        {
            if (T + a[j] > t)
                break;
            
            T += a[j];
            ++First;
        }

        unsigned __int64 TotalTime = 0;

        if (First < N)
        {
            TotalTime = t;

            map<unsigned __int64, int> Times;
            Times[a[First % a.size()] - (t-T)] = 1;
            TotalTime += (a[First % a.size()] - (t-T))/2;
            int TotalL = 1;

            for (int j = First + 1; j < N; ++j)
            {
                ++Times[a[j % a.size()]];
                ++TotalL;
                TotalTime += a[j % a.size()] / 2;
            }

            while (TotalL > L)
            {
                if (Times.begin()->second == 0)
                {
                    Times.erase(Times.begin());
                    continue;
                }
                
                --TotalL;
                --Times.begin()->second;
                TotalTime += Times.begin()->first / 2;
            }
        }
        else
        {
            for (int j = 0; j < N; ++j)
            {
                TotalTime += a[j % a.size()];
            }
        }
       
        cout << "Case #" << i + 1 << ": " << TotalTime << endl;
    }

    return 0;
}
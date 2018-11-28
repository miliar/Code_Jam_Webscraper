///////////////////////////////////////////////////////////////////////
/////    The code is written for Google Code Jam 2010 contest.    /////
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
    #define INPUT_FILE PROBLEM_NAME "-small-attempt0.in"
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
        int R, k, N, j;
        cin >> R >> k >> N;
        vector<int> Groups(N);

        for (j = 0; j < N; ++j)
            cin >> Groups[j];

        vector<pair<vector<int>, int>> Order;
        unsigned __int64 TotalSum = 0;

        for (int r = 0; r < R; ++r)
        {
            unsigned __int64 Sum = 0;
            int m = 0;

            for (m = 0; m < Order.size(); ++m)
            {
                if (Order[m].first == Groups)
                    break;
            }

            if (m < Order.size())
            {
                int Count = Order.size() - m;

                for (; m < Order.size(); ++m)
                {
                    Sum += Order[m].second;
                }

                int Last = (R - r) / Count;
                TotalSum += Last * Sum;
                r += Last * Count - 1;
                Order.clear();
                continue;
            }

            for (j = 0; j < N; ++j)
            {
                if (Sum + Groups[j] > k)
                    break;

                Sum += Groups[j];
            }

            if (!Sum)
                break;

            TotalSum += Sum;
            Order.push_back(make_pair(Groups, Sum));

            vector<int> Sub(Groups.begin(), Groups.begin() + j);
            Groups.erase(Groups.begin(), Groups.begin() + j);
            Groups.insert(Groups.end(), Sub.begin(), Sub.end());           

        }
        cout << "Case #" << i + 1 << ": " << TotalSum << endl;
    }

    return 0;
}
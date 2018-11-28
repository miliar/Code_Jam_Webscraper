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
        int C, D, N;
        cin >> C;
        map<string, char> CombineMap;

        for (int j = 0; j < C; ++j)
        {
            std::string Comb;
            cin >> Comb;
            CombineMap[Comb.substr(0, 2)] = Comb[2];
            CombineMap[Comb.substr(1, 1) += Comb[0]] = Comb[2];
        }

        cin >> D;

        vector<string> DenyVec;

        for (int j = 0; j < D; ++j)
        {
            string Deny;
            cin >> Deny;
            DenyVec.push_back(Deny);
        }

        cin >> N;
        string Input, Output;
        cin >> Input;
        map<char, int> CharMap;

        for (int j = 0; j < N; ++j)
        {
            char Cur = Input[j];

            if (!Output.empty())
            {
                size_t Pos = Output.size() - 1;
                map<string, char>::const_iterator I = CombineMap.find(Output.substr(Pos) += Cur);

                if (I != CombineMap.end())
                {
                    --CharMap[Output[Pos]];
                    Output.erase(Pos);
                    Cur = I->second;
                }
            }

            Output.push_back(Cur);
            ++CharMap[Cur];

            for (size_t k = 0; k < DenyVec.size(); ++k)
            {
                if (CharMap[DenyVec[k][0]] && CharMap[DenyVec[k][1]])
                {
                    Output.clear();
                    CharMap.clear();
                    break;
                }
            }
        }
       
        cout << "Case #" << i + 1 << ": [";
        
        if (!Output.empty())
            cout << Output[0];

        for (size_t j = 1; j < Output.size(); ++j)
        {
            cout << ", " << Output[j];
        }

        cout << "]" << endl;

    }

    return 0;
}
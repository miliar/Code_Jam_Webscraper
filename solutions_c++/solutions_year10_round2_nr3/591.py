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
#define LARGE_INPUT 0

#if LARGE_INPUT
    #define INPUT_FILE PROBLEM_NAME "-large.in"
    #define OUTPUT_FILE PROBLEM_NAME "-large.out"
#else
    #define INPUT_FILE PROBLEM_NAME "-small-attempt0.in"
    #define OUTPUT_FILE PROBLEM_NAME "-small.out"
#endif


vector<vector<int>> PartSet(501, vector<int>(501, -1));
int modular = 100003;

int Fact(int n)
{
    int res = 1;

    for (int i = 1; i <= n; ++i)
        res *= i;

    return res;
}

int GetCnk(int n, int k)
{
    if (k < 0 || n < k)
        return 0;

    if (n == k)
        return 1;

    if (k == 1)
        return n;

    if (n < 13)
        return (Fact(n) / Fact(n-k) / Fact(k)) % modular;

    return (GetCnk(n - 1, k - 1) + GetCnk(n-1, k)) % modular;
}

int GetVariants(int n, int l)
{
    if (PartSet[n][l] >= 0)
        return PartSet[n][l];

    if (l == 1)
        return 1;

    int Sum = 0;

    for (int i = 1; i < l; ++i)
    {
        Sum += GetVariants(l, i) * GetCnk(n - l - 1, l - i - 1);
        Sum %= modular;
    }

    return PartSet[n][l] = Sum;
}

int main()
{
    freopen(INPUT_FILE,"r",stdin);
    freopen(OUTPUT_FILE,"w",stdout);

    int T;
    cin >> T;

    for (int i = 0; i < T; ++i)
    {
        int n;
        cin >> n;
        int Sum = 0;

        for (int j = 1; j < n; ++j)
        {
            Sum += GetVariants(n, j);
            Sum %= modular;
        }
       
        cout << "Case #" << i + 1 << ": " << Sum << endl;
    }

    return 0;
}
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

#define PROBLEM_NAME "A"
#define LARGE_INPUT 0

#if LARGE_INPUT
    #define INPUT_FILE PROBLEM_NAME "-large.in"
    #define OUTPUT_FILE PROBLEM_NAME "-large.out"
#else
    #define INPUT_FILE PROBLEM_NAME "-small-attempt0.in"
    #define OUTPUT_FILE PROBLEM_NAME "-small.out"
#endif

char charmap[256];

void learn()
{
    char input[]  = "q a zoo ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv";
    char output[] = "z y qee our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up";

    for (size_t i = 0; i != _countof(input); ++i)
        charmap[input[i]] = output[i];
}

int main()
{
    freopen(INPUT_FILE,"r",stdin);
    freopen(OUTPUT_FILE,"w",stdout);

    learn();

    int T;
    cin >> T;
    cin.ignore();

    for (int i = 0; i < T; ++i)
    {
        string str;
        getline(cin, str);

        for (string::iterator I = str.begin(); I != str.end(); ++I)
            *I = charmap[*I];
       
        cout << "Case #" << i + 1 << ": " << str << endl;
    }

    return 0;
}
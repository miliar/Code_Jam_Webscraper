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

#define PROBLEM_NAME "A"
#define LARGE_INPUT 1

#if LARGE_INPUT
    #define INPUT_FILE PROBLEM_NAME "-large.in"
    #define OUTPUT_FILE PROBLEM_NAME "-large.out"
#else
    #define INPUT_FILE PROBLEM_NAME "-small-attempt0.in"
    #define OUTPUT_FILE PROBLEM_NAME "-small.out"
#endif

struct Directory
{
    static int mkdir;
    map<string, Directory> Subdirs;

    void Parse(string const& Path)
    {
        if (Path.empty())
            return;

        string::const_iterator I = find(Path.begin() + 1, Path.end(), '/');
        string Dir(Path.begin() + 1, I);
        pair<map<string, Directory>::iterator, bool> Res = Subdirs.insert(make_pair(Dir, Directory()));
        
        if (Res.second)
            ++mkdir;

        Res.first->second.Parse(string(I, Path.end()));
    }
};

int Directory::mkdir = 0;

int main()
{
    freopen(INPUT_FILE,"r",stdin);
    freopen(OUTPUT_FILE,"w",stdout);

    int T;
    cin >> T;

    for (int i = 0; i < T; ++i)
    {
        int N, M;
        cin >> N >> M;
        Directory Root;

        for (int j = 0; j < N; ++j)
        {
            string Path;
            cin >> Path;
            Root.Parse(Path);
        }

        Root.mkdir = 0;

        for (int j = 0; j < M; ++j)
        {
            string Path;
            cin >> Path;
            Root.Parse(Path);
        }
       
        cout << "Case #" << i + 1 << ": " << Root.mkdir << endl;
    }

    return 0;
}
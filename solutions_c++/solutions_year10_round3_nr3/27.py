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
    #define INPUT_FILE PROBLEM_NAME "-small-attempt.in"
    #define OUTPUT_FILE PROBLEM_NAME "-small.out"
#endif

class Board
{
    vector<vector<int>> Brd;
    int M, N;

public:
    Board(int M, int N) :
      M(M),
      N(N),
      Brd(M, vector<int>(N))
    {
        for (int j = 0; j < M; ++j)
        {
            for (int k = 0; k < N / 4; ++k)
            {
                char c;
                cin >> c;
                c = (c >= '0' && c <= '9' ? c - '0' : c - 'A' + 10);
                Brd[j][k * 4 + 3] = c & 1;
                c >>= 1;
                Brd[j][k * 4 + 2] = c & 1;
                c >>= 1;
                Brd[j][k * 4 + 1] = c & 1;
                c >>= 1;
                Brd[j][k * 4] = c & 1;
            }
        }
    }

    bool CheckChess(int x, int y, int s)
    {
        if (y + s > M || x + s > N || Brd[y][x] == -1)
            return false;

        int StartCol = Brd[y][x];

        for (int i = y; i < y + s; ++i)
        {
            int StartCol1 = StartCol;

            for (int j = x; j < x + s; ++j)
            {
                if (StartCol1 != Brd[i][j])
                    return false;

                StartCol1 = !StartCol1;
            }

            StartCol = !StartCol;
        }

        for (int i = y; i < y + s; ++i)
            for (int j = x; j < x + s; ++j)
                Brd[i][j] = -1;

        return true;
    }
};

int main()
{
    freopen(INPUT_FILE,"r",stdin);
    freopen(OUTPUT_FILE,"w",stdout);

    int T;
    cin >> T;

    for (int i = 0; i < T; ++i)
    {
        int M, N;
        cin >> M >> N;
        Board board(M, N);
        map<int, int> Sol;

        for (int s = min(M, N); s > 0; --s)
        {
            for (int y = 0; y < M; ++y)
            {
                for (int x = 0; x < N; ++x)
                {
                    if (board.CheckChess(x, y, s))
                        ++Sol[s];
                }
            }
        }

        cout << "Case #" << i + 1 << ": " << Sol.size() << endl;

        for (map<int, int>::reverse_iterator I = Sol.rbegin(); I != Sol.rend(); ++I)
        {
            cout << I->first << ' ' << I->second << endl;
        }
    }

    return 0;
}
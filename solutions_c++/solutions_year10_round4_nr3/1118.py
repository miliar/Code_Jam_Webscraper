/***
 * Code written by zyx (Carlos Guia) for the Google Code Jam 2010
 * Environment used: Microsoft Visual C++ 2008 under Windows XP
 *
 * This code is much more complex than needed to solve the problem, defines, typedefs, consts and a
 * framework to back source and data files make it look very ofuscated. However, it has been completely
 * sectioned, as an example section foo would look something like this
//////////////////////// foo //////////////////////
... foo specific stuff ...
//////////////////////// foo //////////////////////
 * And as an attempt to help readers understand the solution, here is a quick description of the sections
 * found in the file in order:
 * - Debug Utilities: some funtions to debug the code without affecting the output.
 * - Reading Utilities: many macro definitions with the most common thins that need to be readed.
 * - Zyx GCJ Framework Utilities: funtions to use the correct files, keep track of time and back up files.
 * - Basic Utilities: macros, typedefs and consts that are commonly used.
 * - Solution: the main method with the logic used to solve this particular problem.
 *
 * What is used for input/output is based on this rules:
 *   if ZYX_MACHINE is defined, then xxx.in is used as input and ouput is selected as:
 *     if _DEBUG is defined, then standard output is used.
 *     else xxx.out is used for output.
 *   else standard input/output are used.
 *
 * The code is expected to work under MS VC++ 2005 or later and most gcc versions, without the ZYX_MACHINE
 * define using standard input/output. Unfortunately, only the non-GCJ prewritten code has been tested with
 * gcc at TopCoder and/or SPOJ. So if absolutely needed, this is how you can exactly reproduce my environment:
 *   - Use MS VC++ 2008 Express Edition under Windows XP
 *   - Create a Win32 console project with 2 files: this cpp file and a file called xxx.in
 *   - Add to the preprocesor definitions: ZYX_MACHINE
 *   - Put the input data in file xxx.in
 *   - Run the project in release mode.
 *   - Find the directory attempt.XXX with maximum XXX value under the project directory,
 *     inside that directory is a file called xxx.out with the generated output.
 *
 * WARNING: If ZYX_MACHINE is defined and _DEBUG is not defined, then the code assumes Windows as operating system
 *          and will try to create a directory called attempt.XXX and copy source and input/output files to it.
 ***/
#ifdef _MSC_VER
#pragma warning(disable:4996)  // deprecations
#endif  //  #ifdef _MSC_VER
#include <functional>
#include <algorithm>
#include <iostream>
#include <numeric>
#include <utility>
#include <sstream>
#include <complex>
#include <limits>
#include <string>
#include <bitset>
#include <vector>
#include <queue>
#include <stack>
#include <list>
#include <map>
#include <set>
#include <stdlib.h>
#include <assert.h>
#include <stdarg.h>
#include <string.h>
#include <ctype.h>
#include <stdio.h>
#include <float.h>
#include <math.h>
#include <time.h>
namespace std { long long abs(long long x) { return x < 0 ? -x : x; } }
using namespace std;

////////////////////// Debug Utilities ///////////////////////
void dprintf(char* format, ...) {
  fprintf(stderr, "DEBUG: ");
  va_list argp; va_start(argp, format);
  vfprintf(stderr, format, argp); va_end(argp);
  fprintf(stderr, "\n");
}
struct Exception {
  const char* message;
  const int line;
  Exception(const char* m, int l) : message(m), line(l) {}
};
#define THROW(M) throw Exception(M, __LINE__)
////////////////////// Debug Utilities ///////////////////////

////////////////////// Reading Utilities ///////////////////////
static char stringReader[2097152];
static inline bool ReadLine() {
  char* ptr = fgets(stringReader, sizeof(stringReader), stdin);
  if ( ptr == 0 ) return false;
  int N = strlen(stringReader);
  if ( stringReader[N - 1] == '\n' ) stringReader[N - 1] = 0;
  return true;
}
#define InLine(X) string X; ReadLine(); X = stringReader
#define InString1(X) string X; scanf("%s", stringReader); X = stringReader
#define InString2(X, Y) string X, Y; scanf("%s", stringReader); X = stringReader; scanf("%s", stringReader); Y = stringReader
#define InString3(X, Y, Z) string X, Y, Z; scanf("%s", stringReader); X = stringReader; scanf("%s", stringReader); Y = stringReader; scanf("%s", stringReader); Z = stringReader
#define InString4(X, Y, Z) string X, Y, Z, W; scanf("%s", stringReader); X = stringReader; scanf("%s", stringReader); Y = stringReader; scanf("%s", stringReader); Z = stringReader; scanf("%s", stringReader); W = stringReader
#define InDouble1(X) double X; scanf("%lf", &X)
#define InDouble2(X, Y) double X, Y; scanf("%lf%lf", &X, &Y)
#define InDouble3(X, Y, Z) double X, Y, Z; scanf("%lf%lf%lf", &X, &Y, &Z)
#define InDouble4(X, Y, Z, W) double X, Y, Z, W; scanf("%lf%lf%lf%lf", &X, &Y, &Z, &W)
#define InI641(X) i64 X; scanf("%lld", &X)
#define InI642(X, Y) i64 X, Y; scanf("%lld%lld", &X, &Y)
#define InI643(X, Y, Z) i64 X, Y, Z; scanf("%lld%lld%lld", &X, &Y, &Z)
#define InI644(X, Y, Z, W) i64 X, Y, Z, W; scanf("%lld%lld%lld%lld", &X, &Y, &Z, &W)
#define InInt1(X) int X; scanf("%d", &X)
#define InInt2(X, Y) int X, Y; scanf("%d%d", &X, &Y)
#define InInt3(X, Y, Z) int X, Y, Z; scanf("%d%d%d", &X, &Y, &Z)
#define InInt4(X, Y, Z, W) int X, Y, Z, W; scanf("%d%d%d%d", &X, &Y, &Z, &W)
#define InGlobalLine(X) ReadLine(); X = stringReader
#define InGlobalString1(X) scanf("%s", stringReader); X = stringReader
#define InGlobalString2(X, Y) scanf("%s", stringReader); X = stringReader; scanf("%s", stringReader); Y = stringReader
#define InGlobalString3(X, Y, Z) scanf("%s", stringReader); X = stringReader; scanf("%s", stringReader); Y = stringReader; scanf("%s", stringReader); Z = stringReader
#define InGlobalString4(X, Y, Z, W) scanf("%s", stringReader); X = stringReader; scanf("%s", stringReader); Y = stringReader; scanf("%s", stringReader); Z = stringReader; scanf("%s", stringReader); W = stringReader
#define InGlobalDouble1(X) scanf("%lf", &X)
#define InGlobalDouble2(X, Y) scanf("%lf%lf", &X, &Y)
#define InGlobalDouble3(X, Y, Z) scanf("%lf%lf%lf", &X, &Y, &Z)
#define InGlobalDouble4(X, Y, Z, W) scanf("%lf%lf%lf%lf", &X, &Y, &Z, &W)
#define InGlobalI641(X) scanf("%lld", &X)
#define InGlobalI642(X, Y) scanf("%lld%lld", &X, &Y)
#define InGlobalI643(X, Y, Z) scanf("%lld%lld%lld", &X, &Y, &Z)
#define InGlobalI644(X, Y, Z, W) scanf("%lld%lld%lld%lld", &X, &Y, &Z, &W)
#define InGlobalInt1(X) scanf("%d", &X)
#define InGlobalInt2(X, Y) scanf("%d%d", &X, &Y)
#define InGlobalInt3(X, Y, Z) scanf("%d%d%d", &X, &Y, &Z)
#define InGlobalInt4(X, Y, Z, W) scanf("%d%d%d%d", &X, &Y, &Z, &W)
#define InVectorLine(X, N) vector<string> X(N); for ( int i_##X = 0; i_##X < N; ++i_##X ) ReadLine(), X[i_##X] = stringReader;
#define InVectorString(X, N) vector<string> X(N); for ( int i_##X = 0; i_##X < N; ++i_##X ) scanf("%s", stringReader), X[i_##X] = stringReader
#define InVectorDouble(X, N) vector<double> X(N); for ( int i_##X = 0; i_##X < N; ++i_##X ) scanf("%lf", &X[i_##X])
#define InVectorI64(X, N) vector<i64> X(N); for ( int i_##X = 0; i_##X < N; ++i_##X ) scanf("%lld", &X[i_##X])
#define InVectorInt(X, N) vector<int> X(N); for ( int i_##X = 0; i_##X < N; ++i_##X ) scanf("%d", &X[i_##X])
#define InVectorGlobalLine(X, N) X.assign(N, ""); for ( int i_##X = 0; i_##X < N; ++i_##X ) ReadLine(), X[i_##X] = stringReader;
#define InVectorGlobalString(X, N) X.assign(N, ""); for ( int i_##X = 0; i_##X < N; ++i_##X ) scanf("%s", stringReader), X[i_##X] = stringReader
#define InVectorGlobalDouble(X, N) X.assign(N, 0); for ( int i_##X = 0; i_##X < N; ++i_##X ) scanf("%lf", &X[i_##X])
#define InVectorGlobalI64(X, N) X.assign(N, 0); for ( int i_##X = 0; i_##X < N; ++i_##X ) scanf("%lld", &X[i_##X])
#define InVectorGlobalInt(X, N) X.assign(N, 0); for ( int i_##X = 0; i_##X < N; ++i_##X ) scanf("%d", &X[i_##X])
#define InArrayLine(X, N, MAX_N) string X[MAX_N]; for ( int i_##X = 0; i_##X < N; ++i_##X ) ReadLine(), X[i_##X] = stringReader;
#define InArrayString(X, N, MAX_N) string X[MAX_N]; for ( int i_##X = 0; i_##X < N; ++i_##X ) scanf("%s", stringReader), X[i_##X] = stringReader
#define InArrayDouble(X, N, MAX_N) double X[MAX_N]; for ( int i_##X = 0; i_##X < N; ++i_##X ) scanf("%lf", &X[i_##X])
#define InArrayI64(X, N, MAX_N) i64 X[MAX_N]; for ( int i_##X = 0; i_##X < N; ++i_##X ) scanf("%lld", &X[i_##X])
#define InArrayInt(X, N, MAX_N) int X[MAX_N]; for ( int i_##X = 0; i_##X < N; ++i_##X ) scanf("%d", &X[i_##X])
#define InArrayLineGlobal(X, N) for ( int i_##X = 0; i_##X < N; ++i_##X ) ReadLine(), X[i_##X] = stringReader;
#define InArrayStringGlobal(X, N) for ( int i_##X = 0; i_##X < N; ++i_##X ) scanf("%s", stringReader), X[i_##X] = stringReader
#define InArrayDoubleGlobal(X, N) for ( int i_##X = 0; i_##X < N; ++i_##X ) scanf("%lf", &X[i_##X])
#define InArrayI64Global(X, N) for ( int i_##X = 0; i_##X < N; ++i_##X ) scanf("%lld", &X[i_##X])
#define InArrayIntGlobal(X, N) for ( int i_##X = 0; i_##X < N; ++i_##X ) scanf("%d", &X[i_##X])
#define WhileTests() int TOTAL_TEST_CASES; ReadLine(); sscanf(stringReader, "%d", &TOTAL_TEST_CASES); for ( int current_test_case = 1; current_test_case <= TOTAL_TEST_CASES; ++current_test_case )
#define WhileInString(X) int current_test_case = 1; for ( string X; scanf("%s", &X) == 1 && (X != ""); ++current_test_case )
#define WhileInI641(X) int current_test_case = 1; for ( i64 X; scanf("%lld", &X) == 1 && (X); ++current_test_case )
#define WhileInI642(X, Y) int current_test_case = 1; for ( i64 X, Y, current_test_case = 1; scanf("%lld%lld", &X, &Y) == 2 && (X|Y); ++current_test_case )
#define WhileInI643(X, Y, Z) int current_test_case = 1; for ( i64 X, Y, Z, current_test_case = 1; scanf("%lld%lld%lld", &X, &Y, &Z) == 3 && (X|Y|Z); ++current_test_case )
#define WhileInInt1(X) for ( int X, current_test_case = 1; scanf("%d", &X) == 1 && (X); ++current_test_case )
#define WhileInInt2(X, Y) for ( int X, Y, current_test_case = 1; scanf("%d%d", &X, &Y) == 2 && (X|Y); ++current_test_case )
#define WhileInInt3(X, Y, Z) for ( int X, Y, Z, current_test_case = 1; scanf("%d%d%d", &X, &Y, &Z) == 3 && (X|Y|Z); ++current_test_case )
#define WhileInGlobalI641(X) for ( int current_test_case = 1; scanf("%lld", &X) == 1 && (X); ++current_test_case )
#define WhileInGlobalI642(X, Y) for ( int current_test_case = 1; scanf("%lld%lld", &X, &Y) == 2 && (X|Y); ++current_test_case )
#define WhileInGlobalI643(X, Y, Z) for ( int current_test_case = 1; scanf("%lld%lld%lld", &X, &Y, &Z) == 3 && (X|Y|Z); ++current_test_case )
#define WhileInGlobalInt1(X) for ( int current_test_case = 1; scanf("%d", &X) == 1 && (X); ++current_test_case )
#define WhileInGlobalInt2(X, Y) for ( int current_test_case = 1; scanf("%d%d", &X, &Y) == 2 && (X|Y); ++current_test_case )
#define WhileInGlobalInt3(X, Y, Z) for ( int current_test_case = 1; scanf("%d%d%d", &X, &Y, &Z) == 3 && (X|Y|Z); ++current_test_case )
#define WhileInStringEOF(X) int current_test_case = 1; for ( string X; scanf("%s", &X) == 1; ++current_test_case )
#define WhileInI641EOF(X) int current_test_case = 1; for ( i64 X; scanf("%lld", &X) == 1; ++current_test_case )
#define WhileInI642EOF(X, Y) int current_test_case = 1; for ( i64 X, Y, current_test_case = 1; scanf("%lld%lld", &X, &Y) == 2; ++current_test_case )
#define WhileInI643EOF(X, Y, Z) int current_test_case = 1; for ( i64 X, Y, Z, current_test_case = 1; scanf("%lld%lld%lld", &X, &Y, &Z) == 3; ++current_test_case )
#define WhileInInt1EOF(X) for ( int X, current_test_case = 1; scanf("%d", &X) == 1; ++current_test_case )
#define WhileInInt2EOF(X, Y) for ( int X, Y, current_test_case = 1; scanf("%d%d", &X, &Y) == 2; ++current_test_case )
#define WhileInInt3EOF(X, Y, Z) for ( int X, Y, Z, current_test_case = 1; scanf("%d%d%d", &X, &Y, &Z) == 3; ++current_test_case )
#define WhileInGlobalI641EOF(X) for ( int current_test_case = 1; scanf("%lld", &X) == 1; ++current_test_case )
#define WhileInGlobalI642EOF(X, Y) for ( int current_test_case = 1; scanf("%lld%lld", &X, &Y) == 2; ++current_test_case )
#define WhileInGlobalI643EOF(X, Y, Z) for ( int current_test_case = 1; scanf("%lld%lld%lld", &X, &Y, &Z) == 3; ++current_test_case )
#define WhileInGlobalInt1EOF(X) for ( int current_test_case = 1; scanf("%d", &X) == 1; ++current_test_case )
#define WhileInGlobalInt2EOF(X, Y) for ( int current_test_case = 1; scanf("%d%d", &X, &Y) == 2; ++current_test_case )
#define WhileInGlobalInt3EOF(X, Y, Z) for ( int current_test_case = 1; scanf("%d%d%d", &X, &Y, &Z) == 3; ++current_test_case )
////////////////////// Reading Utilities ///////////////////////

////////////////// Zyx GCJ Framework Utilities ///////////////////
void ZyxGCJ_OpenFiles() {
#ifdef ZYX_MACHINE
  freopen("xxx.in", "rt", stdin);
#ifndef _DEBUG
  freopen("xxx.out", "wt", stdout);
#endif  //  #ifndef _DEBUG
#endif  //  #ifdef ZYX_MACHINE
}
void ZyxGCJ_EstimateTime(clock_t start, int current_test_case, int TOTAL_TEST_CASES) {
#ifdef ZYX_MACHINE
#ifndef _DEBUG
  double p = double(current_test_case)/TOTAL_TEST_CASES;
  clock_t now = clock();
  dprintf("Computing case: %d/%d (%.2f%%)", current_test_case, TOTAL_TEST_CASES, 100 * p);
  dprintf("Times: %.4f (%.4f)", double(now - start) / CLOCKS_PER_SEC / 60,
    (now - start) / (p * CLOCKS_PER_SEC) / 60);
#endif  //  #ifndef _DEBUG
#endif  //  #ifdef ZYX_MACHINE
}
void ZyxGCJ_BackUpFiles() {
  fclose(stdin);
  fclose(stdout);
#ifdef ZYX_MACHINE
#ifndef _DEBUG
  for ( int i = 0; ; ++i ) {
    sprintf(stringReader, "attempt.%03d\\", i);
    FILE* file = fopen((string(stringReader) + "xxx.in").c_str(), "rt");
    if ( file ) fclose(file);
    else {
      dprintf("Storing at %s\n", stringReader);
      system((string("md ") + stringReader).c_str());
      system((string("copy xxx.in ") + stringReader).c_str());
      system((string("copy xxx.out ") + stringReader).c_str());
      system((string("copy source.cpp ") + stringReader).c_str());
      break;
    }
  }
#endif  //  #ifndef _DEBUG
#endif  //  #ifdef ZYX_MACHINE
}
// BEGIN CUT HERE
//Znippet tag
// END CUT HERE
////////////////// Zyx GCJ Framework Utilities ///////////////////

///////////////////////// Basic Utilities //////////////////////////
#define SIZE(N, V) int N = static_cast<int>((V).size())
#define GSIZE(N, V) (N) = static_cast<int>((V).size())
#define ALL(V) (V).begin(), (V).end()
#define UNIQUE(C) {sort(ALL(C)); C.resize(unique(ALL(C)) - C.begin());}
#define CAST(X, Y) {stringstream ss; ss << (X); ss >> (Y);}
typedef long long i64;
const i64 ooLL = 0x3f3f3f3f3f3f3f3fLL;
const int oo = 0x3f3f3f3f;
const double eps = 1e-9;
///////////////////////// Basic Utilities //////////////////////////

////////////////////////// Solution ///////////////////////////
int main() {
try {
  ZyxGCJ_OpenFiles();
  clock_t start = clock();
  WhileTests() {
    ZyxGCJ_EstimateTime(start, current_test_case, TOTAL_TEST_CASES);
    printf("Case #%d: ", current_test_case);
    bool grid[2][110][110];
    memset(grid, false, sizeof(grid));
    InInt1(R);
    int alive = 0;
    int lowX = oo, highX = 0, lowY = oo, highY = 0;
    for ( int i = 0; i < R; ++i ) {
      InInt4(x1, y1, x2, y2);
      lowX = min(lowX, x1);
      highX = max(highX, x2);
      lowY = min(lowY, y1);
      highY = max(highY, y2);
      for ( int x = x1; x <= x2; ++x ) for ( int y = y1; y <= y2; ++y ) if ( grid[0][x][y] == 0 ) {
        ++alive;
        grid[0][x][y] = true;
      }
    }
    int sol = 0;
    int current = 0;
    while ( alive ) {
      ++sol;
      int old = current;
      current = 1 - old;
      for ( int x = lowX; x <= highX; ++x ) for ( int y = lowY; y <= highY; ++y ) {
        if ( grid[old][x][y] ) {
          if ( !grid[old][x - 1][y] && !grid[old][x][y - 1] ) {
            grid[current][x][y] = false;
            --alive;
          }
          else
            grid[current][x][y] = true;
        } else {
          if ( grid[old][x - 1][y] && grid[old][x][y - 1] ) {
            grid[current][x][y] = true;
            ++alive;
          }
          else
            grid[current][x][y] = false;
        }
      }
    }
    printf("%d\n", sol);
  }
  ZyxGCJ_BackUpFiles();
  return 0;
} catch ( const Exception& exception ) {
  fprintf(stderr, "******************************\n");
  fprintf(stderr, "ERROR.%d: %s\n", exception.line, exception.message);
  fprintf(stderr, "******************************\n");
  throw exception;
}
}
////////////////////////// Solution ///////////////////////////
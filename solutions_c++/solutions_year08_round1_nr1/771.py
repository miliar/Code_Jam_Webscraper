/* ******************************************************************* */
/* Google Code Jam 2008                                                */
/*                                                                     */
/* This program should compile fine under Windows and Linux systems.   */
/* Boost library (www.boost.org) is needed to compile.                 */
/*                                                                     */
/* => Compiling and running under Linux:                               */
/* $ g++ X.cpp -O2 -Wall -o X                                          */
/* $ ./X < data.in > data.out                                          */
/*                                                                     */
/* => Compiling and running under Windows:                             */
/* > g++.exe X.cpp -O2 -Wall -o X.exe -DFILE_INPUT                     */
/* > X.exe data.in > data.out                                          */
/*                                                                     */
/* Coded by edub4rt. <bart_barthel@hotmail.com>                        */
/* ******************************************************************* */

#include <iostream>
#include <sstream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <list>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <cassert>
#include <cmath>
#include <ctime>
#include <boost/lexical_cast.hpp>
#include <boost/utility.hpp>
#include <boost/foreach.hpp>
#include <boost/format.hpp>
#include <boost/algorithm/string.hpp>
#include <boost/tuple/tuple.hpp>
#include <boost/tuple/tuple_comparison.hpp>

using namespace std;
using namespace boost;

typedef uint64_t uint64;
typedef uint32_t uint32;
typedef uint16_t uint16;
typedef uint8_t uint8;
typedef int64_t int64;
typedef int32_t int32;
typedef int16_t int16;
typedef int8_t int8;
typedef uint8 byte;
typedef unsigned char uchar;
typedef unsigned short ushort;
typedef unsigned int uint;
typedef unsigned long ulong;
typedef float real32;
typedef double real64;
typedef long double real128;
typedef real32 real;

typedef vector<int> IntVec;
typedef vector<string> StringVec;

#define ALL(x) (x).begin(),(x).end()
#define rep(x) for(uint32_t _in##__LINE_=0;_in##__LINE_<x;_in##__LINE_++)
#define forcount(x,y) for(uint32_t _ic##__LINE__=0;_ic##__LINE__<y;_ic##__LINE__++)for(bool _forcount_continue##__LINE__=true;_forcount_continue##__LINE__==true;_forcount_continue##__LINE__?(_ic##__LINE__=y,_forcount_continue##__LINE__=false):(_forcount_continue##__LINE__=false))for(x=_ic##__LINE__;_forcount_continue##__LINE__==true;_forcount_continue##__LINE__=false)
#define foriter(x,y) for(typeof(y.begin()) _ii##__LINE__=y.begin();_ii##__LINE__!=y.end();_ii##__LINE__++)for(bool _foriter_continue##__LINE__=true;_foriter_continue##__LINE__==true;_foriter_continue##__LINE__==true?(_ii##__LINE__=y.end(),_foriter_continue##__LINE__=false):(_foriter_continue##__LINE__=false))for(x=_ii##__LINE__;_foriter_continue##__LINE__==true;_foriter_continue##__LINE__=false)
#define forever() while(true)
#define foreach BOOST_FOREACH
#define sqr(x) ((x)*(x))
#define INF 1e17
#define PI  acos(-1.)
#define EPS 1e-7
#define X first
#define Y second

#ifdef FILE_INPUT
#define cin fin
#endif

int main(int argc, char *argv[])
{
#ifdef FILE_INPUT
    if(argc < 2)
        return 0;
    ifstream fin(argv[1]);
#endif

    uint32 numCases;
    cin >> numCases;

    forcount(uint32 curCase, numCases)
    {
        int n, tmp, resp = 0;

        cin >> n;

        IntVec v1(n);
        IntVec v2(n);

        forcount(int i, n) {
            cin >> tmp;
            v1[i] = tmp;
        }

        forcount(int i, n) {
            cin >> tmp;
            v2[i] = tmp;
        }

        sort(ALL(v1));
        sort(ALL(v2));
        reverse(ALL(v2));

        forcount(int i, n) {
            resp += v1[i]*v2[i];
        }
        cout << "Case #" << (curCase+1) << ": " << resp << endl;
    }

    return 0;
}

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

#ifdef FILE_INPUT
#define cin fin
#endif

typedef pair<uint64,uint64> Point;
typedef vector<Point> PointList;

uint64 x[1 << 16];
uint64 y[1 << 16];

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
        PointList pList;
        int64 n, A, B, C, D, x0, y0, M, ans = 0;
        cin >> n >> A >> B >> C >> D >> x0 >> y0 >> M;

        x[0] = x0;
        y[0] = y0;
        for(int i=1;i<n;i++) {
            x[i] = (A*x[i-1] + B) % M;
            y[i] = (C*y[i-1] + D) % M;
        }

        for(int a=0;a<n;a++) {
            for(int b=0;b<n;b++) {
                if(b!=a) {
                for(int c=0;c<n;c++) {
                    if(c!=a && c!=b) {
                        if((x[a] + x[b] + x[c]) % 3 == 0 && (y[a] + y[b] + y[c]) % 3 == 0) {
                            ans++;
                        }
                    }
                }
                }
            }
        }
        cout << "Case #" << (curCase+1) << ": " << ans/6 << endl;
    }

    return 0;
}

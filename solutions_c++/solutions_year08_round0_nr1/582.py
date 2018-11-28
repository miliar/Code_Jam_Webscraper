/* ******************************************************************* */
/* Google Code Jam 2008                                                */
/*                                                                     */
/* This program should compile fine under Windows and Linux systems.   */
/* But it's needs the boost library (www.boost.org).                   */
/*                                                                     */
/* => Compiling and running under Linux:                               */
/* $ g++ problem.cpp -o problem                                        */
/* $ ./problem < data.in > data.out                                    */
/*                                                                     */
/* => Compiling and running under Windows:                             */
/* > g++.exe problem.cpp -o problem.exe -DFILE_INPUT                   */
/* > problem.exe data.in > data.out                                    */
/*                                                                     */
/* Coded by edub4rt.                                                   */
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
#include <stack>
#include <complex>
#include <cstdio>
#include <cassert>
#include <cmath>
#include <boost/algorithm/string.hpp>
#include <boost/foreach.hpp>

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

#define len() length()
#define vall(x) (x).begin(),(x).end()
#define vsort(x) sort(vall(x))
#define vreverse(x) reverse(vall(x))
#define vclear(x,c) memset(x,c,sizeof(x))
#define foreach BOOST_FOREACH
#define forcount(VAR,NUM) for(uint32 _ic=0;_ic<NUM;_ic++)for(bool _forcount_continue=true;_forcount_continue==true;)for(VAR=_ic;_forcount_continue==true; _forcount_continue=false)
#define forever() while(true)

#ifdef FILE_INPUT
    #define din fin
#else
    #define din cin
#endif
#define dout cout

template<class T> string int2str(T x) { ostringstream o; o << x; return o.str(); }
int str2int(string s) { istringstream i(s); int x; i>>x; return x; }
typedef vector<int> intVec;
typedef vector<string> strVec;

vector<string> queryList;
vector<string> engineList;

uint32_t getBestEngine(vector<string>::iterator start)
{
    int *maxQuerys = new int[queryList.size()];

    forcount(uint32_t curengine, engineList.size()) {
        maxQuerys[curengine] = 0;

        for(vector<string>::iterator it = start; it != queryList.end(); it++)
        {
            if(engineList[curengine] == (*it))
                break;
            maxQuerys[curengine]++;
        }
    }

    uint32_t bestEngine = 0;
    forcount(uint32_t curengine, engineList.size()) {
        if(maxQuerys[curengine] > maxQuerys[bestEngine])
            bestEngine = curengine;
    }

    delete maxQuerys;

    return bestEngine;
}

int main(int argc, char *argv[])
{
#ifdef FILE_INPUT
    if(argc < 2)
        return 0;
    ifstream fin(argv[1]);
#endif
    char temp[256];

    uint32 numcases;
    din >> numcases;

    for(uint32 casee = 1; casee <= numcases; casee++) {
        uint32_t numengines;
        din >> numengines;

        engineList.clear();
        din.getline(temp,256);
        forcount(uint32_t engine, numengines) {
            din.getline(temp,256);
            engineList.push_back(temp);
        }

        uint32_t numquerys;
        din >> numquerys;

        queryList.clear();
        din.getline(temp,256);
        forcount(uint32_t query, numquerys) {
            din.getline(temp,256);
            queryList.push_back(temp);
        }

        uint32_t switches = 0, curengine = 0;

        curengine = getBestEngine(queryList.begin());
        for(vector<string>::iterator it = queryList.begin(); it != queryList.end(); it++)
        {
            if(engineList[curengine] == (*it)) {
                curengine = getBestEngine(it);
                switches++;
            }
        }

        dout << "Case #" << casee << ": " << switches << endl;
    }
    return 0;
}

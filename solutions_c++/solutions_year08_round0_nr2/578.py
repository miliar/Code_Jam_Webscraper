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
#define fornum(x) for(uint32_t _in=0;_in<x;_in++)
#define forever() while(true)

#ifdef FILE_INPUT
    #define din fin
#else
    #define din cin
#endif
#define dout cout

template<class T> string int2str(T x) { ostringstream o; o << x; return o.str(); }
int str2int(string s) { istringstream i(s); int x; i>>x; return x; }

struct TimeLine
{
    TimeLine() : start(0), end(0), line(3) { }
    TimeLine(uint32_t _start, uint32_t _end, uint8_t _line) : start(_start), end(_end), line(_line) { }
    uint32_t start;
    uint32_t end;
    uint8_t line;
};

#define ATOB 1
#define BTOA 2

typedef vector<TimeLine> TimeList;
TimeList timeList;
uint32_t turnaround_time, na, nb;
bool found;

uint32_t convertTime(string stime)
{
    struct tm tim;
    strptime(stime.c_str(),"%H:%M",&tim);
    uint32_t time = tim.tm_hour*3600 + tim.tm_min*60;
    return time;
}

TimeLine getFirstTimeLine()
{
    TimeLine first = (*timeList.begin());

    foreach(TimeLine timeLine, timeList) {
        if(timeLine.start < first.start)
            first = timeLine;
    }
    return first;
}

TimeLine getNextTimeLine(TimeLine from)
{
    TimeLine next;
    found = false;
    foreach(TimeLine timeLine, timeList) {
        if(timeLine.start >= (from.end + turnaround_time) && (!found || timeLine.start < next.start) &&
            ((from.line == ATOB && timeLine.line == BTOA) || (from.line == BTOA && timeLine.line == ATOB))) {
            next = timeLine;
            found = true;
        }
    }
    return next;
}

void removeTimeLine(TimeLine timeLine)
{
    for(TimeList::iterator it = timeList.begin(); it != timeList.end(); it++)
    {
        if((*it).start == timeLine.start && (*it).end == timeLine.end && (*it).line == timeLine.line) {
            timeList.erase(it);
            break;
        }
    }
}

int main(int argc, char *argv[])
{
#ifdef FILE_INPUT
    if(argc < 2)
        return 0;
    ifstream fin(argv[1]);
#endif

    uint32 numcases;
    din >> numcases;

    for(uint32 casee = 1; casee <= numcases; casee++) {

        din >> turnaround_time;
        turnaround_time *= 60;
        din >> na;
        din >> nb;

        timeList.clear();
        fornum(na) {
            string startTime, endTime;
            din >> startTime >> endTime;
            timeList.push_back(TimeLine(convertTime(startTime),convertTime(endTime),ATOB));
        }

        fornum(nb) {
            string startTime, endTime;
            din >> startTime >> endTime;
            timeList.push_back(TimeLine(convertTime(startTime),convertTime(endTime),BTOA));
        }

        uint32_t startA = 0, startB = 0;

        while(!timeList.empty()) {
            TimeLine timeLine = getFirstTimeLine();
            removeTimeLine(timeLine);
            if(timeLine.line == ATOB)
                startA++;
            else if(timeLine.line == BTOA)
                startB++;
            timeLine = getNextTimeLine(timeLine);
            while(found) {
                removeTimeLine(timeLine);
                timeLine = getNextTimeLine(timeLine);
            }
            removeTimeLine(timeLine);
        }

        dout << "Case #" << casee << ": " << startA << " " << startB << endl;
    }
    return 0;
}

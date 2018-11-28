#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>
#include <algorithm>
#include <utility>
#include <map>
#include <queue>
#include <set>

#include <stdlib.h>
#include <string.h>
#include <math.h>

// Loops
#define FOR(i, a, b)    for( int i = a, _b = b; i <= _b; i++ )
#define FORD(i, b, a)   for( int i = b, _a = a; i >= _a; i-- )
#define REP(i, n)       FOR(i, 0, n - 1)
#define REPD(i, n)      FORD(i, n - 1, 0)
#define NP_PRIME(x)		x == 2 ? 3 : x + 2

// Number types
#define llong  long long
#define ullong unsigned long long

// FILES
std::string prefix_file_name = "C-small-attempt0";
std::ifstream finput  ( (prefix_file_name + ".in") .c_str() );
std::ofstream foutput ( (prefix_file_name + ".out").c_str() );

// WHERE PRINTING
#define CONSOLE 0
#if CONSOLE == 1
	#define OUT std::cout
#else
	#define OUT foutput
#endif

// Debug and print options
#define DEBM(x, msg)    OUT << "DEB(" << #x << "): " << (x) << " - " << (msg) << std::endl
#define DEB(x)          OUT << "DEB(" << #x << "): " << (x) << std::endl
#define PS(x)           OUT << (x) << " "
#define PL(x)           OUT << (x) << std::endl
#define NL()            OUT << std::endl
#define PAUSE()			system("PAUSE")

clock_t __starttime;

#define STIME  __starttime = clock()
#define RTIME  std::cout << "\nTime: " << double(clock() - __starttime) / ((double)(CLOCKS_PER_SEC)) << " ms\n"

std::set< std::pair<int, int> > setpair;

int main()
{
	STIME;
	
	/* ------------------------------------------- */
	int ncases, a, b, m, count;
	char buffer[16];
	std::string number, tmp;
	
    finput >> ncases;
    REP(i, ncases)
    {
        finput >> a >> b;
        setpair.clear();
        count = 0;
        FOR(n, a, b)
        {
            sprintf(buffer, "%d", n);
            number = buffer;
            REP(k, number.size() - 1)
            {
                if( number[k + 1] >= number[0] )
                {
                    tmp = number.substr(k + 1, number.size()) + number.substr(0, k + 1);
                    sscanf(tmp.c_str(), "%d", &m);
                    if( n < m && a <= m && m <= b )
                        count += setpair.insert( std::make_pair(n, m) ).second;
                }
            }
        }
        OUT << "Case #" << i + 1 << ": " << count << "\n";
    }
	
	/* ------------------------------------------- */
	
	RTIME;
	PAUSE();
	return 0;
}


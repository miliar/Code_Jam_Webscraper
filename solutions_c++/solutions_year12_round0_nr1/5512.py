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
std::string prefix_file_name = "A-small-attempt0";
std::ifstream finput  ( (prefix_file_name + ".in") .c_str() );
std::ofstream foutput ( (prefix_file_name + ".out").c_str() );

// WHERE PRINTING
#define CONSOLE 1
#if CONSOLE == 0
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


int main()
{
	STIME;
	
	/* ------------------------------------------- */
	int ncases;
	char buffer[128];
	char maplet['z' + 1];
	bool used['z' + 1];
	
    FOR(i, 'a', 'z')
    {
        maplet[i] = '#';
        used[i] = false;
    }
	
    char google[3][128] = {"ejp mysljylc kd kxveddknmc re jsicpdrysi", "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd", "de kr kd eoya kw aej tysr re ujdr lkgc jv"};	
	char sample[3][128] = {"our language is impossible to understand", "there are twenty six factorial possibilities", "so it is okay if you want to just give up"};
    
    REP(i, 3)	
    	REP(j, strlen(google[i]))
            maplet[google[i][j]] = sample[i][j];
    
    maplet['q'] = 'z';
    maplet['z'] = 'q';
	
    finput >> ncases;
	finput.getline(buffer, 128);
    REP(i, ncases)
    {
        finput.getline(buffer, 128);
        OUT << "Case #" << i + 1 << ": ";
        REP(j, strlen(buffer))
            OUT << maplet[buffer[j]];
        NL();
    }

	
	/* ------------------------------------------- */
	
	RTIME;
	PAUSE();
	return 0;
}


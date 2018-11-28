#/* to compile, run this file in a bash shell (with apparent dependencies met)
g++ -g -O3 -ffast-math -Wall -march=native -o bin $0 lib/gnuplot_i.c lib/mt19937ar.c -lm -lgmp -lgmpxx && ./bin
exit
*/

/*	
	Solution by Matthew Lai (cyberfish) 
	My solutions may use -
		Boost (http://www.boost.org)
		GNU MP Bignum Library (http://gmplib.org)
		MPFR Library (http://www.mpfr.org)
		Mersenne Twister reference implementation 
		    (http://www.math.sci.hiroshima-u.ac.jp/~m-mat/MT/MT2002/CODES/mt19937ar.c, with the main() function removed)
		
	Code contains reference to Gnuplot (http://www.gnuplot.info) used for debugging, and an ANSI C interface for it (http://ndevilla.free.fr/gnuplot/)

*/

#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <sstream>
#include <algorithm>
#include <list>
#include <queue>
#include <stack>
#include <utility>

#include <cstdio>
#include <cmath>
#include <cstring>
#include <cassert>
#include <climits>

#include <gmp.h>
#include <gmpxx.h>

#include "lib/gnuplot_i.h"

#include <boost/tuple/tuple.hpp>
#include <boost/tuple/tuple_comparison.hpp>
#include <boost/tuple/tuple_io.hpp>

using namespace std;

typedef unsigned long long int uint64;
typedef signed long long int int64;

template <class T>
T max(T &a, T &b) { return (a > b) ? a : b; }
template <class T>
T min(T &a, T &b) { return (a > b) ? b : a; }
template <class T>
T xchg(T &a, T &b) { T t = a; a = b; b = t; }

int read_int(); /* read an int on its own line */
const char *read_line(); /* read a line from cin, return a char*, and leak ;) */

template <class T>
void dbg_print_vector(const string &id, const vector<T> &v, int start_idx = 0, int end_idx = -1);

/* from Mersenne Twister */
void init_genrand(unsigned long s);
unsigned long genrand_int32(void);
double genrand_real(void); /* [0, 1] */

void gen_primes(int64 a, int64 b, vector<int64> &v); /* generate all primes [a, b] and store them in v */

bool valid(const vector<vector<int> > &map, int x, int y) {
    return (x >= 0 && x < map[0].size() && y >= 0 && y < map.size());
}

pair<int, int> flow_where(const vector<vector<int> > &map, int x, int y) { /* -1, -1 means nowhere */
    if ((!valid(map, x+1, y) || (map[y][x+1] >= map[y][x])) &&
        (!valid(map, x, y+1) || (map[y+1][x] >= map[y][x])) &&
        (!valid(map, x-1, y) || (map[y][x-1] >= map[y][x])) &&
        (!valid(map, x, y-1) || (map[y-1][x] >= map[y][x]))) {
        
        return make_pair(-1, -1);
    }    
    
    int min_alt = INT_MAX;
    
    if (valid(map, x+1, y) && (map[y][x+1] < min_alt)) min_alt = map[y][x+1];
    if (valid(map, x, y+1) && (map[y+1][x] < min_alt)) min_alt = map[y+1][x];
    if (valid(map, x-1, y) && (map[y][x-1] < min_alt)) min_alt = map[y][x-1];
    if (valid(map, x, y-1) && (map[y-1][x] < min_alt)) min_alt = map[y-1][x];
    
    if (valid(map, x, y-1) && (map[y-1][x] == min_alt)) return make_pair(x, y-1);
    if (valid(map, x-1, y) && (map[y][x-1] == min_alt)) return make_pair(x-1, y);
    if (valid(map, x+1, y) && (map[y][x+1] == min_alt)) return make_pair(x+1, y);
    if (valid(map, x, y+1) && (map[y+1][x] == min_alt)) return make_pair(x, y+1);
    
    assert(false);
    
}

void color(vector<vector<int> > &color_map, const vector<vector<int> > &alt_map, int x, int y, int fill_color) {
    color_map[y][x] = fill_color;
    
    pair<int, int> this_loc = make_pair(x, y);
    
    pair<int, int> ret;
    
    if (valid(alt_map, x+1, y) && (color_map[y][x+1] == -1)) {
    
        ret = flow_where(alt_map, x+1, y);
        
        if (ret == this_loc) color(color_map, alt_map, x+1, y, fill_color);
        
    }
    
    if (valid(alt_map, x-1, y) && (color_map[y][x-1] == -1)) {
    
        ret = flow_where(alt_map, x-1, y);
        
        if (ret == this_loc) color(color_map, alt_map, x-1, y, fill_color);
        
    }
    
    if (valid(alt_map, x, y+1) && (color_map[y+1][x] == -1)) {
    
        ret = flow_where(alt_map, x, y+1);
        
        if (ret == this_loc) color(color_map, alt_map, x, y+1, fill_color);
        
    }
        
    if (valid(alt_map, x, y-1) && (color_map[y-1][x] == -1)) {
    
        ret = flow_where(alt_map, x, y-1);
        
        if (ret == this_loc) color(color_map, alt_map, x, y-1, fill_color);
        
    }
}

void docase(int64 case_number) {

    int h, w;
    
    sscanf(read_line(), "%d %d", &h, &w);
    
    vector<vector<int> > alt_map; /* [h][w] */
    
    for (int i = 0; i < h; ++i) {
        vector<int> this_row;
        stringstream ss(read_line());
        for (int r = 0; r < w; ++r) {
            int t;
            ss >> t;
            this_row.push_back(t);
        }
        alt_map.push_back(this_row);
    }
    
    vector<pair<int, int> > sinks;
    
    for (int i = 0; i < h; ++i) {
        for (int r = 0; r < w; ++r) {
            pair<int, int> rt = flow_where(alt_map, r, i);
            
            if (rt == make_pair(-1, -1)) {
                sinks.push_back(make_pair(r, i));
            }
        }
    }
    
    vector<vector<int> > color_map; /* -1 = uncolored */
    
    for (int i = 0; i < h; ++i) {
        vector<int> this_row;
        for (int r = 0; r < w; ++r) {
            this_row.push_back(-1);
        }
        color_map.push_back(this_row);
    }
    
    int fill_c = 0;
    
    for (size_t i = 0; i < sinks.size(); ++i) {
        color(color_map, alt_map, sinks[i].first, sinks[i].second, fill_c++);
    }
    
    cout << "Case #" << case_number << ": " << endl;
    
    char assign = 'a';
    map<int, char> assignments;
    for (int i = 0; i < h; ++i) {
        for (int r = 0; r < w; ++r) {
            if (assignments.find(color_map[i][r]) == assignments.end()) {
                assignments[color_map[i][r]] = assign++;
            }
            cout << assignments[color_map[i][r]] << " ";
        }
        cout << endl;
    }
}

int main() {	
	int64 numcases;
	numcases = read_int();
	
	for (int64 i = 0; i < numcases; ++i) {
	    docase(i+1);
	}
}




int read_int() {
    string t;
    getline(cin, t);
    return atoi(t.c_str());
}

const char *read_line() {
    string* t = new string;
    getline(cin, *t);
    return t->c_str();
}

template <class T>
void dbg_print_vector(const string &id, const vector<T> &v, int start_idx, int end_idx) {
    if (end_idx == -1) end_idx = v.size() - 1;
    
    cout << id << "[" << start_idx << "-" << end_idx << "] ";
    
    for (size_t i = (size_t) start_idx; i <= (size_t) end_idx; ++i) {
        cout << v[i] << " ";
    }
    
    cout << endl;
}

void gen_primes(int64 a, int64 b, vector<int64> &v) { /* do the sieve */
    vector<bool> isPrime(b+1); /* using the bitfield specialization */
    int64 limit = sqrt(b) + 1;
    for (size_t i = 0; i < isPrime.size(); ++i) {  
        isPrime[i] = true;
    }
    
    isPrime[0] = isPrime[1] = false;
    
    for (size_t i = 2; i < isPrime.size(); ++i) {
        if (isPrime[i]) {
            if (i >= a && i <= b) v.push_back(i);
            if (i <= limit) {
                for (size_t r = i; r < isPrime.size(); r += i) {
                    isPrime[r] = false;
                }
            }
        }
    }
}


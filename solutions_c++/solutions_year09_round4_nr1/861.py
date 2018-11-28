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

void docase(int64 case_number) {

    int N;
    
    cin >> N;
    
    list<int> min_rows;
    
    for (int i = 0; i < N; ++i) {  
        string s;
        cin >> s;
        int min_row = N - 1;
        for (int q = s.length() - 1; q >= 0; --q) {
            if (s[q] == '1') break;
            --min_row;
        }
        min_rows.push_back(min_row);
    }
    
    int64 swap_count = 0;
    int64 pos = 0;
    for (list<int>::iterator it = min_rows.begin(); it != min_rows.end();) {
        if (pos < *it) {
            int64 pos_r = pos;
            for (list<int>::iterator itr = it; itr != min_rows.end(); ++itr) {
                if (*itr <= pos) {
                    min_rows.insert(it, *itr);
                    min_rows.erase(itr);
                    swap_count += pos_r - pos;
                    break;
                }
                ++pos_r;
            }
        } else {
            ++it;
        }
        pos++;
    }

    cout << "Case #" << case_number << ": " << swap_count << endl;
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


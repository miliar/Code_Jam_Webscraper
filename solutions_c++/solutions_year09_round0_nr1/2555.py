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



set<string> dictionary;

int64 count(set<string> s, vector<set<char> > &pattern) {

    if (s.empty()) return 0;
    
    int64 first_pair = -1;    
    string first_str; /* up to the first pair */
    
    for (int64 i = 0; i < pattern.size(); ++i) {
        if (pattern[i].size() > 1) {
            first_pair = i;
            break;
        }
        first_str.push_back(*(pattern[i].begin()));
    }
    
    if (first_pair == -1) {
        if (s.find(first_str) == s.end()) {
            return 0;
        } else {
            return 1;
        }
    }
    
    /* remove bad dictionary entries */
    for (set<string>::iterator it = s.begin(); it != s.end();) {
        bool erased = false;
        for (size_t i = 0; i < it->length(); ++i) {
            if (pattern[i].find((*it)[i]) == pattern[i].end()) {
                s.erase(it++);
                erased = true;
                break;
            }
        }
        if (!erased) ++it;
    }
    
    if (s.empty()) return 0;
    
    vector<set<char> > pattern_t = pattern;    
    
    set<char> subpattern_try = pattern[first_pair];
    
    int64 count_r = 0;
    
    for (set<char>::iterator it = subpattern_try.begin(); it != subpattern_try.end(); ++it) {
        pattern_t[first_pair].clear();
        pattern_t[first_pair].insert(*it);
        
        count_r += count(s, pattern_t);
    }
    
    return count_r;
    
}	
	
int l, d, n;

void docase(int64 case_number) {

    string pat;
    getline(cin, pat);
    
    size_t idx = 0;
    
    vector<set<char> > pattern;
    
    for (size_t i = 0; i < l; ++i) {
        set<char> this_subpat;
        char first_char;
        first_char = pat[idx++];
        if (first_char != '(') {
            this_subpat.insert(first_char);
        } else {
            do {
                first_char = pat[idx++];
                if (first_char != ')') {
                    this_subpat.insert(first_char);
                }
            } while (first_char != ')');
        }
        pattern.push_back(this_subpat);
    }

    cout << "Case #" << case_number << ": " << count(dictionary, pattern) << endl;
}

int main() {
	
	sscanf(read_line(), "%d %d %d", &l, &d, &n);
	
	for (int i = 0; i < d; ++i) {
	    string wd;
	    getline(cin, wd);
	    dictionary.insert(wd);
	    assert(wd.length() == l);
	}
	
	for (int i = 0; i < n; ++i) {
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


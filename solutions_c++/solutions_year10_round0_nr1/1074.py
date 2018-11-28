#define NDEBUG
#include <algorithm>
#include <cctype>
#include <cmath>
#include <cstdarg>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <deque>
#include <fstream>
#include <functional>
#include <iomanip>
#include <iostream>
#include <iterator>
#include <limits>
#include <list>
#include <map>
#include <numeric>
#include <set>
#include <sstream>
#include <stack>
#include <queue>
#include <utility>
#include <vector>

using namespace std;

/* Macros */

#ifdef NDEBUG
# define DBG if (1) {} else
#else
# define DBG if (0) {} else
#endif

// number of elements in an array
#define nelems(_arr) (sizeof(_arr) / sizeof((_arr)[0]))
// all of a container
#define all(_cont) (_cont).begin(), (_cont).end()
// all of an array
#define alla(_arr) (_arr), (_arr) + nelems(_arr)
// poor man's auto: the iterator type of a container
#define Iter(_cont) typeof((_cont).begin())

// loop an array with index
#define fora(_i, _a)				\
	for (int _i = 0; _i < nelems(_a); ++_i)
// loop a container with index
#define forc(_i, _v)							\
	for (typeof((_v).size()) _i = 0; _i < (_v).size(); ++_i)
// loop all items in a container with iterator
#define foreach(_i, _c)							\
	for (typeof((_c).begin()) _i = (_c).begin(), __ei = (_c).end(); \
	     _i != __ei; ++_i)

// repeat N times
#define dotimes(_i, _rep)				\
	for (typeof(_rep) _i = 0; _i < (_rep); ++_i)
// loop through a range [_beg, _end)
#define dorange(_i, _beg, _end)						\
	for (typeof(_beg) _i = (_beg), __e = (_end); _i != __e; ++_i)
// loop through a range, [_beg, _end]
#define dorangei(_i, _beg, _end)					\
	for (typeof(_beg) _i = (_beg), __e = (_end)+1; _i != __e; ++_i)

/* Type shorthands of questionable value */

typedef long long llong;
typedef unsigned long long ullong;

typedef set<string> sset;
typedef set<int> iset;
typedef vector<int> ivector;
typedef vector<string> svector;
typedef vector<ivector> imatrix;
typedef vector<char> cvector;
typedef vector<vector<char> > cmatrix;
typedef queue<int> iqueue;
typedef queue<string> squeue;
typedef deque<int> ideque;
typedef map<int, int> iimap;
typedef map<int, string> ismap;
typedef map<string, int> simap;
typedef map<string, string> ssmap;
typedef pair<int, int> iipair;

/* I/O helpers */

// a streambuf which discards everything
struct devnull: streambuf {
	int overflow(int c) { return traits_type::not_eof(c); }
};

// an iomanip that eats everything until the next newline
istream&
endl(istream &is)
{
	return is.ignore(numeric_limits<streamsize>::max(), '\n');
}

// an iomanip that skips spaces and tabs, but not newlines
istream&
skipsp(istream &is)
{
	char c;
	while (is.get(c)) {
		if (c != ' ' && c != '\t') {
			is.unget();
			break;
		}
	}
	return is;
}

// asserts that the next char is delim
// if yes, it it consumed, otherwise failbit is set
istream&
operator>>(istream &is, char const &delim)
{
	if (is.peek() != delim)
		is.setstate(ios::failbit);
	else
		is.ignore();
	return is;
}

struct __ignore_range_s {
	__ignore_range_s(char const *range) : set(range) {}
	char const *set;
};

istream&
operator>>(istream &is, __ignore_range_s const &ir)
{
	char c;
	while (is.get(c)) {
		bool inset = strchr(ir.set, c) != NULL;
		if (!inset) {
			is.unget();
			break;
		}
	}
	return is;
}

// skips over all characters from RANGE
__ignore_range_s
skip(char const *range)
{
	return __ignore_range_s(range);
}

struct __skipto_s {
	__skipto_s(char c) : delim(c) {};
	char delim;
};

istream&
operator>>(istream &is, __skipto_s const &sts)
{
	return is.ignore(numeric_limits<streamsize>::max(), sts.delim);
}

// ignores all characters till DELIM
__skipto_s
skipto(char c)
{
	return __skipto_s(c);
}

struct __accept_range_s {
	__accept_range_s(char const *range, string &s, bool inclusive = true) :
		set(range), s(s), inclusive(inclusive) {}
	__accept_range_s const &operator!() { inclusive = !inclusive; return *this; }
	char const *set;
	string &s;
	bool inclusive;
};

istream&
operator>>(istream &is, __accept_range_s const &ar)
{
	char c;
	ar.s.clear();
	while (is.get(c)) {
		bool inset = strchr(ar.set, c) != NULL;
		if (ar.inclusive != inset) {
			is.unget();
			break;
		}
		ar.s += c;
	}
	return is;
}

// inputs a string S consisting of characters in RANGE.  use the negation
// operator in the return value to input characters NOT in the range
__accept_range_s
from(char const *range, string &s)
{
	return __accept_range_s(range, s, true);
}

// split S into INTO along chars from DELIM
template <typename T>
static void
split(string const &s, T &into, char const *delim = " ")
{
	istringstream iss(s);
	string w;
	while (iss) {
		iss >> skip(delim);
		if (!iss) break;
		iss >> !from(delim, w);
		into.push_back(w);
	}
}

// braindead sprintf into a string, for small formatting ops
string
fmt(char const *format, ...)
{
	va_list ap;
	va_start(ap, format);
	char buf[512];
	int w = vsnprintf(buf, sizeof(buf), format, ap);
	va_end(ap);
	if (w < 0)
		return string("(sprintf error)");
	string ret(buf);
	if (w > int(sizeof(buf) - 1))
		ret += "...";
	return ret;
}

/* Printing containers */

// print something without any specific rule
template <typename T>
ostream&
pprint(ostream &os, T const &v)
{
	return os << v;
}

// print a char
ostream&
pprint(ostream &os, char c)
{
	os << '\'';
	if (c < 32)
		os << "\\x" << hex << setw(2) << setfill('0') << int(c);
	else
		os << c;
	os << '\'';
	return os;
}

// print a string
ostream&
pprint(ostream& os, string const &s)
{
	os << '"';
	foreach (c, s) {
		if (*c == '"') os << "\\\"";
		else if (*c == '\\') os << "\\\\";
		else os << *c;
	}
	os << '"';
	return os;
}

// prints a pair
template <typename A, typename B>
ostream&
pprint(ostream &os, pair<A, B> const &p)
{
	os << '(';
	pprint(os, p.first);
	os << ", ";
	pprint(os, p.second);
	os << ')';
	return os;
}

// prints a sequence
template <typename Iter>
ostream&
pprint(ostream &os, Iter beg, Iter end, char sl = '[', char el = ']')
{
	os << sl;
	for (Iter it = beg; it != end; ++it) {
		if (it != beg)
			os << ", ";
		pprint(os, *it);
	}
	os << el;
	return os;
}

// prints an associative container
template <typename Tk, typename Tv>
ostream&
pprint(ostream &os, map<Tk, Tv> const &m)
{
	typedef typename map<Tk, Tv>::const_iterator Ci;
	os << "{\n";
	Ci beg = m.begin(), end = m.end();
	for (Ci it = beg; it != end; ++it) {
		os << "  ";
		pprint(os, it->first);
		os << " => ";
		pprint(os, it->second);
		os << '\n';
	}
	os << '}';
	return os;
}

// "... then I saw cout shifted left by "hello world" and I stopped."
template <typename T>
ostream& operator<<(ostream &os, vector<T> const &v)
{ return pprint(os, all(v)); }
template <typename T>
ostream& operator<<(ostream &os, list<T> const &v)
{ return pprint(os, all(v)); }
template <typename T>
ostream& operator<<(ostream &os, deque<T> const &v)
{ return pprint(os, all(v)); }
template <typename T>
ostream& operator<<(ostream &os, stack<T> const &v)
{ return pprint(os, all(v)); }
template <typename T>
ostream& operator<<(ostream &os, queue<T> const &v)
{ return pprint(os, all(v)); }
template <typename T>
ostream& operator<<(ostream &os, priority_queue<T> const &v)
{ return pprint(os, all(v)); }
template <typename T>
ostream& operator<<(ostream &os, set<T> const &s)
{ return pprint(os, all(s), '<', '>'); }
template <typename Tk, typename Tv>
ostream& operator<<(ostream &os, map<Tk, Tv> const &m)
{ return pprint(os, m); }
template <typename A, typename B>
ostream& operator<<(ostream &os, pair<A, B> const &p)
{ return pprint(os, p); }

/* blah */

template <typename E, typename C>
static inline bool
elem(E const &e, C const &c)
{
	return c.find(e) != c.end();
}

template <typename E, typename C>
static inline bool
celem(E const &e, C const &c)
{
	return find(all(c), e) != c.end();
}

static inline void CRASH() { *((int *)0) = 0; }

/* We need colors. */
#define fg(col) (__termcolor_##col)
static char const __termcolor_red[] = "\e[1;31m";
static char const __termcolor_green[] = "\e[1;32m";
static char const __termcolor_yellow[] = "\e[1;33m";
static char const __termcolor_blue[] = "\e[1;36m";
static char const __termcolor_norm[] = "\e[0m";

#define __SEEN_LIBH
#ifndef __SEEN_LIBH
# include "../lib.h"
#endif

int main()
{
	int T;
	cin >> T;
	dorangei(c, 1, T) {
		int N, K;
		cin >> N >> K;
		bool on = (K & ((1 << N) - 1)) == ((1 << N) - 1);
		cout << "Case #" << c << ": " << (on ? "ON" : "OFF") << endl;
	}
}

#define NDEBUG
#include <algorithm>
#include <cassert>
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
typedef vector<cvector> cmatrix;
typedef vector<llong> llvector;
typedef vector<ullong> ullvector;
typedef vector<llvector> llmatrix;
typedef vector<ullvector> ullmatrix;
typedef queue<int> iqueue;
typedef queue<string> squeue;
typedef deque<int> ideque;
typedef map<int, int> iimap;
typedef map<int, string> ismap;
typedef map<string, int> simap;
typedef map<string, string> ssmap;
typedef pair<int, int> iipair;

/* I/O helpers */

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

#define __SEEN_LIBH
#ifndef __SEEN_LIBH
# include "../lib.h"
# include "../dbg.h"
#endif

static void
prb(cmatrix const &b)
{
	foreach (ri, b) {
		foreach (ci, *ri) clog << *ci;
		clog << endl;
	}
}

static cmatrix
rotate(cmatrix const &b)
{
	cmatrix rot(b);
	int N = b.size();
	forc (i, b) {
		forc (j, b[i]) {
			rot[i][j] = b[N-j-1][i];
		}
	}
	return rot;
}

static cmatrix
gravity(cmatrix const &b, ivector const &gap)
{
	cmatrix fall(b.size(), cvector(b.size(), '.'));
	int N = b.size();
	forc (c, b) {
		int i = N-1, j = N-1;
		while (i >= 0) {
			while (i >= 0 && b[i][c] == '.') --i;
			if (i >= 0)
				fall[j--][c] = b[i--][c];
		}
	}
	return fall;
}

static bool
check(cmatrix const &b, int r, int c, int dr, int dc, char player, int K)
{
	int N = b.size();
	while (r < N && c < N && r >= 0 && c >= 0 && K > 0) {
		if (b[r][c] != player) return false;
		--K;
		r += dr;
		c += dc;
	}
	return K == 0;
}

static pair<bool, bool>
win(cmatrix const &b, int K)
{
	pair<bool, bool> ret = make_pair(false, false);
	int N = b.size();
	dotimes(i, N) dotimes(j, N) {
		ret.first |= check(b, i, j, 1, 0, 'R', K);
		ret.second |= check(b, i, j, 1, 0, 'B', K);
		ret.first |= check(b, i, j, 0, 1, 'R', K);
		ret.second |= check(b, i, j, 0, 1, 'B', K);
		ret.first |= check(b, i, j, 1, 1, 'R', K);
		ret.second |= check(b, i, j, 1, 1, 'B', K);
		ret.first |= check(b, i, j, 1, -1, 'R', K);
		ret.second |= check(b, i, j, 1, -1, 'B', K);
	}
	return ret;
}

int main()
{
	int T;
	cin >> T;
	dorangei(c, 1, T) {
		int N, K;
		cin >> N >> K >> endl;
		cmatrix board(N, cvector(N, '.'));
		ivector gap(N);
		dotimes(i, N) {
			string s;
			getline(cin, s);
			forc (j, s) board[i][j] = s[j];
			gap[N-1-i] = s.find_last_not_of('.');
		}
		//prb(board);
		//clog << gap << endl;
		cmatrix rb = rotate(board);
		//prb(rb);
		cmatrix fall = gravity(rb, gap);
		//prb(fall);
		pair<bool, bool> w = win(fall, K);
		cout << "Case #" << c << ": ";
		if (w.first) {
			if (w.second)
				cout << "Both";
			else
				cout << "Red";
		} else {
			if (w.second)
				cout << "Blue";
			else
				cout << "Neither";
		}
		cout << endl;
	}
}

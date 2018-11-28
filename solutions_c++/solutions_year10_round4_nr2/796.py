// This source require GCC 4.5.
// Requires the BigInteger library from http://mattmccutchen.net/bigint/
// Compile with g++ -std=c++0x

#include <iostream>
#include <algorithm>
#include <vector>
#include <functional>
#include <queue>
#include <stack>
#include <deque>
#include <iterator>
#include <map>
#include <set>
#include <stdio.h>
#include <math.h>
#include <list>
#include <utility>
#include <numeric>
#include <sstream>
#include <array>
#include <unordered_map>
#include <unordered_set>
#include <iomanip>
#include "BigIntegerLibrary.hh"

#define for0(i,n) for (decltype(n) i = 0; i < (n); ++i)
#define for1(i,n) for (decltype(n) i = 1; i <= (n); ++i)
#define forr(i,a,b) for (auto i = (a); i < (b); ++i)
#define foreach(i,c) for(auto i = ::begin(c); i != ::end(c); ++i)
#define all(x) ::begin(x), ::end(x)
#define PB push_back
#define SS size()
#define Fn(init, rval) [&](init) { return rval; }

typedef long long ll;
typedef long double ld;
typedef BigInteger big;

const double eps = 1e-8;
const double pi = 2.0 * acos(0.0);

//=============================================================================
// ITERATOR HELPERS
//=============================================================================

template <class T> typename T::iterator begin(T& x) { return x.begin(); }
template <class T> typename T::iterator end(T& x) {	return x.end(); }
template <class T> typename T::const_iterator begin(const T& x) { return x.begin(); }
template <class T> typename T::const_iterator end(const T& x) {	return x.end(); }

template <class T, std::size_t N>
T* begin(T (& x)[N]) { return x; }

template <class T, std::size_t N>
T* end(T (& x)[N]) { return x + N; }


//=============================================================================
// CONVENIENCE STL WRAPPERS/HELPERS
//=============================================================================

template <class A, class B>
std::istream& operator>>(std::istream& is, std::pair<A, B>& p)
{
	return is >> p.first >> p.second;
}

template <class A, class B>
std::ostream& operator<<(std::ostream& os, const std::pair<A, B>& p)
{
	return os << '(' << p.first << ", " << p.second << ')';
}

template <class T>
void for_all(T& x, std::function<void(typename T::value_type)> f)
{
	std::for_each(begin(x), end(x), f);
}

template <class T>
void sort(T& x)
{
	std::sort(begin(x), end(x));
}

template <class T, class F>
void sort(T& x, F f)
{
	std::sort(begin(x), end(x), f);
}

template <class T>
void reverse(T& x)
{
	std::reverse(begin(x), end(x));
}

template <class T>
T reversed(const T& x)
{
	T temp(x);
	reverse(temp);
	return temp;
}

template <class T>
int count(const T& x, typename T::value_type const& v)
{
	return std::count(begin(x), end(x), v);
}

template <class T>
int count_if(const T& x, std::function<bool(char)> f)
{
	return std::count_if(begin(x), end(x), f);
}

template <class T>
int index_of(const T& c, typename T::value_type const& x)
{
	auto i = std::find(begin(c), end(c), x);
	if (i == end(c)) return -1;
	return std::distance(begin(c), i);
}

template <class T>
bool contains(const T& c, typename T::value_type const& x)
{
	return std::find(begin(c), end(c), x) != end(c);
}

template <class T>
bool next_permutation(T& x)
{
	return std::next_permutation(begin(x), end(x));
}

template <class T>
bool prev_permutation(T& x)
{
	return std::prev_permutation(begin(x), end(x));
}

template <class T>
std::vector<T> read_n(int n)
{
	std::vector<T> v(n);
	for (int i = 0; i < n; ++i)
		std::cin >> v[i];
	return v;
}

template <class T>
std::vector< std::pair<T, int> > indexed_vector(const T& x)
{
	std::vector< std::pair<T, int> > v;
	int i = 0;
	foreach (p, x)
		v.PB(std::pair<T, int>(*p, i++));
	return v;
}

template <class T>
std::string to_string(const T& x)
{
	std::stringstream ss;
	ss << x;
	return ss.str();
}

template <>
std::string to_string(const big& x)
{
	return bigIntegerToString(x);
}

template <class T>
T parse(const std::string& s)
{
	std::stringstream ss(s);
	T x;
	ss >> x;
	return x;
}

template <>
big parse(const std::string& s)
{
	return stringToBigInteger(s);
}
	

//=============================================================================
// VECTOR MATH 2D
//=============================================================================

template <class T>
struct v2
{
    T x, y;

    typedef v2<T> const& cref;
    typedef v2<T>& ref;

    v2() : x(T(0)), y(T(0)) {}
    v2(T x, T y) : x(x), y(y) {}
    v2(cref p) : x(p.x), y(p.y) {}
    v2(std::initializer_list<T> in) : x(*(in.begin())), y(*(in.begin()+1)) {}

    friend v2<T>    operator+(cref a, cref b)   { return v2<T>(a.x + b.x, a.y + b.y); }
    friend v2<T>    operator-(cref a, cref b)   { return v2<T>(a.x - b.x, a.y - b.y); }
    friend v2<T>    operator*(cref a, T m)      { return v2<T>(a.x * m, a.y * m); }
    friend v2<T>    operator*(T m, cref a)      { return v2<T>(m * a.x, m * a.y); }
    friend v2<T>    operator/(cref a, T m)      { return a * (T(1) / m); }
    friend T        operator*(cref a, cref b)   { return a.x * b.x + a.y * b.y; }
    friend T        operator^(cref a, cref b)   { return a * b.perp(); }
    void            operator+=(cref a)          { x += a.x; y += a.y; }
    void            operator-=(cref a)          { x -= a.x; y -= a.y; }
    void            operator*=(T m)             { x *= m; y *= m; }
    void            operator/=(T m)             { x /= m; y /= m; }
    friend bool     operator==(cref a, cref b)  { return a.x == b.x && a.y == b.y; }
    friend bool     operator!=(cref a, cref b)  { return !(a == b); }
    friend bool     operator<(cref a, cref b)   { return a.x == b.x ? a.y < b.y : a.x < b.x; }
    friend bool     operator>(cref a, cref b)   { return a.x == b.x ? a.y > b.y : a.x > b.x; }
    friend bool     operator<=(cref a, cref b)  { return !(a > b); }
    friend bool     operator>=(cref a, cref b)  { return !(a < b); }
    v2<T>           perp() const                { return v2<T>(y, -x); }
    double          size() const                { return sqrt(x * x + y * y); }
    T               manh() const                { return abs(x) + abs(y); }
    T               king() const                { return max(abs(x), abs(y)); }
    double          arg() const                 { return atan2(y, x); }
    v2<double>      normalized() const          { return *this / size(); }
    void            normalize()                 { *this /= size(); }

    friend std::istream& operator>>(std::istream& is, ref p) { return is >> p.x >> p.y; }
    friend std::ostream& operator<<(std::ostream& os, cref p) { return os << '(' << p.x << ", " << p.y << ')'; }
    
    struct arg_sort
    {
    	bool operator()(cref a, cref b) { return a.arg() < b.arg(); }
    };
};

typedef v2<float> v2f;
typedef v2<double> v2d;
typedef v2<long double> v2ld;
typedef v2<int> v2i;
typedef v2<ll> v2l;



//=============================================================================
// VECTOR MATH 3D
//=============================================================================

template <class T>
struct v3
{
    T x, y, z;

    typedef v3<T> const& cref;
    typedef v3<T>& ref;

    v3() : x(T(0)), y(T(0)), z(T(0)) {}
    v3(T x, T y, T z) : x(x), y(y), z(z) {}
    v3(cref p) : x(p.x), y(p.y), z(p.z) {}

    friend v3<T>    operator+(cref a, cref b)   { return v3<T>(a.x + b.x, a.y + b.y, a.z + b.z); }
    friend v3<T>    operator-(cref a, cref b)   { return v3<T>(a.x - b.x, a.y - b.y, a.z - b.z); }
    friend v3<T>    operator*(cref a, T m)      { return v3<T>(a.x * m, a.y * m, a.z * m); }
    friend v3<T>    operator*(T m, cref a)      { return v3<T>(m * a.x, m * a.y, m * a.z); }
    friend v3<T>    operator/(cref a, T m)      { return a * (T(1) / m); }
    friend T        operator*(cref a, cref b)   { return a.x * b.x + a.y * b.y + a.z * b.z; }
    friend v3<T>    operator^(cref a, cref b)   { return v3<T>(	a.y * b.z - a.z * b.y,
    															a.z * b.x - a.x * b.z,
    															a.x * b.y - a.y * b.x ); }
    void            operator+=(cref a)          { x += a.x; y += a.y; z += a.z; }
    void            operator-=(cref a)          { x -= a.x; y -= a.y; z -= a.z; }
    void            operator*=(T m)             { x *= m; y *= m; z *= m; }
    void            operator/=(T m)             { x /= m; y /= m; z /= m; }
    friend bool     operator==(cref a, cref b)  { return a.x == b.x && a.y == b.y && a.z == b.z; }
    friend bool     operator!=(cref a, cref b)  { return !(a == b); }
    friend bool     operator<(cref a, cref b)   { return a.x < b.x ? true :
    													 a.x > b.x ? false :
    													 a.y < b.y ? true :
    													 a.y > b.y ? false :
    													 a.z < b.z; }
    friend bool     operator>(cref a, cref b)   { return !(a < b || a == b); }
    friend bool     operator<=(cref a, cref b)  { return a < b || a == b; }
    friend bool     operator>=(cref a, cref b)  { return !(a < b); }
    double          size() const                { return sqrt(x * x + y * y + z * z); }
    T               manh() const                { return abs(x) + abs(y) + abs(z); }
    T               king() const                { return max(abs(x), max(abs(y), abs(z))); }
    v3<double>      normalized() const          { return *this / size(); }
    void            normalize()                 { *this /= size(); }

    friend std::istream& operator>>(std::istream& is, ref p) { return is >> p.x >> p.y >> p.z; }
    friend std::ostream& operator<<(std::ostream& os, cref p) { return os << '(' << p.x << ", " << p.y << ", " << p.z << ')'; }
};

typedef v3<float> v3f;
typedef v3<double> v3d;
typedef v3<long double> v3ld;
typedef v3<int> v3i;
typedef v3<ll> v3l;


//=============================================================================
// RANGE INTERFACE
//=============================================================================

template <class It>
struct filter_iterator
{
	typedef filter_iterator<It> this_t;
	typedef typename std::iterator_traits<It>::value_type value_type;
	typedef typename std::iterator_traits<It>::difference_type difference_type;
	typedef typename std::iterator_traits<It>::reference reference;
	typedef typename std::iterator_traits<It>::pointer pointer;
	typedef typename std::iterator_traits<It>::iterator_category iterator_category;
	typedef value_type const& cref_t;
	
	typedef std::function<bool(cref_t)> fun_t;
	
	filter_iterator(const It& _a, const It& _b, fun_t _f)
	: a(_a), b(_b), f(_f) { while (a != b && !f(*a)) ++a; }
	
	It a, b;
	fun_t f;
	
	this_t& operator++() { do {++a;} while (a != b && !f(*a)); return *this; }
	this_t operator++(int) { this_t t(*this); ++*this; return t; }
	this_t& operator--() { do {--a;} while (!f(*a)); return *this; }
	this_t& operator--(int) { this_t t(*this); --*this; return t; }
	value_type operator*() const { return *a; }
	pointer operator->() const { return &(*a); }
	bool operator==(const this_t& r) const { return a == r.a; }
	bool operator!=(const this_t& r) const { return a != r.a; }
};

template <class It, class Out>
struct compose_iterator
{
	typedef compose_iterator<It, Out> this_t;
	typedef Out value_type;
	typedef typename std::iterator_traits<It>::difference_type difference_type;
	typedef Out& reference;
	typedef Out* pointer;
	typedef typename std::iterator_traits<It>::iterator_category iterator_category;
	typedef Out const& cref_t;
	
	typedef std::function<Out(cref_t)> fun_t;
	
	compose_iterator(const It& a, fun_t f)
	: a(a), f(f) {}
	
	It a;
	fun_t f;
	
	this_t& operator++() { ++a; return *this; }
	this_t operator++(int) { this_t t(*this); ++*this; return t; }
	this_t& operator--() { --a; return *this; }
	this_t& operator--(int) { this_t t(*this); --*this; return t; }
	value_type operator*() const { return f(*a); }
	pointer operator->() const { return &f(*a); }
	bool operator==(const this_t& r) const { return a == r.a; }
	bool operator!=(const this_t& r) const { return a != r.a; }
};

template <class It>
struct range
{
	typedef range<It> this_t;
	typedef typename std::iterator_traits<It>::value_type value_type;
	typedef typename std::iterator_traits<It>::difference_type difference_type;
	typedef typename std::iterator_traits<It>::reference reference;
	typedef typename std::iterator_traits<It>::pointer pointer;
	typedef typename std::iterator_traits<It>::iterator_category iterator_category;
	typedef value_type const& cref_t;
	typedef It iterator;
	typedef const It const_iterator;
	
	range(const It& a, const It& b) : a(a), b(b) {}

	It a, b;
	
	iterator begin() { return a; }
	iterator end() { return b; }
	const_iterator begin() const { return a; }
	const_iterator end() const { return b; }
	
	range<filter_iterator<It>> where(std::function<bool(const value_type&)> f) const
	{
		typedef filter_iterator<It> FIt;
		return range<FIt>(FIt(a, b, f), FIt(b, b, f));
	}
	
	this_t const& print() const
	{
		for (It i = a; i != b; ++i)
		{
			if (i != a) std::cout << ' ';
			std::cout << *i;
		}
		return *this;
	}
	
	this_t const& println() const
	{
		print();
		std::cout << std::endl;
		return *this;
	}
	
	range<compose_iterator<It, value_type>> sub(const value_type& x) const
	{
		typedef compose_iterator<It, value_type> CIt;
		return range<CIt>(CIt(a, Fn(cref_t y, y - x)), CIt(b, Fn(cref_t y, y - x)));
	}
	
	template <class T>
	range<compose_iterator<It, T>> cast() const
	{
		typedef compose_iterator<It, T> CIt;
		return range<CIt>(CIt(a, Fn(cref_t y, static_cast<T>(y))), CIt(b, Fn(cref_t y, static_cast<T>(y))));
	}
	
	ll sum() const
	{
		return std::accumulate(all(*this), value_type(0));
	}
};

template <class It>
range<It> make_range(It a, It b)
{
	return range<It>(a, b);
}

template <class T>
auto R(T& x) -> range<decltype(begin(x))>
{
	return make_range(begin(x), end(x));
}

template <class T>
auto R(const T& x) -> range<decltype(begin(x))>
{
	return make_range(begin(x), end(x));
}


//=============================================================================
// MISCELLANEOUS
//=============================================================================

std::string number_to_string(ll n)
{
	static std::string suffix[5] = {"", "thousand", "million", "billion", "trillion"};
	static std::string prefix[10] = {"", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"};
	static std::string teens[10] = {"ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"}; 
	static std::string singles[10] = {"", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};
	int c[5];
	
	for0 (i, 5)
	{
		c[i] = n % 1000;
		n /= 1000;
	}
	
	std::string out = "";
	
	for (int i = 4; i >= 0; --i)
	{
		if (c[i] == 0) continue;
		int A = (c[i]/100) % 10;
		int B = (c[i]/10) % 10;
		int C = (c[i]/1) % 10;
		if (A) out += singles[A] + " hundred";
		if (A && (B || C)) out += " and ";
		if (B == 1)
			out += teens[C];
		else
		{
			if (B != 0)
			{
				out += prefix[B];
				if (C) out += " ";
			}
			if (C) out += singles[C];
		}
		if (i != 0) out += " ", out += suffix[i];
	}
	
	return out;
}

//=============================================================================
// NUMBER THEORY / COMBINATORICS 
//=============================================================================

const int MAX_PRIMES = 1000000;
std::deque<int> primes(1, 2);

int nth_prime(int i);

template <class T>
bool is_prime(T n)
{
	if (n < 2) return false;
	for (int i = 0; i < MAX_PRIMES; ++i)
	{
		T p = T(nth_prime(i));
		if (p * p > n)
			return true;
		if (n % p == 0)
			return false;		
	}
	// TODO what if n > maxprime^2?
	return true;
}

int nth_prime(int i)
{
	while (primes.size() <= i)
	{
		primes.push_back(primes.back() + 1);
		while (!is_prime(primes.back()))
			primes.back()++;
	}
	// TODO what if i > MAX_PRIMES?
	return primes[i];
}

template <class T>
int count_divisors(T n)
{
	if (n < T(3)) return n;
	
	T c = T(1);
	for (int i = 0; i < MAX_PRIMES; ++i)
	{
		T p = T(nth_prime(i));
		if (p * p > n) return c + c;
		T e = T(1);
		while (n % p == 0)
		{
			++e;
			n /= p;
		}
		if (e > 1) c *= e;
		if (n == 1) return c;
	}
	// TODO what if n > maxprime^2?
}

template <class T>
int count_distinct_prime_factors(T n)
{
	if (n < T(3)) return n;
	
	T c = 0;
	for (int i = 0; i < MAX_PRIMES; ++i)
	{
		T p = T(nth_prime(i));
		if (p * p > n) break;
		if (n % p == 0) c++;
		while (n % p == 0) n /= p;
		if (n == 1) break;
	}
	return c;
	// TODO what if n > maxprime^2?
}

template <class T>
T gcd(const T& a, const T& b)
{
	if (b == 0) return a;
	return gcd(b, a % b);
}

template <class T>
bool coprime(const T& a, const T& b)
{
	return gcd(a, b) == T(1);
}

template <class T>
T lcm(const T& a, const T& b)
{
	return b * (a / gcd(a, b));
}

ll choose(ll n, ll k, ll mod = 0)
{
	const int MAX = 1000;
	static std::vector< std::vector<ll> > c(MAX, std::vector<ll>(MAX, -1));
	if (k == 0) return 1;
	if (n == 0) return 0;
	if (c[n][k] == -1)
	{
		c[n][k] = choose(n-1, k-1) + choose(n-1, k);
		if (mod != 0) c[n][k] %= mod;
	}
	return c[n][k];
}

template <class T>
T fact(int n)
{
	return n <= 1 ? T(1) : T(n) * fact<T>(n-1);
}

template <class T>
T fib(int n)
{
	if (n < 3) return T(1);
	const int MAX = 100000;
	static std::vector<T> cache(MAX, 0);
	if (cache[n] == 0)
		cache[n] = fib<T>(n-1) + fib<T>(n-2);
	return cache[n];
}

template <class T>
T sqr(const T& x)
{
	return x * x;
}

template <class T>
bool is_square(const T& x)
{
	const T r = sqrt(x + 0.5);
	return r * r == x;
}

template <class T>
bool is_cube(const T& x)
{
	const T r = pow(x + 0.5, 0.33333333333);
	return r * r * r == x;
}

template <class T>
bool is_even(const T& x)
{
	return x % 2 == 0;
}

template <class T>
bool is_odd(const T& x)
{
	return !is_even(x);
}

template <class T>
typename T::value_type sum(const T& x)
{
	return std::accumulate(all(x), typename T::value_type(0));
}

template <class T>
T fast_exp(T a, const T& b, const T& mod = T(0))
{
	if (mod != T(0)) a %= mod;
	if (b == T(0)) return T(1);
	if (mod == T(0))
	{
		if (b == T(1)) return a;
		if (b == T(2)) return a * a;
	}
	else
	{
		if (b == T(1)) return a;
		if (b == T(2)) return (a * a) % mod;
	}
	T h = b / T(2);
	T c = fast_exp<T>(a, h, mod);
	if (mod != T(0))
	{
		if (is_even(b)) return (c * c) % mod;
		return (((c * c) % mod) * a) % mod;
	}
	else
	{
		if (is_even(b)) return (c * c);
		return (c * c * a);
	}
}

template <class T>
ll digit_sum(const T& x)
{
	return R(to_string(x)).sub('0').template cast<ll>().sum();
}

template <class T>
v2<T> solve_lin(const v2<T>& a, const v2<T>& b, const v2<T>& c)
{
	T y = (a ^ c) / (a ^ b);
	T x = (b ^ c) / (a ^ b);
	return v2<T>{x, y};
}


using namespace std;

ll N, S, T, Q, K, P;

vector<int> M;
ll INF = 999999999999;

struct Round
{
	int i, j;
	ll p;
	Round* a, * b;
	Round(int i, int j, ll p, Round* a, Round * b)
	:i(i), j(j), p(p), a(a), b(b) { /*cerr << v2i(i,j) << p << endl;*/}
	
	~Round() { delete a; delete b; }
	
	ll solve(int r)
	{
		if (a == 0)
		{
			if (M[i] - r < 0 || M[i+1] - r < 0)
				return INF;
			if (M[i] - r >= 1 && M[i+1] - r >= 1)
				return 0;
			return p;
		}
		return min(p + a->solve(r) + b->solve(r), a->solve(r+1) + b->solve(r+1));
	}
};

vector<ll> p;

void subdiv(Round* r, int& rn)
{
	if (r->i + 2 == r->j) return;
	r->a = new Round(r->i, (r->i + r->j) / 2, p[rn++], 0, 0);
	r->b = new Round((r->i + r->j) / 2, r->j, p[rn++], 0, 0);
	subdiv(r->a, rn);
	subdiv(r->b, rn);
}

void solve()
{
	cin >> P;
	ll N = fast_exp<ll>(2, P);
	M = read_n<int>(N);
	p = read_n<ll>(N-1);
	reverse(p);
	reverse(M);
	
	int rn = 0;
	Round root(0, N, p[rn++], 0, 0);
	Round* r = &root;
	subdiv(r, rn);
	
	cout << root.solve(0) << endl;
}


int main()
{
	int T;
	cin >> T;
	for0 (t, T)
	{
		cout << "Case #" << t+1 << ": ";
		solve();
	}
	return 0;
}
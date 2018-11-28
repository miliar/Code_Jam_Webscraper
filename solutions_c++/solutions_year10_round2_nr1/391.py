// This source require GCC 4.5 to compile.
// (may also work with MSVC++ 2010)
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

#define for0(i,n) for (int i = 0; i < (n); ++i)
#define for1(i,n) for (int i = 1; i < (n); ++i)
#define forr(i,n) for (int i = (n)-1; i >= 0; --i)
#define foreach(i,c) for(auto i = begin(c); i != end(c); ++i)
#define all(x) begin(x), end(x)

typedef long long ll;
typedef long double ld;

const double eps = 1e-8;
const double pi = 3.14159265358979323846264338327950;

template <class T>
typename T::iterator begin(T& x)
{
	return x.begin();
}

template <class T>
typename T::iterator end(T& x)
{
	return x.end();
}

template <class T>
typename T::const_iterator begin(const T& x)
{
	return x.begin();
}

template <class T>
typename T::const_iterator end(const T& x)
{
	return x.end();
}

template <class A, class B>
std::istream& operator>>(std::istream& is, std::pair<A, B>& p)
{
	return is >> p.first >> p.second;
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
std::vector<T> read_vector(int n)
{
	std::vector<T> v(n);
	for (int i = 0; i < n; ++i)
		std::cin >> v[i];
	return v;
}

template <class T>
T sqr(const T& x)
{
	return x * x;
}


template <class T>
struct v2
{
    T x, y;

    typedef v2<T> const& cref;
    typedef v2<T>& ref;

    v2() : x(T(0)), y(T(0)) {}
    v2(T x, T y) : x(x), y(y) {}
    v2(cref p) : x(p.x), y(p.y) {}

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
    friend std::ostream& operator<<(std::ostream& os, cref p) { return os << '(' << p.x << ", " << p.y << ')' << std::endl; }
    
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
    //friend bool     operator<(cref a, cref b)   { return a.x == b.x ? a.y < b.y : a.x < b.x; }
    //friend bool     operator>(cref a, cref b)   { return a.x == b.x ? a.y > b.y : a.x > b.x; }
    //friend bool     operator<=(cref a, cref b)  { return !(a > b); }
    //friend bool     operator>=(cref a, cref b)  { return !(a < b); }
    double          size() const                { return sqrt(x * x + y * y + z * z); }
    T               manh() const                { return abs(x) + abs(y) + abs(z); }
    T               king() const                { return max(abs(x), max(abs(y), abs(z))); }
    v3<double>      normalized() const          { return *this / size(); }
    void            normalize()                 { *this /= size(); }

    friend std::istream& operator>>(std::istream& is, ref p) { return is >> p.x >> p.y >> p.z; }
    friend std::ostream& operator<<(std::ostream& os, cref p) { return os << '(' << p.x << ", " << p.y << ", " << p.z << ')' << std::endl; }
};

typedef v3<float> v3f;
typedef v3<double> v3d;
typedef v3<long double> v3ld;
typedef v3<int> v3i;
typedef v3<ll> v3l;


const int MAX_PRIMES = 1000000;
std::deque<int> primes(1, 2);

int nth_prime(int i);

template <class T>
bool is_prime(T n)
{
	for (int i = 0; i < MAX_PRIMES; ++i)
	{
		T p = T(nth_prime(i));
		if (n % p == 0)
			return false;
		if (p * p > n)
			return true;
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
T gcd(const T& a, const T& b)
{
	if (b == 0) return a;
	return gcd(b, a % b);
}

template <class T>
T lcm(const T& a, const T& b)
{
	return a * b / gcd(a, b);
}

using namespace std;

struct dir
{
	map<string, dir*> subdirs;
	dir() {}
	~dir()
	{
		foreach(i, subdirs)
			delete i->second;
	}
};

dir* root;

int add_path(string path)
{
	int c = 0;
	dir* d = root;
	auto i = path.begin();
	for (;;)
	{
		if (i == path.end()) return c;
		auto j = find(i + 1, path.end(), '/');
		string name(i + 1, j);
		//cout << name << endl;
		if (d->subdirs.count(name))
		{
			d = d->subdirs[name];
		}
		else
		{
			d->subdirs[name] = new dir();
			d = d->subdirs[name];
			c++;
		}
		i = j;
	}
	return c;
}

int main()
{
	int T;
	cin >> T;
	for0 (t, T)
	{
		int n ,m;
		cin >> n >> m;
		
		root = new dir();
		
		string temp;
		getline(cin, temp);
		for0 (i, n)
		{	
			string s;
			getline(cin, s);
			add_path(s);
		}
		
		
		int c = 0;
		for0 (i, m)
		{
			string s;
			getline(cin, s);
			c += add_path(s);
		}
		
		
		cout << "Case #" << t+1 << ": ";
		cout << c;
		cout << endl;
		
		delete root;
	}
	return 0;
}
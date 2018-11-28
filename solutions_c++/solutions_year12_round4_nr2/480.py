#if 1
#include <cstdlib>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <functional>
#include <cstring>
#include <string>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <ctime>
#include <cassert>
#include <sstream>
#include <iostream>
#include <bitset>

using namespace std;

typedef long long LL;
typedef long double LD;
typedef pair<int , int> pii;
typedef vector <int> veci;
typedef vector <veci> graph;
const LD eps = 1e-9;
const LD pi = acos(-1.0);
const int inf = 1000 * 1000 * 1000;
const LL inf64 = LL(inf) * inf;

#define mp make_pair
#define pb push_back
#define X first
#define Y second
#define iss istringstream
#define oss ostringstream
#define dbg(x) {cerr << #x << " = " << x << endl;}
#define dbgv(x) {cerr << #x << " ={"; for (int _i = 0; _i < x.size(); _i++) {if (_i) cerr << ", "; cerr << x[_i];} cerr << "}" << endl;}
#define NAME "problem"

namespace geom
{
	// tested: uva10002
	template<class T>
	struct vec_t
	{
		T x, y;
		vec_t() { x = y = T(0); } 
		vec_t(const T &x, const T &y) : x(x), y(y) {}

		T& operator[](int idx)
		{ return idx ? y : x; }
		const T& operator[](int idx) const
		{ return idx ? y : x; }
		
		vec_t operator + (const vec_t &b) const
		{ return vec_t(x + b.x, y + b.y); }
		vec_t operator - (const vec_t &b) const
		{ return vec_t(x - b.x, y - b.y); }
		vec_t operator - () const 
		{ return vec_t(-x, -y); }
		vec_t operator + () const
		{ return *this; }
		vec_t operator * (const T &b) const
		{ return vec_t(x * b, y * b); }
		vec_t operator / (const T &b) const
		{ return vec_t(x / b, y / b); }

		vec_t& operator += (const vec_t &b)
		{ return *this = *this + b; }
		vec_t& operator -= (const vec_t &b)
		{ return *this = *this - b; }
		vec_t& operator *= (const T &b)
		{ return *this = *this * b; }
		vec_t& operator /= (const T &b)
		{ return *this = *this / b; }

		T dot(const vec_t &b) const
		{ return x * b.x + y * b.y; }
		T cross(const vec_t &b) const
		{ return x * b.y - y * b.x; }
		vec_t normal() const
		{ return vec_t(-y, x); }
		vec_t norm() const
		{ return *this / len(); }
			
		T len2() const
		{ return x * x + y * y; }
		double len() const
		{ return sqrt((double)len2()); }

		pair<T, T> to_pair() const
		{ return pair<T, T>(x, y); }
		
		bool operator < (const vec_t &b) const
		{ return to_pair() < b.to_pair(); }
		bool operator > (const vec_t &b) const
		{ return to_pair() > b.to_pair(); }
		bool operator <= (const vec_t &b) const
		{ return to_pair() <= b.to_pair(); }
		bool operator >= (const vec_t &b) const
		{ return to_pair() >= b.to_pair(); }
		bool operator == (const vec_t &b) const
		{ return to_pair() == b.to_pair(); }
		bool operator != (const vec_t &b) const
		{ return to_pair() != b.to_pair(); }

		string to_string() const
		{ ostringstream o; o << "(" << x << ", " << y << ")"; return o.str(); }
		friend ostream& operator << (ostream& o, const vec_t &a)
		{ return o << a.to_string(); }
	};
}

typedef geom::vec_t<LD> vec_t;
bool ints(int a, int b, int c, int d)
{
	return a < d && c < b;
}

void solve(int test)
{
	int n; cin >> n;
	int w, h;
	cin >> w >> h;

	vector<pii> r(n);
	for(int i = 0; i < n; ++i)
	{
		scanf("%d", &r[i].X);
		r[i].Y = i;
	}

	sort(r.rbegin(), r.rend());
	//random_shuffle(r.begin(), r.end());

	vector<pii> p;
	vector<pii> s;
	s.pb(mp(0, 0));
	int cur_x = 0;
	int cur_y = 0;
	for(int i = 0; i < n; )
	{
		vector<pii> add;
		cur_x = 0;
		int pi = i;
		vector<pii> zz;
		while(i < n)
		{
			int pos = upper_bound(s.begin(), s.end(), mp(cur_x, inf)) - s.begin() - 1;

			int h = s[pos].Y;

			int cx, cy;
			if(cur_x == 0)
				cx = 0;
			else
				cx = cur_x + r[i].X;
			if(h == 0)
				cy = 0;
			else
				cy = h + r[i].X;

			if(cx > w)
				break;

			add.pb(mp(cx, cy));
			zz.pb(mp(cur_x, cy + r[i].X));
			int j = i;
			++i;
			
			if(cx + r[j].X > w) break;
			cur_x = cx + r[j].X;
		}

		p.insert(p.end(), add.begin(), add.end());
		s = zz;
		// s.clear();
		// for(int j = 0; j < add.size(); ++j)
		// {
		// 	s.pb(mp(max(add[j].X - r[pi + j].X, 0), add[j].Y + r[pi + j].X));
		// }

		//--i;
		
		
	}

	
	// for(int i = 0; i < p.size(); ++i)
	// 	for(int j = i + 1; j < p.size(); ++j)
	// 		if(ints(p[i].X - r[i].X, p[i].X + r[i].X,
	// 				p[j].X - r[j].X, p[j].X + r[j].X) &&
	// 		   ints(p[i].Y - r[i].Y, p[i].Y + r[i].Y,
	// 				p[j].Y - r[j].Y, p[j].Y + r[j].Y))
	// 		{
	// 			dbg(test);
	// 			cerr << i << " " << j << endl;
	// 			assert(false);
	// 		}
	assert(p.size() == n);
	vector<pii> z(n);
	for(int i = 0; i < n; ++i)
		z[r[i].Y] = p[i];
	cout << "Case #" << test << ":";
	for(int i = 0; i < p.size(); ++i)
		cout << " " << z[i].X << " " << z[i].Y;
	cout << endl;
	
}

int main()
{
	//freopen("input.txt", "r", stdin); //freopen("output.txt", "w", stdout);
	//freopen(NAME ".in","r",stdin);freopen(NAME ".out","w",stdout);

	int tests; cin >> tests;
	for(int t = 1; t <= tests; ++t)
		solve(t);

	return 0;
}
/*************************
*************************/
#endif

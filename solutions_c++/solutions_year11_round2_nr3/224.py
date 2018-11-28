/*
 * Template for code jam - different includes and templates
 * Real task code is in the end
 * Mikhail Dektyarow <mihail.dektyarow@gmail.com>, 2009
 */
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <climits>
#include <cassert>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <sstream>
#include <numeric>
#include <stack>
#include <bitset>
#include <iostream>
#include <string>
#include <list>
using namespace std;

/*
 * DEFINES
 */
#define FOR(i, a, b) for (int i(a), _b(b); i <= _b; ++i)
#define FORD(i, a, b) for (int i(a), _b(b); i >= _b; --i)
#define REP(i, n) for (int i(0), _n(n); i < _n; ++i)
#define REPD(i, n) for (int i((n)-1); i >= 0; --i)
#define ALL(c) (c).begin(), (c).end()
#define SIZE(X) ((int)(X.size()))
#define LENGTH(X) ((int)(X.length()))

/*
 * Types
 */
typedef pair<int,int> ipair;
typedef long long int int64;
typedef unsigned long long uint64;

/*
 * Different useful templates
 */
template<typename T> void remin(T& a, const T& b) { if (b < a) a = b; }
template<typename T> void remax(T& a, const T& b) { if (b > a) a = b; }
template<class T1, class T2>inline istream& operator>> (istream& s, pair<T1, T2> &p) {	return s >> p.first >> p.second;}
template<class T1, class T2>inline ostream& operator<< (ostream& s, const pair<T1, T2>p) {	return s << "(" << p.first << " " << p.second << ")";}
template<class T1>inline ostream& operator<< (ostream& s, const vector<T1> container) {
	for (typename vector<T1>::const_iterator i = container.begin(); i != container.end(); i++) s << *i << " ";
	return s;
}
template<class T1>inline ostream& operator<< (ostream& s, const list<T1> container) {
	for (typename list<T1>::const_iterator i = container.begin(); i != container.end(); i++) s << *i << " ";
	return s;
}
template<class T1>inline istream& operator>> (istream&s, vector<T1> &container) {
	for (typename vector<T1>::iterator i = container.begin(); i != container.end(); i++) s >> *i;
	return s;
}
/*
 * Euclide's algorithm
 */
template<class T> inline T euclide(T a,T b,T &x,T &y)
  {if(a<0){T d=euclide(-a,b,x,y);x=-x;return d;}
   if(b<0){T d=euclide(a,-b,x,y);y=-y;return d;}
   if(b==0){x=1;y=0;return a;}else{T d=euclide(b,a%b,x,y);T t=x;x=y;y=t-(a/b)*y;return d;}}
/*
 * Factorizing a number
 */
template<class T> inline vector<pair<T,int> > factorize(T n)
{vector<pair<T,int> > R;for (T i=2;n>1;){if (n%i==0){int C=0;for (;n%i==0;C++,n/=i);R.push_back(make_pair(i,C));}i++;if (i>n/i) i=n;}if (n>1) R.push_back(make_pair(n,1));return R;}
template<class T> inline bool isPrimeNumber(T n)
  {if(n<=1)return false;for (T i=2;i*i<=n;i++) if (n%i==0) return false;return true;}
//Searching prime numbers
//Using Sieve of Atkin (http://en.wikipedia.org/wiki/Sieve_of_Atkin)
vector<int> gen_primes(int limit) {
	int sqr_lim;
	int x2, y2;
	int n;
	vector<bool> is_prime(limit+1, false);
	sqr_lim = (int)sqrt((long double)limit);
	is_prime[2] = true;
	is_prime[3] = true;
	x2 = 0;
	for (int i = 1; i <= sqr_lim; i++) {
		x2 += 2 * i - 1;
		y2 = 0;
		for (int j = 1; j <= sqr_lim; j++) {
			y2 += 2 * j - 1;
			n = 4 * x2 + y2;
			if ((n <= limit) && (n % 12 == 1 || n % 12 == 5))
				is_prime[n] = !is_prime[n];
			n -= x2;
			if ((n <= limit) && (n % 12 == 7))
				is_prime[n] = !is_prime[n];
			n -= 2 * y2;
			if ((i > j) && (n <= limit) && (n % 12 == 11))
				is_prime[n] = !is_prime[n];
		}
	}
	for (int i = 5; i <= sqr_lim; i++) {
		if (is_prime[i]) {
			n = i * i;
			for (int j = n; j <= limit; j += n) {
				is_prime[j] = false;
			}
		}
	}
	int primes_count = 0;
	for (int i = 2; i < limit; i++) primes_count += is_prime[i];
	vector<int> primes;
	primes.reserve(primes_count);
	for (int i=2; i < limit; i++) if (is_prime[i]) primes.push_back(i);
	return primes;
}
//Translating string to different types
template<class T> string toString(T n){ostringstream ost;ost<<n;ost.flush();return ost.str();}//NOTES:toString(
int toInt(string s){int r=0;istringstream sin(s);sin>>r;return r;}//NOTES:toInt(
int64 toInt64(string s){int64 r=0;istringstream sin(s);sin>>r;return r;}//NOTES:toInt64(
double toDouble(string s){double r=0;istringstream sin(s);sin>>r;return r;}//NOTES:toDouble(

/*
 * Real code
 */

int between(int a, int b, int c, int N) {
	if (b > a) {
		return (c > a) && (c < b);
	}
	return (c > a) || (c < b);
}

int get_next_vertex(int prev, int cur, vector<ipair> walls, int N) {
	int r;
	r = cur;
	REP(i, walls.size()) {
		if (walls[i].first == cur) {
			int cand;
			cand = walls[i].second;
			if (between(r, prev, cand, N)) {
				r = cand;
			}
		}
		if (walls[i].second == cur) {
			int cand;
			cand = walls[i].first;
			if (between(r, prev, cand, N)) {
				r = cand;
			}
		}
	}
	return r;
}

list<vector<int> > get_all_colorings(vector<int> start, int n, int N) {
	if (n == N) {
		return list<vector<int> > (1, start);
	}
	list<vector<int> > result;
	REP(i, 8) {
		bool ok;
		ok = false;
		REP(j, n) {
			if (start[j] >= i-1) {
				ok = true;
			}
		}
		if (!ok) {
			continue;
		}
		start[n] = i;
		list<vector<int> > tmp;
		tmp = get_all_colorings(start, n+1, N);
		result.splice(result.begin(), tmp);
	}
	return result;
}

int coloring_ok(vector<int> coloring, vector<vector<int> > &rooms) {
	int colors;
	colors = *max_element(coloring.begin(), coloring.end());
	REP(room, rooms.size()) {
		REP(color, colors + 1) {
			bool ok;
			ok = false;
			REP(point, rooms[room].size()) {
				if (coloring[rooms[room][point]] == color) {
					ok = true;
					break;
				}
			}
			if (!ok) {
				return -1;
			}
		}
	}
	return colors;
}

int main(void) {
	int __number_of_cases;
	cin >> __number_of_cases;
	REP(__number_of_case, __number_of_cases) {
		int N, M;
		cin >> N >> M;
		vector<ipair> walls(M + N);
		REP(i, M) {
			cin >> walls[i].first;
			--walls[i].first;
		}
		REP(i, M) {
			cin >> walls[i].second;
			--walls[i].second;
		}
		for (int i = M; i < M+N; ++i) {
			walls[i].first = i-M;
			walls[i].second = (i - M + 1) % N;
		}
		vector<vector<int> > rooms;
		REP(i, N) {
			REP (j, M+N) {
				if (walls[j].first == i) {
					vector<int> room;
					room.push_back(i);
					int cur, next;
					int tmp;
					cur = i;
					next = walls[j].second;
					while (next != i) {
						room.push_back(next);
						tmp = next;
						next = get_next_vertex(cur, next, walls, N);
						cur = tmp;
					}
					sort(room.begin(), room.end());
					rooms.push_back(room);
				}
			}
		}
		sort(rooms.begin(), rooms.end());
		rooms.resize(unique(rooms.begin(), rooms.end()) - rooms.begin());
		list<vector<int> > colorings;
		colorings = get_all_colorings(vector<int> (N), 1, N);
		int result;
		result = -1;
		list<vector<int> >::iterator best = colorings.begin();
		for (list<vector<int> >::iterator coloring = colorings.begin(); coloring != colorings.end(); ++coloring) {
			int tmp;
			tmp = coloring_ok(*coloring, rooms);
			//cout << *coloring << "\n" << tmp << "\n";
			if (tmp > result) {
				result = tmp;
				best = coloring;
			}
		}
		cout << "Case #" << __number_of_case+1 << ": " << (result + 1) << "\n";
		REP(i, N) {
			cout << ((*best)[i]+1) << " ";
		}
		cout << "\n";
	}
}

#include <iostream>
#include <istream>
#include <ostream>
#include <fstream>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <string>
#include <cstring>
#include <functional>
#include <deque>
#include <queue>
#include <set>
#include <map>
#include <cstdio>

using namespace std;

/////////types
typedef long long ll;
typedef vector<int> vi;
typedef vector<string> vs;
typedef vector<long long> vll;
typedef pair<double, double> dpt;
typedef pair<double, double> ipt;


////constants
static const double PI = acos(-1.0);
static const double LOW_BOUND = -100000000.0;
static const double UPPER_BOUND = 100000000.0;
static const dpt NULL_PT = dpt(LOW_BOUND, LOW_BOUND);
static const double EPS = 1E-9;

//////// compositions

static inline int get_c0(int j){return j >= 0 ? 1 : 0;}
static inline int get_c1(int j){return j >= 1 ? j : 0;}
static inline int get_c2(int j){return j >= 2 ? (j*(j-1)) >> 1 : 0;}
static inline int get_c3(int j){return j >= 3 ? (j*(j-1)*(j-2))/6 : 0;}

/////power 2
static inline long long two(int n){return 1 << n;}
////
template<class T>
static inline void check_max(T& a, T b){if(a < b) a = b;}
template<class T>
static inline void check_min(T& a, T b){if(a > b) a = b;}

//////// primes
#define PRIME_UPPER 100001
static bool p[PRIME_UPPER];
static deque<int>p_queue;

static inline void init_prime()
{
	p[0] = false; p[1] = false; p[2] = true;
	p_queue.push_back(2);
	for(int i = 3; i < PRIME_UPPER; i++)
	{
		bool found = false;
		for(deque<int>::iterator pIt = p_queue.begin(); pIt != p_queue.end(); pIt++)
		{
			int val = *pIt;
			if(val * val > i){
				p[i] = true;
				break;
			}

			if(i % val == 0){
				p[i] = false;
				found = true;
				break;
			}
		}
		if(!found) {
			p[i] = true;
			p_queue.push_back(i);
		}
	}
}


/////////gcd
template <class T>
static T gcd(T m, T n)
{
	if(n == 0)return m;
	else return gcd(n, m % n);
}

///////// lcm
template <class T>
static inline T lcm(T m, T n)
{
	if(m == 0 || n == 0)return 0;
	T gd = gcd(m, n);
	return m * n / gd;
}

/////// 2D linear array derive
template <class T>
struct Matrix
{
	T d1,d2,d3,d4;
	Matrix(T dd1 = 0, T dd2 = 0, T dd3 = 0, T dd4 = 0):d1(dd1), d2(dd2), d3(dd3), d4(dd4){}
	Matrix(const T& other):d1(other.d1), d2(other.d2), d3(other.d3), d4(other.d4){}
	Matrix<T> operator* (const Matrix<T>& m2) const
	{
		Matrix<T> new_matrix(0,0,0,0);
		new_matrix.d1 = d1 * m2.d1 + d2 * m2.d3;
		new_matrix.d2 = d1 * m2.d2 + d2 * m2.d4;
		new_matrix.d3 = d3 * m2.d1 + d4 * m2.d3;
		new_matrix.d4 = d3 * m2.d2 + d4 * m2.d4;
		return new_matrix;
	}
};

template <class T>
static Matrix<T> get_coeff(Matrix<T>& base, int n)
{
	Matrix<T> result(1,0,0,1);
	Matrix<T> power(base);

	while(n != 0)
	{
		if((n & 1) != 0){
			result = result * power;
		}
		n >>= 1;
		power = power * power;
	}
	return result;
}

template <class T>
static T derive_result(T coff1, T coff2, T init1, T init2, int n)
{
	if(n == 0)return init2;
	if(n == 1)return init1;
	Matrix<T> base(coff1, coff2, 1, 0);
	Matrix<T> n_coeff = get_coeff(base, n-1);
	return init1 * n_coeff.d1 + init2 * n_coeff.d2;
}

////triangle area 
template <class T>
static inline T get_tri_area(pair<T, T> p1, pair<T, T> p2, pair<T, T> p3)
{
	T result = p1.first * p2.second + p2.first * p3.second + p3.first * p1.second
		- p1.first * p3.second - p2.first * p1.second - p3.first * p1.second;
	if(result < 0)result = -result;
	return result /2.0;
}

typedef struct Triple{
	int x;
	int y;
	int d;
	Triple(int a, int b, int c):x(a), y(b), d(c){}
}Tp;

////the extend Euclid-Function
static Tp ex_euclid(int a, int b)
{
	if(b == 0)return Triple(1,0,a);
	Triple t = ex_euclid(b, a % b);
	return Triple(t.x, t.x - (a/b)*t.y, t.d);
}

///solve the linear modular equation
/// solve ax = b(mod n)
static vector<int> modular_solve(int a, int b, int n) 
{
	Tp t = ex_euclid(a, n);
	if(b % t.d == 0){
		int x0 = (t.x *(b/t.d)) % n;
		vector<int> res;

		int temp = n / t.d;
		for(int i = 0; i < t.d; i++)
			res.push_back((x0 + i * temp) % n);
	}else{
		return vector<int>();
	}
}

////power n of x
template<class T>
static inline T power(T x, int n)
{
	T res = 1;
	while(n != 0){
		if((n & 1) == 0)
		{
			res *= x;
		}
		x *= x;
		n >>= 1;
	}
	return res;
}


///////segment intersection
static inline int direct(dpt p1, dpt p2, dpt p3)
{
	return (p2.first - p1.first) *( p3.second - p1.second) - (p2.second - p1.second)* (p3.first - p1.first);
}
static inline bool on_seg(dpt p1, dpt p2, dpt p3)
{
	return min(p1.first, p2.first) <= p3.first &&
			max(p1.first, p2.first) >= p3.first	 &&
			min(p1.second, p2.second) <= p3.second &&
			max(p1.second, p2.second) >= p3.second ;
}
static inline double get_k(dpt p1, dpt p2)
{
	return (p1.second - p2.second) / (p1.first - p2.first);
}

static dpt seg_inter(dpt p1, dpt p2, dpt p3, dpt p4)
{
	int d1 = direct(p3,p4,p1);
	int d2 = direct(p3,p4,p2);
	int d3 = direct(p3,p4,p3);
	int d4 = direct(p3,p4,p4);

	if(((d1 > 0 && d2 < 0)||(d2 > 0 && d1 < 0))&&
		((d3 > 0 && d4 < 0)||(d4 > 0 && d3 < 0))){
			double x0 = fabs(p1.first - p2.first) < EPS? p1.first : 
				fabs(p3.first - p4.first) < EPS? p3.first: LOW_BOUND;
			if(fabs(x0 - LOW_BOUND) < EPS){
				double k1 = get_k(p1, p2);
				double k2 = get_k(p3, p4);
				x0 = (p3.second - p1.second + p1.first * k1 - p3.first * k2) /(k1 - k2);
			}

			double y0 = fabs(p1.second - p2.second) < EPS? p1.second: 
				fabs(p3.second - p4.second) < EPS? p3.second: LOW_BOUND;
			if(fabs(y0 - LOW_BOUND) < EPS){
				double k1 = get_k(p1, p2);
				y0 = k1 * (x0 - p1.first) - p1.second;
			}
			return dpt(x0, y0);

	}else if(d1 == 0 && on_seg(p3, p4, p1)){
		return p1;
	}else if(d2 == 0 && on_seg(p3, p4, p2)){
		return p2;	
	}else if(d3 == 0 && on_seg(p1, p2, p3)){
		return p3;
	}else if(d4 == 0 && on_seg(p1, p2, p4)){
		return p4;
	}
	return NULL_PT;
}


/////segment tree
template<class T , int sz>
class PointTree{
	T max_val[sz << 1];
	int size;

	T find_max(int a, int b, int lower, int upper){
		if(a == b){
			return max_val[a + sz];
		}else{
			int mid = (lower + upper) >> 1;
			if(a > mid){
				return find_max(a, b, mid + 1, upper);
			}else if(b <= mid){
				return find_max(a, b, lower, mid);
			}else{
				T res = find_max(a, mid, lower, mid);
				check_max(res, find_max(mid + 1, b, mid+1, upper));
				return res;
			}
		}
	}

public:
	PointTree():size(0)
	{
		memset(max_val, -1, sizeof(max_val));
	}

	PointTree(vector<int> point):size(0){
		memset(max_val, -1, sizeof(max_val));
		for(int i = 0; i < point.size(); i++)
			insert(point[i], i);
	}

	///insert a value on the position n
	void insert(int val, int n)
	{
		int i = sz + n;
		size++;
		for(max_val[i] = val; i > 1; i >>= 1)
			check_max(max_val[i >> 1], val);

	}

	void del(int n)
	{
		int i = sz + n;
		size--;
		max_val[i] = -1;
		for(i >>= 1; i >= 1; i >>= 1)
			check_max(max_val[i << 1], max_val[(i<<1) + 1]);

	}

	T count(int a, int b)
	{
		if(a > b)swap(a, b);
		return find_max(a, b, 0, sz - 1);
	}

};

static ifstream in("in.txt");
static ofstream out("out.txt");

int a[10001];
bool val[10001];
int M, V;
int dp[10001][2];
int half;
int solve(int num, int des_val)
{
	if(dp[num][des_val] < 10001)return dp[num][des_val];

	if(num > half){
		return 0;
	}else if((num << 1) > half){
		bool res1 = val[num << 1]  && val[(num << 1) + 1] ;
		bool res2 = val[num << 1]  || val[(num << 1) + 1] ;

		
		if(des_val == 1){
			if(res1)dp[num][des_val] = 0;
			else if(res2 && a[num] == 0)dp[num][des_val] = 0;
			else if(val[num] == 1 && res2)dp[num][des_val] = 1;
			else dp[num][des_val] = 10001;
		}else{
			if(!res2)dp[num][des_val] = 0;
			else if(!res1 && a[num] == 1)dp[num][des_val] = 0;
			else if(val[num] == 1 && !res1)dp[num][des_val] = 1;
			else dp[num][des_val] = 10001;
		}
	}else if ((num << 1) > half - 1){
		int x = val[(num << 1) + 1];
		if(des_val == 0)
		{
			if(a[num] == 1){
				if(x == 1){
					check_min(dp[num][des_val], solve(num << 1, 0));
				}else{
					dp[num][des_val] = 0;
				}
			}else{
				if(x == 1){
					if(val[num] == 1)check_min(dp[num][des_val], solve(num << 1, 0) + 1);
					else dp[num][des_val] = 10001;
				}else{
					check_min(dp[num][des_val], 0);
				}
			}
		}else{
			if(a[num] == 1){
				if(x == 1){
					check_min(dp[num][des_val], solve(num << 1, 1));
				}else{
					if(val[num] == 1){
						check_min(dp[num][des_val], solve(num << 1, 1) + 1);
					}else
						dp[num][des_val] = 10001;
				}
			}else{
				if(x == 1)dp[num][des_val] = 0;
				else{
					check_min(dp[num][des_val], solve(num << 1, 1));
				}
			}
		}
	}else{
		if(des_val == 0)
		{
			if(a[num] == 1){
				check_min(dp[num][des_val], solve(num << 1, 0) + solve((num << 1)+ 1, 0));
				check_min(dp[num][des_val], solve(num << 1, 1) + solve((num << 1)+ 1, 0));
				check_min(dp[num][des_val], solve(num << 1, 0) + solve((num << 1)+ 1, 1));
			}else{
				check_min(dp[num][des_val], solve(num << 1, 0) + solve((num << 1)+ 1, 0));
				if(val[num] == 1){
					check_min(dp[num][des_val], solve(num << 1, 1) + solve((num << 1)+ 1, 0) + 1);
					check_min(dp[num][des_val], solve(num << 1, 0) + solve((num << 1)+ 1, 1) + 1);
				}
			}
		}else{
			if(a[num] == 1){
				check_min(dp[num][des_val], solve(num << 1, 1) + solve((num << 1)+ 1, 1));
				if(val[num] == 1){
					check_min(dp[num][des_val], solve(num << 1, 1) + solve((num << 1)+ 1, 0) + 1);
					check_min(dp[num][des_val], solve(num << 1, 0) + solve((num << 1)+ 1, 1) + 1);
				}
			}else{
				check_min(dp[num][des_val], solve(num << 1, 1) + solve((num << 1)+ 1, 1));
				check_min(dp[num][des_val], solve(num << 1, 1) + solve((num << 1)+ 1, 0));
				check_min(dp[num][des_val], solve(num << 1, 0) + solve((num << 1)+ 1, 1));
			}
		}
	}


	return dp[num][des_val];
}


static void process_case(int num)
{

	in >> M >> V;
	memset(a, -1, sizeof(a));
	half = (M-1)/2;
	for(int i = 1; i <= half; i ++)
		in >> a[i] >> val[i];

	for(int i = half + 1; i <= M; i++)
		in >> val[i];
	for(int i = 1; i <= M; i++){
		dp[i][0] = 10001;
		dp[i][1] = 10001;
	}

	int x = solve(1, V);

	out << "Case #" <<num << ": ";
	if(x < 10001){
		out << x <<endl;
	}else{
		out << "IMPOSSIBLE" <<endl;
	}
}



int main()
{
	int num;
	init_prime();
	in >> num;
	for(int i = 1; i <= num; i++)
		process_case(i);


}



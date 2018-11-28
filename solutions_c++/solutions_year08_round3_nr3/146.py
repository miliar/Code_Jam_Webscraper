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

//////// compositions

static inline int get_c0(int j){return j >= 0 ? 1 : 0;}
static inline int get_c1(int j){return j >= 1 ? j : 0;}
static inline int get_c2(int j){return j >= 2 ? (j*(j-1)) >> 1 : 0;}
static inline int get_c3(int j){return j >= 3 ? (j*(j-1)*(j-2))/6 : 0;}

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
static inline T gcd(T m, T n)
{
	if(m == 0 || n == 0)return 0;
	if(m > n)swap(m, n);
	while(m != 0){
		n %= m;
		if(m > n)swap(m, n);
	}
	return n;
}

///////// gcp
template <class T>
static inline T gcp(T m, T n)
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


static ifstream in("in.txt");
static ofstream out("out.txt");
/*
static void process_case(int num)
{

	int P, K, L;
	/////input here
	in >> P >> K >> L;

	priority_queue<long long, deque<long long>, less<long long> > letters;
	for(int i = 0; i < L; i++)
	{
		long long t;
		in >> t;
		letters.push(t);
	}

	long long count = 0;
	long long k_count = K;
	long long stroke  = 1;
	//// process here
	while(!letters.empty())
	{
		long long time = letters.top();
		letters.pop();
		count += time * stroke;
		k_count--;
		if(k_count == 0){
			k_count = K;
			stroke++;
		}
	}


	out << "Case #" <<num << ": ";
	/////output here
	out << count <<endl;
}
*/

static long long A[100];
static long long mark[500000];
static long long TAG = 1000000007;
static void process_case(int num)
{

	int n, m;
	long long X, Y, Z;
	/////input here
	vector<long long> seq;
	in >> n >> m >> X >> Y >> Z;
	seq.reserve(n);

	for(int i = 0; i < m; i++)
		in >> A[i];

	for(int i = 0; i < n; i++)
	{
		long long t = A[i%m];
		seq.push_back(t);
		A[i%m] = labs((X * t + Y * (i + 1))% Z);
	}
/*
	for(int i = 0; i < n; i++)
	seq.push_back(n - i);
*/	
	//// process here
	memset(mark, 0, sizeof(mark));
	mark[0] = 1;
	for(int i = 1; i < n; i++)
	{
		for(int j = 0; j < i; j++)
		{
			long long numi = seq.at(i);
			long long numj = seq.at(j);
			if(numi > numj) {
				mark[i] += mark[j];
				mark[i] %= TAG;
			}
		}
		mark[i]++;	///add itself
		
	}

	long long sum = 0;
	for(int i = 0; i < n; i++)
		sum += mark[i];


	out << "Case #" <<num << ": ";
	/////output here
	out << labs(sum % TAG) <<endl;
}


int main()
{
	int num;
	
	in >> num;
	for(int i = 1; i <= num; i++)
		process_case(i);


}























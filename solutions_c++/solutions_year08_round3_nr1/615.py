#define _CRT_SECURE_NO_WARNINGS

#define _USE_MATH_DEFINES
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <ctime>
#include <cfloat>
#include <climits>

#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <map>
#include <set>
#include <numeric>
#include <algorithm>
#include <iterator>
#include <functional>
#include <utility>
#include <complex>

#define PUSH(c, e)	c.push_back(e)
#define FOREACH(t,i,c)	for(t::iterator i = (c).begin(); i != (c).end(); ++i)
#define ALL(v)		(v).begin(), (v).end()
#define MP(x,y)		make_pair((x), (y))

#define FOR(i,a,b)	for(int i(a),_b(b); i <= _b; ++i)
#define FORD(i,a,b)	for(int i(a),_b(b); i >= _b; --i)
#define REP(i,n)	for(int i(0),_n(n); i < _n; ++i)
#define REPD(i,n)	for(int i((n)-1); i >= 0; --i)
#define FILL(a,c)	memset(&a, c, sizeof(a))

using namespace std;

typedef vector<int> int_v;
typedef vector<double> db_v;
typedef vector<string> str_v;
typedef long long int64;

bool double_eq(double a, double b) { return (b - DBL_EPSILON <= a) && (a <= b + DBL_EPSILON); }
bool double_ls(double a, double b) { return b - a > DBL_EPSILON; }
bool double_gt(double a, double b) { return a - b > DBL_EPSILON; }
double degree_to_radian(double degree) { return degree / 18.0 * M_PI; }
template<typename T> inline T sqr(T a) { return a*a; }

template<typename D, typename S> D cast(const S& s) {
	stringstream ss;
	D result;
	ss << s;
	ss >> result;
	return result;
}

template<typename T> inline void check_min(T& a, T b) { if (b < a) a = b; }
template<typename T> inline void check_max(T& a, T b) { if (b > a) a = b; }

#define MAXN 100
#define MAXP 1000
#define MAXK 1000
#define MAXL 1000

void print_case(int no)
{
	printf("Case #%d: ", no);
}

void example()
{
	int_v v;
	FOR(i,10,20) { PUSH(v, i); }
	FOREACH(int_v, i, v) { printf("%d\n", *i); }
}

struct letter_t
{
	int count;
	//int index; // 본래 index
};

bool letter_index_greater ( const letter_t& elem1, const letter_t& elem2 )
{
   return elem1.count > elem2.count;
}

int main(int argc, char* argv[])
{
	//freopen("input.txt", "rt", stdin);
	//freopen("output.txt", "wt", stdout);
    //freopen("a-small.in","r",stdin);
    //freopen("a-small.out","w",stdout);
    //freopen("a-large.in","r",stdin);
    //freopen("a-large.out","w",stdout);

	int N, P, K, L;
	letter_t letter[MAXL]; // 정렬을 위한 ( 정렬키 : 카운트, 덩달아 : 인덱스 )
	int result;

	scanf("%d", &N);

	REP(i, N)
	{
		scanf("%d%d%d", &P, &K, &L);
		REP(i, L)
			scanf("%d", &letter[i].count);

		// Solve
		{
			result = 0;
			int touch = 1;

			// 1. 각 letters 를 count 대로 정렬(내림차순)
			sort(letter, letter+L, letter_index_greater);		

			// 2. 가장 count 가 많은 letters 부터
			for(int j=0; j<L; j+=K)
			{
				// 2.1. K 개 만큼은 1씩 가산
				for(int k=0; k<K; ++k)
				{
					if(j+k >= L)
						break;

					result += letter[j+k].count * touch;
				}

				++touch; // 터치횟수가 늘어간다.
			}
		}

		print_case(i+1);
		printf("%d\n", result);
	}

	return 0;
}

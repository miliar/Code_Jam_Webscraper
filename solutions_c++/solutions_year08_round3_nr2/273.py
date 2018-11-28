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

void print_case(int no)
{
	printf("Case #%d: ", no);
}

#define MAXSTRING 40

bool is_ugly(long long value)
{
	// 2, 3, 5, 7 로 나뉨 ?
	return (value == 0 || value % 2 == 0 || value % 3 == 0 || value % 5 == 0 || value % 7 == 0);
}

// buho 는 두의 부호며, start 는 당장 계산할 시작위치
// return ugly exp
int solve(char *str, int len, int start = 0, int buho = +1, long long value = 0)
{
	if(start >= len)
	{
		// 진정으로 판단(ugly여부) 그래서 1 를 리턴
		//if(buho == +1)
		//	cout << value << " is ugly : " << ((buho == +1) && is_ugly(value)) << endl;
		return (buho == +1) && is_ugly(value) ? 1 : 0;
	}

	int result = 0;

	// 나눌크기
	for(int part_len=1; part_len<=(len-start); ++part_len)
	{
		// 일단 앞 숫자를 계산(start ~ start+part_len-1)
		char save = str[start+part_len];
		str[start+part_len] = 0;
		long long new_value = value + buho * cast<int64>(/*part*/str+start);
		str[start+part_len] = save;

		result += solve(str, len, start + part_len, +1, new_value); // +
		result += solve(str, len, start + part_len, -1, new_value); // -
	}

	//printf("\n");

	// +, -, 혹은 len-1(끝) 경우 start ~ i-1 까지를 더함
	return result;
}

int main(int argc, char* argv[])
{
	//freopen("input.txt", "rt", stdin);
	//freopen("output.txt", "wt", stdout);
    //freopen("a-small.in","r",stdin);
    //freopen("a-small.out","w",stdout);
    //freopen("a-large.in","r",stdin);
    //freopen("a-large.out","w",stdout);

	int N;
	char str[MAXSTRING+2];
	int result;
	scanf("%d", &N);

	REP(i, N)
	{
		// input
		scanf("%s", str);

		result = solve(str, strlen(str));

		// result
		print_case(i+1);
		printf("%d\n", result);
	}

	return 0;
}

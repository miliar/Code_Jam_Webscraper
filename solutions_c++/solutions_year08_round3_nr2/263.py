#define _CRT_SECURE_NO_WARNINGS

#include <map>
#include <set>
#include <cmath>
#include <queue>
#include <vector>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <numeric>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <ctime>
using namespace std;

//typedef long long int64;
typedef vector<int> vi;
typedef vector<string> vs;
typedef vector<double> vd;
typedef pair<int,int> pii;

#define For(i,a,b) for (int i(a),_b(b); i <= _b; ++i)
#define Ford(i,a,b) for (int i(a),_b(b); i >= _b; --i)
#define Rep(i,n) for (int i(0),_n(n); i < _n; ++i)
#define Repd(i,n) for (int i((n)-1); i >= 0; --i)
#define Fill(a,c) memset(&a, c, sizeof(a))
#define MP(x, y) make_pair((x), (y))
#define All(v) (v).begin(), (v).end()

template<typename T, typename S> T cast(S s) {
	stringstream ss;
	ss << s;
	T res;
	ss >> res;
	return res;
}

template<typename T> inline T sqr(T a) { return a*a; }
template<typename T> inline int Size(const T& c) { return (int)c.size(); }
template<typename T> inline void checkMin(T& a, T b) { if (b < a) a = b; }
template<typename T> inline void checkMax(T& a, T b) { if (b > a) a = b; }

char buf[1024];


int gcd(int a, int b);
long long eval(char *s, int len, int i);
int  npow(int a, int n);

int main() {

#ifndef  ONLINE_JUDGE
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
#endif

	gets(buf);
	int ncase = atoi(buf);
	For(nc,1,ncase) {
		gets(buf);
		int len = strlen(buf);

		int cnt = 0;
		int pow_3 = npow(3,len-1);
		for(int i=0; i<pow_3; i++)
		{
			long long value = eval(buf, len, i);
			int c = ((value % 210) + 210)%210;
			int ret = gcd(210, c); // 210=2*3*5*7 
			if ( ret != 1 || value == 0 )
				cnt++;
		}

		printf("Case #%d: %d\n", nc, cnt);
	}
}

int  npow(int a, int n)
{
	int  r = 1;
	Rep(i,n)
		r *= a;
	return  r;
}

long long eval(char *s, int len, int perm)
{
	// op : 0:none, 1:+, 2:-
	long long sum=0;
	int sign = 1;
	long long build = 0;
	Rep(i,len) {
		build = build*10 + s[i]-'0';
		int  op = perm%3;
		perm /= 3;
		if ( op == 0 )
			continue;
		else if ( op == 1 ) {
			sum += sign * build;
			sign = 1;
			build = 0;
		} else if ( op == 2 ) {
			sum += sign * build;
			sign = -1;
			build = 0;
		}
	}
	sum += sign * build;
	
	return  sum;
}

int gcd(int a, int b)
{
	if ( b == 0 )
		return  a;
	int  r = a % b;
	return  gcd(b,r);
}

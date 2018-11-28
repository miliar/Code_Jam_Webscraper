#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <list>
#include <deque>
#include <stack>
#include <queue>
#include <map>
#include <set>
#include <algorithm>
#include <functional>
#include <cmath>
#include <memory.h>

using namespace std;

typedef vector<int> VI;
typedef pair<int, int> PII;
typedef long long Int;

#define FOR(i, a, b) for(int i=a; i<b; ++i)
#define RFOR(i, a, b) for(int i=b-1; i>=a; --i)
#define FILL(a, val) memset(a, val, sizeof(a))

#define all(c) c.begin(), c.end()
#define sz(c) (int)c.size()
#define pb push_back

#define mp make_pair
#define X first
#define Y second

const double PI = acos(-1.0);
const int INF = 1000000000;

PII operator+(const PII & a, const PII & b){return PII(a.X+b.X, a.Y+b.Y);}
PII operator-(const PII & a, const PII & b){return PII(a.X-b.X, a.Y-b.Y);}
int dot_p(const PII & a, const PII & b){return a.X*b.X + a.Y*b.Y;}
int cross_p(const PII & a, const PII & b){return a.X*b.Y - a.Y*b.X;}

int to_int(string s){
	if (s == "")
		return 0;
	istringstream iss(s);
	int n;
	iss >> n;
	return n;
}

string to_str(int n){
	ostringstream oss;
	oss << n;
	return oss.str();
}
/*
int n;
int nn;
int a[28];
int b[28];

bool ch(int m)
{
	nn = 1;
	FILL(b, -1);
	FOR(i, 0, n-1)
		if ((m & (1<<i)) != 0)
		{
			a[nn] = i+2;
			b[i+2] = nn;
			++nn;
		}
	FOR(i, 1, nn)
	{
		int p = a[i];
		while (p != -1 && p!=1)
		{
			p = b[p];
		}
		if (p == -1)
			return false;
		else
			return true;
	}
}
*/

int c[502][502];

int d[503][503];
int f(int len, int last)
{
	if (d[len][last] == -1)
	{
		if (len < 1)
			return 0;
		if (len>=last)
			return 0;
		if (len == 1)
			return 1;
		int res = 0;
		FOR(i, 1, len)
		{
			if (f(i, len) > 0 && c[last-len-1][len-i-1] > 0)
			{
				res = (res+ ((Int)f(i, len)*c[last-len-1][len-i-1])%100003)%100003;
			}
		}
		d[len][last] = res;
	}
	return d[len][last];
}

int main(){
	//freopen("input.txt", "r", stdin);
	//freopen("output.txt", "w", stdout);

	//freopen("C-small-attempt0.in", "r", stdin);
	//freopen("A-small-attempt0.out", "w", stdout);

	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);
	
	FILL(c, 0);
	FOR(n, 0, 501)
	{
		c[n][0] = 1;
	}
	//c[0][0] = 1;
	//c[1][1] = 1;
	FOR(n, 1, 501)
		FOR(k, 1, 501)
			c[n][k] = (c[n-1][k-1] + c[n-1][k])%100003;
	FILL(d, -1);
		FOR(i, 1, 501)
			FOR(j, 2, 501)
				f(i, j);
	int T;
	scanf("%d", &T);
	FOR(t, 0, T)
	{
		int n;
		scanf("%d", &n);
		/*int res = 0;
		FOR(l, 1, n)
		{
			FOR(last, l+1, n+1)
			{
				if (ch(l, last))
					res ++;
			}
			
		}
		*/
		

		int res = 0;
		FOR(i, 1, n)
			res = (res + f(i , n))%100003;
		printf("Case #%d: %d", t+1, res);		
		if (t != T-1)
			printf("\n");
	}

	return 0;
}
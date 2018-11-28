#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
#include <map>
#include <list>
#include <cmath>
#include <sstream>
#include <algorithm>
#include <ctime>

using namespace std;

#define FOR(i, a, b) for (int i = (a); i < (b); i++)
#define FOD(i, a, b) for (int i = (a); i >= (b); i--)
#define REP(i, a) for (int i = 0; i < (a); i++)
#define sz(a) ((int)a.size())
#define cl clear()
#define mp make_pair
#define pb push_back
#define X first
#define Y second
#define ALL(a) a.begin(), a.end()
#define sqr(a) ((a)*(a))

typedef long long ll;

class ln{
	public:
		int a[10000];
		int k;
		ln()
		{
			memset(a, 0, sizeof(a));
			k = 0;
		}
		ln(int x)
		{
			memset(a, 0, sizeof(a));
			k = 0;
			while (x > 0)
			{
				a[k++] = x % 10;
				x /= 10;
			}
		}
		ln operator * (int x)
		{
			ln rt;
			int t = 0;
			REP(i, k)
			{
				t = t + a[i] * x;
				rt.a[i] = t % 10;
				t /= 10;
			}
			rt.k = k;
			while (t > 0)
			{
				rt.a[rt.k++] = t % 10;
				t /= 10;
			}
			return rt;
		}
		ln& operator *= (int x)
		{
			int t = 0;
			REP(i, k)
			{
				t = t + a[i] * x;
				a[i] = t % 10;
				t /= 10;
			}
			while (t > 0)
			{
				a[k++] = t % 10;
				t /= 10;
			}
			return *this;
		}
		ln operator + (ln& b)
		{
			ln rt;
			rt.k = max(k, b.k);
			int t = 0;
			REP(i, rt.k)
			{
				t = t + a[i] + b.a[i];
				rt.a[i] = t % 10;
				t /= 10;
			}
			while (t > 0)
			{
				rt.a[rt.k++] = t % 10;
				t /= 10;
			}
			return rt;
		}
		ln& operator += (ln& b)
		{
			k = max(k, b.k);
			int t = 0;
			REP(i, k)
			{
				t = t + a[i] + b.a[i];
				a[i] = t % 10;
				t /= 10;
			}
			while (t > 0)
			{
				a[k++] = t % 10;
				t /= 10;
			}
			return *this;
		}
		void output(FILE* stream = stdout)
		{
			while (k >= 0 && a[k - 1] == 0)
				k--;
			if (k == 0)
			{
				fprintf(stream, "0");
				return;
			}
			FOD(i, k - 1, 0)
				fprintf(stream, "%d", a[i]);
		}
};

bool w[256];
int v[256];

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int t;
	scanf("%d\n", &t);
	ln tmp;
	REP(k, t)
	{
		string s;
		getline(cin, s);
		if (sz(s) == 1)
		{
			printf("Case #%d: 1\n", k + 1);
			continue;
		}
		memset(w, 0, sizeof(w));
		memset(v, 0, sizeof(v));
		w[s[0]] = 1;
		v[s[0]] = 1;
		int bs = 2;
		s[0] = 1;
		bool nn = true;
		FOR(i, 1, sz(s))
			if (!w[s[i]])
			{
				if (nn)
				{
					w[s[i]] = 1;
					v[s[i]] = 0;
					s[i] = 0;
					nn = false;
				}
				else
				{
					w[s[i]] = 1;
					v[s[i]] = bs;
					s[i] = bs++;
				}
			}
			else
				s[i] = v[s[i]];
//		cerr << bs << endl;
		ln ans;
		ln aa = ln(1);
		reverse(ALL(s));
		REP(i, sz(s))
		{
//			cerr << "Bit: " << (char)(s[i] + '0') << endl;
			tmp = aa * (int)s[i];
			ans += tmp;
			aa *= bs;
//			cerr << "Curr ans: ";
//			ans.output(stderr);
//			cerr << endl;
//			cerr << "Curr b^x: ";
//			aa.output(stderr);
//			cerr << endl;
		}
		printf("Case #%d: ", k + 1);
		ans.output();
		printf("\n");
	}
	return 0;
}

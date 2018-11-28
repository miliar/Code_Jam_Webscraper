#include <algorithm>
#include <cmath>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <vector>

using namespace std;

#define fore(i,a) for(int i = 0; i < (a); i++)
#define fort(i,a) for(typeof((a).begin()) i = (a).begin(); i != (a).end(); i++)
#define all(x) (x).begin(), (x).end()
#define pb push_back
#define mp make_pair
#define x first
#define y second

typedef pair<int,int> pi;
typedef vector<int> vi;
typedef long long ll;

#define err(...)
#define err(...) fprintf(stderr, __VA_ARGS__)

#define MOD 10009

struct s26
{
	int q[26];
	void get(char * x)
	{
		fore(i,26) q[i] = 0;
		for(int i = 0; x[i]; i++) q[x[i]-'a']++;
	}
	void out()
	{
		fore(i,26) printf("%d ", q[i]); printf("\n");
	}
};

s26 w[111];
int n,k;
char p[111], buf[111];
int res[111];
int fac[111];

int eval(s26 x)
{
	int res = 0, cur = 1;
	for(int i = 0; p[i]; i++)
		if(p[i] == '+')
		{
			res += cur;
			if(res >= MOD) res -= MOD;
			cur = 1;
		}
		else
		{
			cur = cur * x.q[p[i]-'a'] % MOD;
		}
	//x.out();
	//printf("eval = %d\n", res + cur);
	return res + cur;
}

int f(vi rec)
{
	ll res = fac[rec.size()];
	int cur = 1;
	for(int i = 1; i < rec.size(); i++)
		if(rec[i] == rec[i-1])
		{
			cur++;
		}
		else
		{
			res /= fac[cur];
			cur = 1;
		}
	return res / fac[cur];
}

void go(s26 cur, int last, int cnt, ll div, int cont)
{
	if(cnt > k) return;
	if(last == n)
	{
		res[cnt] += fac[cnt] / div * eval(cur) % MOD;
		if(res[cnt] >= MOD) res[cnt] -= MOD;
		return;
	}
	go(cur, last+1, cnt, div*fac[cont], 0);
	fore(i,26) cur.q[i] += w[last].q[i];
	//rec.pb(last);
	go(cur, last, cnt+1, div, cont+1);
}

void test()
{
	scanf(" %s%d%d", p, &k, &n);
	fore(i,k+1) res[i] = 0;
	fore(i,n)
	{
		scanf("%s", buf);
		w[i].get(buf);
	}
	go(s26(), 0, 0, 1, 0);
	for(int i = 1; i <= k; i++) printf("%d ", res[i]); printf("\n");
}

int main()
{
	fac[0] = 1;
	fac[1] = 1;
	for(int i = 2; i < 11; i++) fac[i] = fac[i-1] * i;
	int T;
	scanf("%d", &T);
	for(int tt = 1; tt <= T; tt++)
	{
		printf("Case #%d: ", tt);
		test();
	}
}

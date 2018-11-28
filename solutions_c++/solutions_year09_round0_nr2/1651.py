#include<iostream>
#include<cstdio>
#include<cctype>
#include<cmath>
#include<cstdlib>
#include<algorithm>
#include<vector>
#include<string>
#include<list>
#include<deque>
#include<map>
#include<set>
#include<queue>
#include<stack>
#include<utility>
#include<sstream>
#include<cstring>
#include <memory.h>
using namespace std;
typedef long long ll;
typedef unsigned long long ull;
typedef double dd;
typedef long double ld;
typedef vector <int > VI;
typedef vector < VI > VVI;
typedef vector < ll > VLL;
typedef vector < dd > VD;
typedef vector < string > VS;
typedef pair<int,int> PII;
typedef vector <PII> VPII;
typedef istringstream ISS;

#define VAR(V,init) __typeof(init) V=(init)
#define FOR(I,A,B) for(int I=(A);I<=(B);I++)
#define FORD(I,A,B) for(int I=(A);I>=(B);I--)
#define REP(I,N) for(int I=0;I<(N);I++)
#define FOREACH(I,C) for(VAR(I,(C).begin());I!=(C).end();I++)
#define ALL(X) (X).begin(),(X).end()
#define CLE(a,b) memset(a,b,sizeof(a))
#define MINN(a,b) ((a)>(b)?(b):(a))
#define MAXX(a,b) ((a)<(b)?(b):(a))
#define PB push_back
#define PF push_front
#define CB pop_back
#define CF pop_front
#define MP make_pair
#define FI first
#define SE second
#define SZ(X) ((int)(X.size()))
#define INF 1000000000
#define INFLL 1000000000000000000ll
int COND = 1000;
#define DB(x) ({if(COND){COND--; cerr << __LINE__ << " : " << #x << ": " << x << endl; };})
#define deb(A) //A
//////////////////

#define MAX_W 200
#define MAX_H 200

struct FindUnion
{
	int *f, *r;
	FindUnion(int n)
	{
		f = new int[n];
		r = new int[n];
		REP(i, n)
		{
			f[i] = -1;
			r[i] = 0;
		}
	}
	~FindUnion()
	{
		delete f;
		delete r;
	}
	int Find(int a)
	{
		return (f[a] == -1? a : f[a] = Find(f[a]));
	}
	void Join(int a, int b)
	{
		a = Find(a);
		b = Find(b);
		if(a == b)
			return;
		if(r[a] < r[b])
			f[a] = b;
		else
		{
			f[b] = a;
			if(r[a] == r[b])
				r[a]++;
		}
	}
};


int m[MAX_W][MAX_H], w, h, t;
char nam[MAX_W][MAX_H];

int nx[] = {0, -1, 1, 0}, ny[] = {-1, 0, 0, 1};

bool exist(int x, int y)
{
	return x >= 0 && x < w && y >= 0 && y < h;
}

int toInt(int x, int y)
{
	return y * w + x;
}

int where(int x, int y) {
	int px, py, bx = x, by = y, val = m[x][y];
	REP(i, 4) {
		px = x + nx[i];
		py = y + ny[i];
		if(exist(px, py) && m[px][py] < val) {
			val = m[px][py];
			bx = px;
			by = py;
		}
	}
	return toInt(bx, by);
}

int main()
{
	scanf("%d", &t);
	REP(i, t) {
		scanf("%d%d", &h, &w);
		FindUnion fu(w * h);
		REP(y, h)
			REP(x, w) {
				scanf("%d", &m[x][y]);
				nam[x][y] = '?';
			}
		REP(y, h)
			REP(x, w)
				fu.Join(toInt(x, y), where(x, y));
		int l = 'a';
		REP(y, h)
			REP(x, w) {
				int tmp = fu.Find(toInt(x, y));
				if(nam[tmp % w][tmp / w] == '?')
					nam[tmp % w][tmp / w] = l++;
			}
		printf("Case #%d:\n", i + 1);
		REP(y, h)
			REP(x, w) {
				int tmp = fu.Find(toInt(x, y));
				printf("%c%c", nam[tmp % w][tmp / w], (x + 1) < w ? ' ' : '\n');
			}
	}
	return 0;
}

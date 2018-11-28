/*###################START INCLUDE-urile#########################/*/
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <fstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

/*###################STOP INCLUDE-urile#########################/*/
using namespace std;
/*######################START PRECODE#############################*/
const long double eps = 1e-7; // marja de eroare
const long double pi=acos(-1.0);//valoarea lui PI
typedef long long LL;
typedef unsigned long long ULL;
typedef long double LD;
typedef pair<int,int> PII;
#define PB push_back  //vector<> v.PB(X);
#define NP next_permutation //v.NP()
#define MP make_pair //MP
#define X first //.X 
#define Y second //.Y
#define ALL(a) (a).begin(), (a).end() //sort(ALL(v))
#define RALL(a) (a).rbegin(), (a).rend()//sort(RALL(v)) //sens invers
#define FORIT(it, v) for (typeof((v).begin()) it = (v).begin(); it != (v).end(); ++it) //parcurg cu iteratoru//FORIT(it, V) {cout << *it << '\n';}
#define STERGE(v) memset(v,0,sizeof v) //set 0 on something
long long BIG_INF =  0x3f3f3f3f;
#define STERGEI(v) memset(v,0x3f, sizeof(v)) //set cu infinit
//memcmp
typedef stringstream iss; //iss f(string); f>>X; sau f << X;//sau de output
/*#####################TEMPLATES##################################*/

template<class A, class B> inline A i2s(B x){stringstream s; s<<x; A r; s>>r;return r;} //string x = i2s<string, int>(X);
template<class A> inline A abs(A a) {if (a < 0) return -a; return a;} //
//__gcd(A, B) - euclidu
template<class A> inline A euclid(A a, A b, A &x, A &y) {
	if (!b) {x=1, y = 0; return a;} 
	A ret = euclid(b, a%b, x, y);
	A aux = x; 
	x = y; y = aux - (a/b)*y;
	return ret;
} ///euclid(556, 21, A, B); si A * 556 + B * 21 = gcd-ul
//de verificad daca e prim
template<class A> inline int isPrime(A X) {
	if (X <= 1 || (X % 2 == 0 && X != 2)) return 0;
	for (A i = 3; i * i <= X; i+=2) if (X % i == 0) return 0;
	return 1;
} ///isPrime(22531);


void solve();
int main()
{
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; ++i)
	{
		printf("Case #%d: ", i);
		solve();
	}
	return 0;
}
int n;
vector<pair<int, int> > v;
map<pair<int, int>, int> E;
int S[2001], F[2001];
vector<vector<int> > FF;
vector<vector<int> > who;
int bestC;
int C[2001];
int MAX;
int SOL[2001];
void back(int k, int c)
{
	if (c > MAX) return;
	if (n - k + c <= bestC) return;
	if (k == n)
	{
		//verifica
		for (int i = 0; i < FF.size(); ++i)
		{
			set<int> x;
			for (int j = 0; j < FF[i].size(); ++j) x.insert(C[FF[i][j]]);
			if (x.size() != c) return;
		}
		bestC = c;
		for (int i = 1; i <= n; ++i) SOL[i] = C[i];
		return;
	}
	C[k+1] = c + 1;
	back(k+1, c + 1);
	for (int i = 1; i <= c; ++i)
	{
		C[k+1] = i;
		back(k + 1, c);
	}
}
void solve()
{
	//your code here
	v.clear();
	E.clear();
	FF.clear();
	who.clear();
	cin >> n;
	int m;
	cin >> m;
	for (int i = 0; i < m; ++i)
		cin >> S[i];
	for (int i = 0; i < m; ++i)
		cin >> F[i];
	for (int i = 0; i < m; ++i)
	{
		int a, b;
		a = S[i]; b = F[i];
		v.PB(MP(a, b));
		v.PB(MP(b, a));
		E[MP(a,b)] = 1;
		E[MP(b,a)] = 1;
	}
	for (int i = 1; i <= n; ++i)
	{
		int nxt = i + 1;
		if (nxt > n) nxt = 1;
		E[MP(i, nxt)] = 1;
		E[MP(nxt, i)] = 1;
	}
	// try to make figurens
	int col = n;
	for (int i = 1; i < (1 << n); ++i)
	{
		// can it be a figure?
		vector<int> fig;
		for (int j = 0; j < n; ++j) if (i & (1 << j))
			fig.PB(j + 1);
		if (fig.size() < 3) continue;
		// exista edges
		int pos = 1;
		for (int j = 0; j < fig.size(); ++j)
		{
			if (E[MP(fig[j], fig[(j + 1) % fig.size()])] == 0)
			{
				pos = 0;
				break;
			}
		}
		if (pos == 0) continue;
		// desparte
		for (int j = 0; j < fig.size(); ++j) 
			for (int dist = 2; dist < fig.size(); ++dist)
		{
			int nxt = j + dist;
			nxt %= fig.size();
			if ((nxt + 1) % fig.size() == j) continue;
			if (E[MP(fig[j], fig[nxt])])
			{
				pos = 0;
				break;
			}
		}
		if (pos == 0) continue;
		if (fig.size() < col) col = fig.size();
		FF.PB(fig);
		/*
		for (int j = 0; j < fig.size(); ++j)
		{
			who[fig[j]].PB(FF.size() - 1);
		}*/
	}
	MAX = col;
	bestC = 0;
	back(0, 0);
	cout << bestC << '\n';
	for (int i = 1; i <= n; ++i)
	{
		if (i > 1) cout << " ";
		cout << SOL[i];
	}
	cout << '\n';
}

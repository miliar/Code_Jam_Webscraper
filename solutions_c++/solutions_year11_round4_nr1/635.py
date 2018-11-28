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
void solve()
{
	//your code here
	double X, S, R, t;
	int N;
	cin >> X >> S >> R >> t >> N;
	vector<pair<int, int> > v;
	while (N--)
	{
		int B, E, W;
		cin >> B >> E >> W;
		int D = E - B;
		X -= D;
		v.PB(MP(W, D));	
	}
	if (X)
		v.PB(MP(0, X));
	sort(ALL(v));
	double ret = 0;
	for (int i = 0; i < v.size(); ++i)
	{
		double D = v[i].second;
		double A = v[i].first;

		double total = D / (A + R);
		if (t < total) total = t;
		t -= total;
		double fugit = (A + R) * total;
		ret += total;
		ret += (D - fugit) / (A + S);
	}
	printf("%.09lf\n", ret);
}

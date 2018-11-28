#include <map>
#include <set>
#include <queue>
#include <cstdio>
#include <cstring>
#include <cassert>
#include <numeric>
#include <algorithm>
#include <ctime>
#include <string>
#include <vector>
#include <iostream>
#include <cmath>
#include <cstdlib>
#include <sstream>
using namespace std;

#define pb push_back
#define pi 2*acos(0.0)
#define inf 1000000000
#define all(c) (c).begin(), (c).end()

#define L(s) (int)((s).end()-(s).begin())
#define ll long long
#define fo(i,n) for(i=0;i<(n);++i)
#define For(i,a,b) for (int i(a),_b(b); i <= _b; ++i)
#define Ford(i,a,b) for (int i(a),_b(b); i >= _b; --i)
#define Rep(i,n) for (int i(0),_n(n); i < _n; ++i)
#define Repd(i,n) for (int i((n)-1); i >= 0; --i)
#define Fill(a,c) memset(&a, c, sizeof(a))
#define MP(x, y) make_pair((x), (y))

typedef vector<int> vi;
typedef vector<string> vs;
typedef vector<double> vd;
typedef pair<int,int> pii;

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

const double eps = 1e-9;

int numCase, A, B, P;
int a[1001];
int primes[1001];

int gcd(int m, int n)
{

	while (m != n)
	{
		if (m>n) m = m - n;
		else n = n - m;
	}
	int endP = (int)sqrt(m) + 1;
	for (int i=2; i< endP; i++)
		while (m % i==0 && m!=i) m = m / i;

	return m;
}

void fillAll(int a0, int a1, int startP, int endP)
{
	for (int i=startP; i<=endP; i++)
	{
		if (a[i]==a1)
		{
			a[i] = a0;
		}
	}
}
int main()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);

	int sum = 0;

	Fill(primes,1);
/*	For(i,2,B)
		if (primes[i]!=0)
		{
			For(j,2,B/i)
				primes[j*i] = 0;
		}*/
	scanf("%d", &numCase);
	For(test, 1, numCase)
	{
		scanf("%d %d %d", &A, &B, &P);
		sum = B-A+1;
		For(i, A, B)
		{
			a[i] = i;
		}

		For(i,A,B-1)
			For(j,i+1,B)
			{
				if ((a[i]!=a[j])&&(gcd(i,j)>=P))
				{
					//cout << i << ' ' << j << endl;
					sum--;
					fillAll(a[i], a[j], A, B);
				}
			}
		cout << "Case #" << test << ": "<< sum <<endl;
	}

	return 0;
}

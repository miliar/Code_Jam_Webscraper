#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <cctype>
#include <cassert>
#include <climits>
#include <iostream>
#include <iomanip>
#include <vector>
#include <deque>
#include <string>
#include <sstream>
#include <stack>
#include <queue>
#include <map>
#include <set>
#include <utility>
#include <list>
#include <algorithm>

using namespace std;

#define FORI(N) for (int i = 0; i < (N); i++)
#define FOREI(N) for (int i = 1; i <= (N); i++)
#define FORJ(N) for (int j = 0; j < (N); j++)
#define FOREJ(N) for (int j = 1; j <= (N); j++)
#define FORK(N) for (int k = 0; k < (N); k++)
#define FOREK(N) for (int k = 1; k <= (N); k++)
#define ALL(A) A.begin(), A.end()
#define EACH(A,T) for (typeof(A.begin()) T = A.begin(); T != A.end(); T++)
#define REP(N) while (N--)

#define sz size()
#define pb(N) push_back(N)
#define CLEAR(M,O) memset (M, C, sizeof(M))

int A, B, P;
int V[1001];
int pr[1001];

int gcd (int a, int b)
{
	return (b==0)?a:gcd(b,a%b);
}

int can (int a, int b)
{
	int g = gcd(a,b);
	int gpf = 1;
	for (int i = 2; i*i <= g; i++)
		if ((!pr[i]) && g % i == 0)
		{
			while (g%i == 0) g /= i;
			gpf = i;
		}
	if (g > 1) gpf = g;
	return gpf >= P;
}

void dfs (int n)
{
	V[n] = 1;
	for (int i = A; i <= B; i++) if ((!V[i]) && can(n,i))
	    dfs(i);
}

int main()
{
	int T;
	cin >> T;
	memset (pr, 0, sizeof(pr));
	for (int i = 2; i <= 40; i++) if (!pr[i])
	    for (int j = i+i; j <= 1000; j += i) pr[j] = 1;
	for (int cc = 1; cc <= T; cc++)
	{
		cin >> A >> B >> P;
		memset (V, 0, sizeof(int) * 1001);
		int k = 0;
		for (int i = A; i <= B; i++)
		    if (!V[i]) { dfs(i); k++;}
		cout << "Case #" << cc << ": " << k << endl;
	}
	return 0;
}

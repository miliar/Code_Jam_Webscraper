#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <memory.h>
#include <vector>
#include <map>
#include <queue>

#define REP(i,n) for(int i=0; i<n; i++)
#define REPD(i,n) for(int i=(n-1); i>=0; i--)
#define FOR(i,a,b) for(int i=a; i<=b; i++)
#define FORD(i, a,b) for(int i=a; i>=b; i--)
#define FILL(a, v) memset(&a, v, sizeof(a))
#define DB(x) cout << #x << " : " << x << endl
#define pb push_back
#define mp make_pair
#define x first
#define y second

using namespace std;

const int MAXN = 1000000;

int T, c, Xor, m, sum, n;

int main()
{
	//freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
	scanf("%d", &T);
	FOR(Tn, 1, T)
	{
		printf("Case #%d: ", Tn);
		scanf("%d", &n);
		Xor = sum = 0; m = -1;
		REP(i, n)
		{
			scanf("%d", &c);
			Xor ^= c;
			sum += c;
			if (m == -1 || m > c) m = c;
		}
		if (Xor != 0) 
			printf("NO\n");
		else
			printf("%d\n", sum - m);
	}
	return 0;
}

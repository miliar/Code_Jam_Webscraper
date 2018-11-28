#include <iostream>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <string>
#include <sstream>
#include <algorithm>
#include <cstdio>
#include <cmath>
#include <bitset>
using namespace std;
#define forn(i,n) for(int i=0; i<int(n); i++)
#define forsn(i,s,n) for(int i=(s); i<int(n); i++)
#define dforn(i,n) for(int i = int(n) - 1; i >= 0; i--)
#define forall(i,c) for(__typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)
#define dforall(i,c) for(__typeof((c).rbegin()) i = (c).rbegin(); i != (c).rend(); i++)
#define all(c) (c).begin(), (c).end()
#define esta(v,c) ((c).find(v) != (c).end())
#define zMem(c) memset((c), 0, sizeof(c))
#define pb push_back
#define x first
#define y second
#define INF 1000000000
typedef long long tint;
typedef vector<int> vint;
typedef vector<vint> vvint;
typedef pair<int,int> pint;


int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	
	int TT;
	cin >> TT;
	
	forn(tt,TT)
	{
		int n,k;
		cin >> n >> k;
		int r = 1<<n;
		cout << "Case #" << (tt+1) << (((k+1) & (r-1)) ? ": OFF" : ": ON") << endl;
	}	
	
	return 0;
}

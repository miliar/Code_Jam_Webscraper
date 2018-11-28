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

int X[1024], V[1024];

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B.out","w",stdout);
	
	int TT; cin >> TT;
	forn(tt,TT)
	{
		int N,K,B,T; int cantc=0, cantswaps=0;
		cin >> N >> K >> B >> T;
		forn(i,N) cin >> X[i];
		forn(i,N) cin >> V[i];
		int cantmalas = 0;
		dforn(i,N)
		{
			if(cantc >= K) break;
			if(B-X[i]>V[i]*T) cantmalas++;
			else cantswaps += cantmalas, cantc++;
		}
		if(cantc >= K)
			cout << "Case #" << tt+1 << ": " << cantswaps << endl;
		else
			cout << "Case #" << tt+1 << ": " << "IMPOSSIBLE" << endl;
	}
		
	return 0;
}

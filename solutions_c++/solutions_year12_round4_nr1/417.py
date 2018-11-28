#pragma comment(linker,"/STACK:16777216")
#include <algorithm>
#include <cstring>
#include <set>
#include <map>
#include <vector>
#include <queue>
#include <iostream>
#include <iterator>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <sstream>
#include <fstream>
#include <locale>
#include <climits>

using namespace std;

typedef long long ll;
typedef unsigned long long Ull;

#define VI vector <int>
#define FOR(i, a, b) for(int (i) = (a); (i) < (b); ++(i))
#define RFOR(i, a, b) for(int (i) = (a)-1; (i) >= (b); --(i))
#define CLEAR(a) memset((a), , sizeof(a))
#define INF 1000000000
#define PB push_back
#define ALL(c) (c).begin(),  (c).end()
#define pi 2*acos(0.0)
#define SQR(a) (a)*(a)
#define MP make_pair
#define MOD 1000000007
#define EPS 1e-7
#define INF 2000000000


int T,TT,n,D;
int d[10010],l[10010];
int dd[10010];

int main()
{
	freopen("inputA.txt","r",stdin);
	freopen("outputA.txt","w",stdout);

	cin >> TT;
	FOR(T,0,TT)
	{
		cin >> n;
		FOR(i,0,n)
		{
			cin >> d[i] >> l[i];
			dd[i] = 0;
		}
		dd[0] = d[0];
		cin >> D;
		FOR(i,0,n)
		{
			FOR(j,i+1,n)
			{
				if (dd[i] < d[j] - d[i]) break;
				int r = min(d[j] - d[i],l[j]);
				dd[j] = max(dd[j],r);
			}
		}
		bool b = 0;
		RFOR(i,n,0)
			if (D - d[i] <= dd[i])
			{
				b = 1;
				break;
			}
		
		cout << "Case #" << T+1 << ": ";
		if (b)cout << "YES\n";else cout << "NO\n";
	}
	return 0;
}
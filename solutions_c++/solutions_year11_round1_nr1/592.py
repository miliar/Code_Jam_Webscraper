#include <iostream>
#include <cstring>
#include <cstdlib>
#include <cstdio>
#include <cmath>
#include <cassert>
#include <algorithm>
#include <numeric>
#include <functional>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>

using namespace std;

#define forn(i,n) for(int i=0;i<(int)(n);i++)
#define forsn(i,s,n) for(int i=(s);i<(int)(n);i++)
#define dforn(i,n) for(int i=(n)-1;i>=0;i--)
#define dforsn(i,s,n) for(int i=(n)-1; i>=(int)(s);i--)

#define forall(it,c) for(typeof((c).begin()) it = (c).begin(); it != (c).end(); it++)
#define dforall(it,c) for(typeof((c).rbegin()) it = (c).rbegin(); it != (c).rend(); it++)

#define esta(x,c) ((c).find(x) != (c).end())
#define all(c) (c).begin(),(c).end()

typedef long long tint;
typedef vector<int> vint;

const char *ans[2] = {"Broken", "Possible"};

tint mcd(tint a,tint b) { return (a==0)?b:mcd(b%a,a);}

int main()
{
	freopen("entrada.in","r",stdin);
	freopen("salida.out","w",stdout);
	int TT; cin >> TT;
	forn(tt,TT)
	{
		tint N,PD,PG;
		cin >> N >> PD >> PG;
		int res = 0;
		if (PG == 0)
			res = PD == 0;
		else if (PG == 100)
			res = PD == 100;
		else
		{
			const tint MD = mcd(PD,100LL);
			tint qD = 100 / MD;
			res = qD <= N;
		}
		cout << "Case #" << tt+1 << ": " << ans[res] << endl;
		cerr << "Case #" << tt+1 << ": " << ans[res] << endl;
	}
	return 0;
}

#include <iostream>
#include <sstream>
#include <string>
#include <cstring>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <deque>
#include <cstdio>
#include <cstdlib>
#include <numeric>
#include <functional>
#include <algorithm>

using namespace std;

#define forn(i,n) for(int i=0;i<(int)(n);i++)
#define forsn(i,s,n) for(int i=(s);i<(int)(n);i++)
#define dforn(i,n) for(int i=(n)-1;i>=0;i--)
#define dforsn(i,s,n) for(int i=(n)-1;i>=(int)(s);i--)

#define forall(i,c) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)
#define dforall(i,c) for(typeof((c).rbegin()) i = (c).rbegin(); i != (c).rend(); i++)
#define all(c) (c).begin(),(c).end()

#define esta(x,c) ((c).find(x) != (c).end())
#define zMem(c) memset((c),0,sizeof(c))

typedef long long tint;
typedef long double tdbl;

typedef pair<int,int> pint;
typedef pair<tint,tint> ptint;

typedef vector<int> vint;
typedef vector<vint> vvint;
typedef vector<string> vstr;

int n;

vint v;

bool anda(const vint &w)
{
	forn(i,w.size())
	if (w[i] > 0)
		return false;
	return true;
}

int res = 0;

void empujar(vint &v,int i,int su)
{
	if (v[i+1] == 0 || -v[i+1] + i + 1 < su)
		empujar(v,i+1,su+1);
	v[i]--;
	v[i+1]++;
	res++;
	swap(v[i],v[i+1]);
	
}

int main()
{
	freopen("entrada.in","r",stdin);
	freopen("salida.out","w",stdout);
	int totalCasos;
	cin >> totalCasos;
	forn(caso,totalCasos)
	{
		cin >> n;
		v = vint(n);
		forn(i,n)
		{
			int ma = -1;
			forn(j,n)
			{
				char x;
				cin >> x;
				if (x == '1')
					ma = j;
			}
			v[i] = ma;
		}
		
		res = 0;
		forn(i,n)
		{
			if (v[i] > i)
			{
				int el;
				forsn(j,i+1,n)
				if (v[j] <= i)
				{
					el = j;
					break;
				}
				dforsn(j,i,el)
				{
					swap(v[j],v[j+1]);
					res++;
				}
			}
		}
		cout << "Case #" << caso + 1 << ": " << res << endl;
	}
	return 0;
}

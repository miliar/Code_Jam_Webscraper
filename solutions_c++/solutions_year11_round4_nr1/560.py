#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <vector>
#include <algorithm>
#include <numeric>
#include <functional>

using namespace std;

#define forn(i,n) for(int i=0;i<(int)(n);i++)
#define forsn(i,s,n) for(int i=(s);i<(int)(n);i++)

#define forall(it,c) for(typeof((c).begin()) it = (c).begin(); it != (c).end(); it++)

#define all(c) (c).begin(),(c).end()

typedef long long tint;
typedef long double tdbl;
typedef pair<int,int> Pint;
typedef vector<int> vint;

typedef pair<int,int> Par;

int main()
{
	freopen("entrada.in","r",stdin);
	freopen("salida.out","w",stdout);
	int TT; cin >> TT;
	forn(tt,TT)
	{
		int X,S,R,t,N; cin >> X >> S >> R >> t >> N;
		vector<Par> v;
		R -= S;
		forn(i,N)
		{
			int A,B,W; cin >> A >> B >> W;
			const int L = B - A;
			X -= L;
			v.push_back(Par(S+W,L));
		}
		v.push_back(Par(S,X));
		sort(all(v));
		tdbl res = 0.0;
		tdbl T = t;
		forall(p,v)
		{
			tdbl L = p->second;
			tdbl W = p->first;
			tdbl time = L / (W + R);
			if (time <= T)
			{
				T -= time;
				res += time;
			}
			else
			{
				res += T + (L - T * (W + R)) / W ;
				T = 0.0;
			}
		}
		cout << "Case #" << tt+1 << ": ";
		printf("%.10lf\n",(double)res);
		cerr << "Case #" << tt+1 << ": ";
		fprintf(stderr,"%.10lf\n",(double)res);
	}
	return 0;
}

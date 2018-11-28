#include <iostream>
#include <vector>
#include <deque>
#include <cstdio>
#include <cstdlib>
#include <queue>

using namespace std;

#define forn(i,n) for(int i=0;i<(int)(n);i++)

typedef long long tint;

typedef vector<tint> vint;
typedef pair<int,tint> Par;
typedef deque<Par> Cola;

#define id first
#define cant second

int main()
{
	freopen("c.in","r",stdin);
	freopen("c.out","w",stdout);
	int TT; cin>>TT;
	forn(tt,TT)
	{
		tint R,k;
		int N;
		cin >> R >> k >> N;
		Cola q(N);
		forn(i,N) {cin >> q[i].cant; q[i].id = i;}
		tint res = 0;
		vint acu(N+5);
		vector<bool> u(N+5,false);
		vector<int> idp(N+5);
		acu[0] = 0;
		tint P = 0;
		while (R > 0)
		{
			
			if (u[q.front().id]) break;
			u[q.front().id] = true;
			idp[P] = q.front().id;
			R--;
			P++;
			acu[P] = acu[P-1];
			queue<Par> aux;
			tint cap = k;
			while ((!q.empty()) && cap >= q.front().cant)
			{
				cap -= q.front().cant;
				acu[P] += q.front().cant;
				aux.push(q.front());
				q.pop_front();
			}
			while (!aux.empty())
			{
				q.push_back(aux.front());
				aux.pop();
			}
			res = acu[P];
		}
		if (R > 0)
		{
			int pS;
			forn(i,N) if (idp[i] == q.front().id) {pS = i; break;}
			// pS = cantidad de veces que hay que iterar la operacion para que el que esté parado al frente
			// de la cola sea el primero que se repite en el ciclo.
			tint Pcost = acu[P] - acu[pS];
			res += (R / tint(P-pS)) * Pcost;
			R %= tint(P-pS);
			res += acu[pS + R] - acu[pS];
		}
		printf("Case #%d: %lld\n",tt+1,res);
	}
	return 0;
}
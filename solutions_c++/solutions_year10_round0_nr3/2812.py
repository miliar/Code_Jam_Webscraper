#include <iostream>
#include <utility>
#include <vector>
#include <cmath>
#include <map>
#define fori(N) for(long i=0;i<N;i++)
#define forj(N) for(long j=0;j<N;j++)
#define MK make_pair

using namespace std;

vector<int> g;
long R, k, N;
pair<int,pair<long,long> > ciclo;	// x0 : [#iteraciones del ciclo, #beneficios del ciclo]

void printVector()
{
	fori(g.size())
		cout << g[i] << " ";
	cout << endl;
}


long load(int x0, int &x1)
{
	long benf=0; // recaudado
	
	x1=x0;		// posicion inicial
	
	while(benf+g[x1]<=k)
	{
		benf+=(long)g[x1];	// llevalas
		x1=(x1+1)%N;	// siguiente, aún no incluido
		
		if(x1==x0)	// si vuelvo al principio
			break;
	}
	return benf;
}

void saltar_con_ciclo(long &i, long &benf)
{
	long d=R-i;
	long saltos=(long)d/ciclo.second.first;

	i+=saltos*ciclo.second.first;		//cantidad de saltos x iteraciones dentro de cada salto
	benf+=saltos*ciclo.second.second;	//cantidad de saltos x beneficios de cad salto
}

int compute()
{
	map<int,pair<long,long> > m;		// x0 : [iteracion, beneficios llevados]

	int x0=0, x1=0;
	long benf=0;
	fori(R)
	{
		if(m.find(x0)!=m.end())									// ya visitado, por tanto
		{
			ciclo=MK( x0, MK(i-m[x0].first,benf-m[x0].second));	// tengo un ciclo
			
			//cout << "0: iter: " << i << " benf: " << benf << endl;
			saltar_con_ciclo(i, benf);	// he saltado
			//cout << "1: iter: " << i << " benf: " << benf << endl;

			m.clear();
			
			if(i>=R)
				continue;
		}
		else
			m[x0]=MK(i,benf);							// guardo estado actual

		benf+=load(x0,x1);
		//cout << benf << " : [" << x0 << ":" << x1 << "]" <<endl;	
		x0=x1;
	}
	return benf;
}

int main()
{
	int t, x;

	cin >> t;

	fori(t)
	{
		cin >> R >> k >> N;
		forj(N)
		{
			cin >> x;
			g.push_back(x);
		}
		//printVector();
		
		int res=compute();

		cout << "Case #"<<i+1<<": ";
		cout << res << endl;
		g.clear();
	}
	return 0;
}
#include <cstring>
#include<iostream>
#include <sstream>
#include<list>
#include<vector>
#include<queue>
#include<set>
#include<string>
#include <stack>
#include <cstdlib>
#include <algorithm>
#include <deque>
#include <cmath>
#define forn(i, n) for(int i = 0; i < (int)(n); ++i)
#define dforn(i, n) for(int i = (int)(n)-1; i >= 0; --i)
#define forsn(i, s, n) for(int i=(s); i<(int)(n); ++i)
#define dforsn(i, s, n) for(int i=(int)(n)-1;i>=(s);--i)
#define forall(it, X) for(typeof((X).begin()) it = (X).begin(); it != (X).end(); ++it)
#define dforall(it, X) for(typeof((X).rbegin()) it = (X).rbegin(); it != (X).rend(); ++it)
#define all(c) c.begin(), c.end() 
#define tr(container, it) for(typeof(container.begin()) it = container.begin(); it != container.end(); it++) 
#define present(container, element) (container.find(element) != container.end()) 
#define cpresent(container, element) (find(all(container),element) != container.end()) 
#define sz(a) int((a).size()) 
#define pb push_back 
using namespace std;
typedef vector<int> vint;
typedef vector<vint> vvint;
template<class T> string i2s(T x) {ostringstream o; o << x; return o.str(); };
typedef pair<int,int> ii;

vector< list<long> > gruposGlobal;
long posIgual = -100;
long finPosIgual = -100;

//****************************************************************
bool esIgual(list<long> lista, list<long> grup)
{	while (!lista.empty())
	{	if (lista.front()!=grup.front()) 
			return false;
		lista.pop_front();
		grup.pop_front();
	}
	return true;
}
//****************************************************************
bool esta(list<long> lista)
{	for (long i=0;i<gruposGlobal.size();i++)
	{	if (esIgual(lista, gruposGlobal[i]))
		{	if (posIgual==-100) posIgual = i;
			return true;
		}
	}
	return false;
}
//****************************************************************
void mostrar(list<long> lista)
{	while (!lista.empty())
	{	cout << lista.front() << "  ";
		lista.pop_front();
	}
	
	cout << endl;
}
//****************************************************************
long long unaVuelta(long capacidad, list<long>* grupos, int totGrupos)
{	long long carga = 0;
	int repeticiones = 0;
	while ((repeticiones < totGrupos)&&(carga + grupos->front() <= capacidad ))
	{	long auxi = grupos->front();
		grupos->pop_front();
		grupos->pb(auxi);
		carga += auxi;		
		repeticiones++;
	}
	
	return carga;
}
//****************************************************************
long long resolver(long vueltas, long capacidad, int totGrupos, list<long> grupos)
{	long long res = 0;
	long long ciclo = 0;
	long long auxi = 0;
	long long longCiclo = 0;	
	long long antes = 0;	
	long long durante = 0;	
	long long despues = 0;	
	long long faltan = vueltas;
	vector<long long> parciales;
 
	long hi;
	for (hi=0;hi<vueltas;hi++)
	{	auxi = unaVuelta(capacidad, &grupos, totGrupos);
		res += auxi;
		
		//cout << hi << " ) ";
		if (!esta(grupos)) 
		{	gruposGlobal.pb(grupos);
			//cout << "          ";
			parciales.pb(auxi);
		}
		else
		{	//cout << " Es Igual ";
			finPosIgual = hi;
			parciales.pb(auxi);
			break;
		}
		//cout << res << " -->  ";
			
		//mostrar(grupos);
	}
	
	if (hi==vueltas) return res;
	
	//forn(i,sz(parciales)) cout << parciales[i] << " | ";
	longCiclo = finPosIgual - posIgual + 1;
	//cout << endl << posIgual << " @ " << finPosIgual << " -> " << longCiclo;
	//cout << endl;
	
	for (long i = posIgual;i<finPosIgual+1;i++) ciclo += parciales[i];
	//cout << " ciclo: " << ciclo << endl;

	for (long i = 0;i<finPosIgual+1;i++) antes += parciales[i];
	//cout << "antes " << antes << endl;
	
	faltan -= finPosIgual+1;
	//cout << "faltan " << faltan << endl;

	//cout << "longCiclo " << longCiclo << endl;
	durante = ciclo*(faltan/(longCiclo));
	//cout << "durante " << durante << endl;

	faltan -= (faltan/longCiclo)*longCiclo;
	//cout << "faltan " << faltan << endl;
	for (long i = 0;i<faltan%(longCiclo);i++)
	{ 	despues += parciales[posIgual+i];
		//cout << "-----------------> " << i << "  " << despues << endl;
	}
	//cout << "despues " << despues << endl;

	return antes+durante+despues;
}
//****************************************************************
int main()
{	int totalCasos, N; 
	long R, k, auxi;
	list<long> grupos,grInicial;
	long long solucion;
	
	cin >> totalCasos;
	for (int caso=1;caso<=totalCasos;caso++)
	{	cin >> R;
		cin >> k;
		cin >> N;
		grupos.clear();
		grInicial.clear();
		forn(i,N) { cin >> auxi; grupos.pb(auxi);grInicial.pb(auxi); }
		gruposGlobal.clear();
		gruposGlobal.pb(grInicial);
		//mostrar(grInicial);
		//cout << "===========" << endl;

		posIgual = finPosIgual = -100;
		solucion =resolver(R, k, N, grupos);
		cout << "Case #" << caso << ": " << solucion << endl;
	}
	
	return 0;
}
//****************************************************************


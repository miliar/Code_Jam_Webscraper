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


//****************************************************************
class Par
{public: string str;
	 int tam;
	 Par(string stri)
	 {	str = stri;
		tam = 0;
		forn (i,sz(str))
		  if (str[i]=='/') tam++;
	 }
	 string toString()
	 {	return str + " # " + i2s(tam);
	 }
};
bool operator<(const Par &a, const Par &b) 
{	if (a.tam==b.tam) return a.str < b.str;
	return a.tam < b.tam;
}
//****************************************************************
vector<Par> estan, faltan;
//****************************************************************
int main()
{	int totalCasos,N,M; 
	string linea;
		
	cin >> totalCasos;
	for (int caso=1;caso<=totalCasos;caso++)
	{	estan.clear();faltan.clear();
		cin >> N;
		cin >> M;
		forn (i,N)
		{	cin >> linea;
			estan.pb(Par(linea));
		}
		forn (i,M)
		{	cin >> linea;
			faltan.pb(Par(linea));
		}
		
		sort(all(estan));
		sort(all(faltan));
		/*tr(estan,it)
		{	cout << "Estan: " << it->toString() << endl;
		}
		tr(faltan,it)
		{	cout << "Faltan: " << it->toString() << endl;
		}*/
		
		int contador = 0;
		forn (q,sz(faltan))
		{   string palabra = faltan[q].str;
		    palabra +=  '/';
		    string prefijo = "";
		    palabra = palabra.substr(1,sz(palabra));
		    while (palabra!="")  
		    { 	prefijo += "/";
			    string::size_type loc2 = palabra.find( "/", 0 );
			    prefijo += palabra.substr(0,loc2);
			    			    
			    bool lopongo = true;
			    tr(estan,it2)
			    {	if (it2->str==prefijo)
				{  	lopongo = false;
					break;
				}
			    }
			    if (lopongo)
			    {  	estan.pb(Par(prefijo));
				contador++;
			    }
			    //cout << "prefijo " << q << "  -> "<< prefijo << " lopongo "  << lopongo << endl;
			    palabra = palabra.substr(loc2+1,sz(palabra));
		    }
		} 
		
		cout << "Case #" << caso << ": " << contador << endl;
	}
	
	return 0;
}
//****************************************************************


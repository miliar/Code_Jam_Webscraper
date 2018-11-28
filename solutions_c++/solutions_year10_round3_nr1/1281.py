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
vector< pair<int,int> > cables;
//****************************************************************
int main()
{	int totalCasos,N,c1,c2; 
	string linea;
	pair<int,int> cable1,cable2;
	int a1,b1,a2,b2;
		
	cin >> totalCasos;
	for (int caso=1;caso<=totalCasos;caso++)
	{	cables.clear();
		cin >> N;
		forn(i,N)
		{	cin >> c1;
			cin >> c2;
			cables.pb(make_pair(c1,c2));
		}
	
		
		int cont = 0;  
		int cont2 = 0;
		forn (i,sz(cables))
		{	cable1 = cables[i];
			a1 = cable1.first;
			b1 = cable1.second;
			forn (j,sz(cables))
			{	if (i!=j)
				{	cable2 = cables[j];
					a2 = cable2.first;
					b2 = cable2.second;
					
					if (!(((a1>a2)&&(b1>b2)) || ((a1<a2)&&(b1<b2))))
					{	//cout << "Si" << endl;
						if (((a2>b1)&&(a2<a1)&&(b2>b1)&&(b2<a1))
						    || ((a2>a1)&&(a2<b1)&&(b2>a1)&&(b2<b1)))
						  cont++;
						else
						  cont2++;
					}
				}
			}
		}
		cout << "Case #" << caso << ": " << (cont +cont2)/2 << endl;
	}
	
	return 0;
}
//****************************************************************


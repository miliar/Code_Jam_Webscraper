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


//****************************************************************
void parsear(char* frase)
{	char *ptr;
  	ptr = strtok(frase," \t");
  	while(ptr != NULL)
    	{    	cout << ptr << endl;
      		ptr = strtok(NULL, " \t");
    	}
  	cout << "---------------------" << endl;
}
//****************************************************************
vector<bool> cambiar(vector<bool> cadena, int largo)
{   int pos = 0;
        bool valorPos = cadena[pos];
        cadena[pos] = ! cadena[pos];

        while (valorPos)
        {   pos++;
            if (pos==largo) 
                break;
            valorPos = cadena[pos];
            cadena[pos] = ! cadena[pos];
        }
	return cadena;
}
//****************************************************************
int main()
{	int totalCasos, N, particiones, resto; 
	long K;
	string res;
	cin >> totalCasos;
	for (int caso=1;caso<=totalCasos;caso++)
	{	cin >> N;
		cin >> K;
		particiones = (int) pow(2.0,(double)N);
		resto = K % particiones;
		if (resto == particiones-1)
		{	res = "ON";
		}
		else
		{	res = "OFF";
		}
		//cout << "particiones: " << particiones << "  resto: " << resto << endl;
		cout << "Case #" << caso << ": " << res << endl;
		//cout << "----------------" << endl;
	}
	
	return 0;
}
//****************************************************************
/*
int main()
{	int totalCasos, N, particiones, resto; 
	long K;
	string res;
	cin >> totalCasos;
	for (int caso=1;caso<=totalCasos;caso++)
	{	cin >> N;
		cin >> K;

		vector<bool> cadena(N, false);		
		for (int i=0;i<K;i++)
            		cadena = cambiar(cadena, N);

		if (cadena[N-1])
		{	res = "ON";
		}
		else
		{	res = "OFF";
		}

		//cout << "particiones: " << particiones << "  resto: " << resto << endl;
		cout << "Case #" << caso << ": " << res << endl;
		//cout << "----------------" << endl;
	}
	
	return 0;
}*/

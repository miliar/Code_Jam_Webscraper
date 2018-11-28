// C.cpp: archivo de proyecto principal.

#include "stdafx.h"
#include <vector>
#include <queue>
#include <map>
#include <list>
#include <queue>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>

using namespace std;

/* tipos */
typedef pair<int,int> pint;
typedef long long tint;
typedef unsigned int mint;
typedef unsigned long long mtint;

typedef vector<int> vint;
typedef vector<vint> vvint;

typedef long double tipo;

/* "funciones" */
#define forn(i,n) for(int ___n=n, i=0;i<___n;++i)
#define dforn(i,n) for(int i=(n)-1;i>=0;--i)
#define forsn(i,s,n) for(int ___n=n, i=s;i<___n;++i)
#define dforsn(i,s,n) for(int i = (int)(n)-1; i>=((int)s); i--)
#define forall(it,X) for(typeof((X).begin()) it = (X).begin(); it != (X).end(); ++it)
#define dforall(it,X) for(typeof((X).rbegin()) it = (X).rbegin(); it != (X).rend(); ++it)
#define all(X) (X).begin(), (X).end()
#define esta(e, c) (c.find(e) != c.end())
#define DBG(a) cerr << #a << " = " << a << endl;

template<class T> string itos(const T&x) { ostringstream o; o<<x; return o.str(); }

string wrd[5050];
char mp[256][15];

tint mcd(tint a, tint b){return (b==0)?a:mcd(b, a%b);}


int ShiftLeft(int nro,int MaxDig)
{
	char Numero[10];
	char format[10];
	char dig;
	format[0]='%';
	sprintf(format+1, "0%dd", MaxDig);		

	sprintf(Numero, format, nro);
	dig=Numero[0];
	for(int j=0; j != MaxDig-1; j++)
	{
		Numero[j]=Numero[j+1];		
	}
	Numero[MaxDig-1]=dig;			
	
	return atoi(Numero);
}

int IsRecycled(int A, int B, int nro, int digitos)
{
	int nroshift;
	int guardados[10000];
	int recycled;
	bool valido;
	if(digitos==1)
		return 0;
	recycled=0;
	nroshift=nro;
	//printf("\nProbando con: %d\n", nro);
	for(int i=0; i<digitos-1;i++)
	{
		nroshift=ShiftLeft(nroshift,digitos);
		//printf("nroshift: %d\n",nroshift);
		if(nroshift>nro && nroshift<=B)
		{
			//printf("\nnro: %d - recycled: %d\n",nro,nroshift);
			valido=true;
			for(int j=0;j<recycled;j++)
				if(guardados[j]==nroshift)
					valido=false;
			if(!valido)
				continue;
			guardados[recycled]=nroshift;
			recycled++;
			
		}
	}
	return recycled;
}


int Cantidad_Recycled(int A, int B)
{
	int nro;
	int recycled;	
	int digitos=0;
	for(int j=A; j!=0;j/=10)
		digitos++;
	
	nro=A;
	recycled=0;
	while(nro<=B)
	{
		recycled+=IsRecycled(A, B, nro,digitos);
		nro++;
	}
	
	return recycled;
}


int main() {
	int casos;
	int recycled;
	int A, B;
	
	cin >> casos;
	
	for(int i=0; i < casos; i++)
	{				
		cin >> A;
		cin >> B;

		recycled = Cantidad_Recycled(A, B);
		cout << "Case #" << i+1 << ": " << recycled << endl;

	}
	
	return 0;
}


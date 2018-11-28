// B.cpp: archivo de proyecto principal.

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


int main() {
	int casos;
	int googlers;
	int Tscore;
	int surprising;
	int result;
	int p;
	

	cin >> casos;
	
	for(int i=0; i < casos; i++)
	{		
		result=0;
		cin >> googlers;
		cin >> surprising;
		cin >> p;
			
		for(int j=0; j < googlers; j++)
		{
			
			cin >> Tscore;			
			if(!Tscore && p)
				continue;

			if(Tscore >= (p*3-2))
			{
				result++;
				continue;
			}
			if(surprising)
			{				
				if(Tscore>=(p*3-4))
				{				
					surprising--;				
					result++;
				}
			}
		}

		cout << "Case #" << i+1 << ": " << result << endl;

	}
	
	return 0;
}


// A.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <map>
#include <set>
#include <list>
#include <string>
#include <iostream>
#include <fstream>
#include <strstream>
#include <algorithm>
#include <vector>
#include <cassert>
#include <cassert>
#include <math.h>

#define FOR(i,a,b) for(int i=(a),_b=(b);i<=_b;i++)
#define REP(i,n) FOR(i,0,(n)-1)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;i--)
#define sz size()
template<class T> inline int size(const T& c) { return c.sz; }
#define FORA(i,c) REP(i,size(c))

#define itype(c) __typeof((c).begin())
#define FORE(e,c) for(itype(c) e=(c).begin();e!=(c).end();e++)
#define pb push_back
#define mp make_pair
#define all(x) (x).begin(),(x).end()
#define SORT(x) sort(all(x))
#define REVERSE(x) reverse(all(x))
#define CLEAR(x,c) memset(x,c,sizeof(x)) 
template<class T> inline void checkmin(T &a,T b){if(b<a) a=b;}//asigna en a el minimo
template<class T> inline void checkmax(T &a,T b){if(b>a) a=b;}//asigna en a el maximo

using namespace std;


//INT_MAX,LLONG_MAX


ifstream in("inL.txt");
ofstream out("out.txt");


__int64 N,PD,PG;
void Solve()
{
	if(PG == 0 && PD != 0)
	{
		out << "Broken";
		return;
	}
	else if(PG == 100 && PD != 100)
	{
		out << "Broken";
		return;
	}

	__int64 val = 100;
	if(PD % 2 == 0)
	{
		val /= 2;
		PD /=2;
	}
	if(PD % 2 == 0)
	{
		val /= 2;
		PD /=2;
	}


	if(PD % 5 == 0)
	{
		val /= 5;
		PD /=5;
	}
	if(PD % 5 == 0)
	{
		val /= 5;
		PD /=5;
	}
	if(val <= N)
		out << "Possible";
	else
		out << "Broken";
}

int _tmain(int argc, _TCHAR* argv[])
{
	int CCC;
	in >> CCC;
	REP(cccc,CCC)
	{
		in >> N >>  PD >> PG;
		out << "Case #" << cccc+1 << ": ";
		Solve();
		out << endl;
	}	return 0;
}


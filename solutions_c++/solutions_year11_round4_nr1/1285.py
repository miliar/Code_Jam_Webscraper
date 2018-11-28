// A.cpp : Defines the entry point for the console application.
//


#include "stdafx.h"


#include <map>
#include <set>
#include <list>
#include <string>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <cassert>
#include <cassert>
#include <math.h>

using namespace std;

ifstream in("inL.txt");
ofstream out("out.txt");

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
#define metafor(c,i) for(i = c.begin();i != c.end();++i)
template<class T> inline void checkmin(T &a,T b){if(b<a) a=b;}//asigna en a el minimo
template<class T> inline void checkmax(T &a,T b){if(b>a) a=b;}//asigna en a el maximo

///LLONG_MAX,INT_MAX
#define INF INT_MAX

int N,NN;
double X,S,R,t;


struct CC
{
	bool operator < (const CC &other)
	{
		return pos < other.pos;
	}
	pair<double,double> pos;
	double speed;
};
double Size(CC cc)
{
	return cc.pos.second-cc.pos.first;
}
bool CompSpeed(const CC &a,const CC &b)
{
	return a.speed < b.speed;
}


CC corrs[3010];
void Solve()
{
	double pos = 0.0;
	double now = 0;
	double tR = t;
	REP(i,NN)
	{
		double d = Size(corrs[i]);
		//double distToNext = corrs[i].pos.first-pos;

		double timeS = d/(S+corrs[i].speed);
		double timeR = d/(R+corrs[i].speed);
		if(t >= 0)
		{
			if(timeR <= t) //puedo correrlo todo
			{
				t -= timeR;
				now += timeR;
			}
			else
			{
				///corro t
				double newPos = d - (R+corrs[i].speed)*t;
				now += t;
				t = 0;
				now += newPos/(S+corrs[i].speed);
			}
		}
		else
		{
			now += timeS;
		}
	}
	char buffer[100];
	sprintf(buffer,"%.10lf",now);
	out << buffer;
}

int _tmain(int argc, _TCHAR* argv[])
{
	int ccc;
	in >> ccc;
	REP(c,ccc)
	{
		in >> X >> S >> R >> t >> N;
		int pos = 0;
		CC tmp[3010];

		REP(i,N)
		{
			in >> tmp[i].pos.first >> tmp[i].pos.second >> tmp[i].speed;
		}
		sort(tmp,tmp+N);
		NN = 0;
		REP(i,N)
		{
			CC cc = tmp[i];
			if(cc.pos.first == pos)
				corrs[NN++] = cc;
			else
			{
				CC mm;
				mm.speed = 0;
				mm.pos.first = pos;
				mm.pos.second = cc.pos.first;
				corrs[NN++] = mm;
				corrs[NN++] = cc;

			}
			pos = cc.pos.second;
		}
		if(pos != X)
		{
			CC mm;
			mm.speed = 0;
			mm.pos.first = pos;
			mm.pos.second = X;
			corrs[NN++] = mm;
		}
		sort(corrs,corrs+NN,CompSpeed);
		out << "Case #" << c+1 << ": ";
		Solve();
		out << endl;
	}	return 0;
}



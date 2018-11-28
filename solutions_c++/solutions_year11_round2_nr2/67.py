#pragma comment(linker,"/STACK:64000000")
#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <cmath>
#include <map>
#include <set>
#include <ctime>
#include <algorithm>
#include <memory.h>

using namespace std;

#define WR printf
#define RE scanf
#define PB push_back
#define SE second
#define FI first

#define FOR(i,k,n) for(int i=(k); i<=(n); i++)
#define DFOR(i,k,n) for(int i=(k); i>=(n); i--)
#define SZ(a) (int)((a).size())
#define FA(i,v) FOR(i,0,SZ(v)-1)
#define RFA(i,v) DFOR(i,SZ(v)-1,0)
#define CLR(a) memset(a, 0, sizeof(a))

#define LL long long
#define VI  vector<int>
#define PAR pair<int ,int>
#define o_O 1000000000 
void __never(int a){printf("\nOPS %d", a);}
#define ass(s) {if (!(s)) {__never(__LINE__);cout.flush();cerr.flush();abort();}}

int C;
double D;
vector< double > vec;

bool check(double t)
{
	double pos = vec[0]-t;
	FA(a,vec) if (a)
	{
		if (vec[a]+t < pos+D) return false;
		pos = max(pos+D, vec[a]-t);
	}
	return true;
}

void sol()
{
	sort(vec.begin(), vec.end());
	double mi=0., ma=100000.*100000.*100000.;
	FOR(a,1,100)
	{
		double sr = (mi+ma)*0.5;
		if (check(sr)) ma=sr;
		else mi=sr;
	}
	WR("%.10lf", mi);
}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int T;
	cin >> T;
	FOR(a,1,T)
	{
		cerr << a << "\n";
		cin >> C >> D;
		int x, y;
		vec.clear();
		FOR(b,1,C)
		{
			cin >> x >> y;
			FOR(c,1,y) vec.push_back((double)x);
		}
		cout << "Case #" << a << ": ";
		sol();
		cout << "\n";
	}
	return 0;
}
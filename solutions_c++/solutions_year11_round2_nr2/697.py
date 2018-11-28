#include <cstdio>
#include <numeric>
#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <sstream>
#include <cmath>
#include <iomanip>

using namespace std;

typedef vector <int> VI;
typedef vector <string> VS;
typedef long long LL;
typedef stringstream SS;

#define ALL(x) x.begin(),x.end()
#define REP(i,n) for(int i=0; i<(n); i++)
#define FOR(i,a,b) for(int i=(a); i<(b); i++)
#define FORE(i,c) for(__typeof((c).begin())i=(c).begin();i!=(c).end();++i)
#define PB push_back
#define sz size()
#define MP make_pair
#define two(x) (1<<(x))


/////////////////////////////////////////////////////////////////////////////////

double P[300];
int V[300];
double D;

bool cando(double t, int C)
{
	double start=P[0]-t;
	vector<double> w;
	REP(i,C) REP(j,V[i]) w.PB(P[i]);
	REP(i,w.sz)
	{
		if(w[i]>start)
		{
			start=max(start, w[i]-t)+D;
		}
		else
		{
			if(start-w[i]>t) return false;
			else start+=D;
		}
	}
	return true;
}

int main()
{
	int T;
	cin>>T;
	REP(index, T)
	{
		cout<<"Case #"<<index+1<<": ";
		//
		int C;
		cin>>C>>D;
		REP(i,C) cin>>P[i]>>V[i];
		
		double low=0.0, high=1e20;
		while(high-low>1e-9)
		{
			double mid=(low+high)/2.0;
			if( cando(mid, C) ) high=mid;
			else low=mid;
		}
		
		cout<<high<<endl;
	}
	return 0;
}

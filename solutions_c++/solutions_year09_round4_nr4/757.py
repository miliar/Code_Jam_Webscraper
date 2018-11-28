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
int N;
double x[50], y[50], r[50];


int main()
{
	int testcases;
	cin >> testcases;
	int index=0;
	while(index<testcases)
	{
		cin>>N;
		REP(i,N) cin>>x[i]>>y[i]>>r[i];


		double ret=1e100;

		if(N==1) { ret=r[0]; }
		else if( N==2) { ret=max(r[0],r[1]); }
		else{
		REP(i,N)
		{
			vector<int>  g1, g2;
			REP(j,N) if(j==i) g1.PB(j); else g2.PB(j);
			double x1=0, y1=0, x2=0, y2=0;
/*			REP(j,g1.sz) x1+=x[g1[j]], y1+=y[g1[j]];
			REP(j,g2.sz) x2+=x[g2[j]], y2+=y[g2[j]];
			x1/=g1.sz; y1/=g1.sz; x2/=g2.sz; y2/=g2.sz;
			double r1=0, r2=0;
			REP(j, g1.sz) r1=max(r1, sqrt((x[g1[j]]-x1)*(x[g1[j]]-x1)+(y[g1[j]]-y1)*(y[g1[j]]-y1))+r[g1[j]]);
			REP(j, g2.sz) r2=max(r2, sqrt((x[g2[j]]-x2)*(x[g2[j]]-x2)+(y[g2[j]]-y2)*(y[g2[j]]-y2))+r[g2[j]]);
			cout<<g1.sz << " "<<g2.sz <<" "<< r1 <<" " <<r2<<endl;
*/
			double r1=r[i];
			double r2=sqrt((x[g2[0]]-x[g2[1]])*(x[g2[0]]-x[g2[1]])+(y[g2[0]]-y[g2[1]])*(y[g2[0]]-y[g2[1]]))/2.0;
			r2+=(r[g2[0]]+r[g2[1]])/2.0;

			ret=min(ret, max(r1,r2));
		}
		}
				
		
		cout << "Case #" << ++index <<": " << ret << endl;
	}
	return 0;

}

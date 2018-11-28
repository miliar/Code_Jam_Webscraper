//Done by Grey Matter
//Fet per Ferran Alet

#include<iostream>
#include<cmath>
#include<iomanip>
#include<vector>
#include<map>
#include<queue>
#include<fstream>
#include<algorithm>
#include<string>
#include<stack>
#include<numeric>
#include<set>
#include<sstream>

#define INF 2147483647
#define LINF 1000000000000000000LL
#define EPS 1e-9
#define debug(x) cerr << #x << " = " << x << endl
#define FORN(x,y) for(int x=0;x<y;x++)
#define FORU(x,y) for(int x=1;x<=y;x++)
using namespace std;


typedef pair<int,int> PII;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<bool> VB;
typedef vector<VB> VVB;
typedef vector<string> VS;
typedef map<int,int> MII;
typedef MII::iterator iMII;
typedef long long ll;
typedef vector<pair<long double,long double> > VDD;

ifstream fin("Dsmall2.in");
ofstream fout("Dsmall2.out");

long double dist(long double xa,long double xb, long double ya, long double yb){
	return sqrt((xb-xa)*(xb-xa)+(yb-ya)*(yb-ya));
}

long double formuleta(long double r, long double R, long double d){
//	cerr<<endl<<endl<<(d*d+r*r-R*R)/(2*d*r)<<" ==> "<<acos((d*d+r*r-R*R)/(2*d*r))<<endl<<endl;
	long double parta=r*r*acos((d*d+r*r-R*R)/(2*d*r));
	long double partb=R*R*acos((d*d+R*R-r*r)/(2*d*R));
	long double partc=0.5*sqrt((-d+r+R)*(d+r-R)*(d-r+R)*(d+r+R));
	return parta+partb-partc;
}

int main() {
	int tests;
	fin>>tests;
	for(int test=1;test<=tests;test++){
		int n,m;
		fin>>n>>m;
		VDD Q(m);
		long double xa,xb,ya,yb;
		fin>>xa>>ya>>xb>>yb;
		for(int i=0;i<m;i++) fin>>Q[i].first>>Q[i].second;
		fout<<"Case #"<<test<<':';
		long double d=dist(xa,xb,ya,yb);
//		debug(d);
		for(int i=0;i<m;i++){
			long double ra=dist(xa,Q[i].first,ya,Q[i].second),rb=dist(xb,Q[i].first,yb,Q[i].second);
//			debug(ra);
//			debug(rb);
			fout<<' ';
			fout<<fixed;
			fout<<setprecision(7)<<formuleta(ra,rb,d);
		}
		fout<<endl;
	}
	system("pause");
}

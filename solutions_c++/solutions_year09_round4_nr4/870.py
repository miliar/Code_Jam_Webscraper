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

double distance(double x1, double y1, double x2, double y2, double r1, double r2){
	return (sqrt(((x1-x2)*(x1-x2))+((y1-y2)*(y1-y2)))+r1+r2);
}

int main() {
	ifstream fin("D.in");
	ofstream fout("D.out");
	int tests,n;
	fin>>tests;
	for(int cas=1;cas<=tests;cas++){
		fin>>n;
		vector<pair<double,pair<double,double> > > v(n);
		FORN(i,n) fin>>v[i].first>>v[i].second.first>>v[i].second.second;
		if(n==1) fout<<"Case #"<<cas<<": "<<v[0].second.second<<endl;
		if(n==2) fout<<"Case #"<<cas<<": "<<max(v[0].second.second,v[1].second.second)<<endl;
		if(n==3){
			double d01=distance(v[0].first,v[0].second.first,v[1].first,v[1].second.first,v[0].second.second,v[1].second.second);
			double d12=distance(v[2].first,v[2].second.first,v[1].first,v[1].second.first,v[2].second.second,v[1].second.second);
			double d02=distance(v[0].first,v[0].second.first,v[2].first,v[2].second.first,v[0].second.second,v[2].second.second);
			fout<<"Case #"<<cas<<": "<<min(d01,min(d12,d02))/2.<<endl;
		}
	}
}

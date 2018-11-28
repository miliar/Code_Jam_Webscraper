#include <cstdio>
#include <iostream>
#include <algorithm>
#include <set>
#include <map>
#include <stack>
#include <list>
#include <queue>
#include <deque>
#include <cctype>
#include <string>
#include <vector>
#include <sstream>
#include <iterator>
#include <numeric>
#include <cmath>
#include <fstream>
#include <time.h>

using namespace std;

typedef long double LD;
typedef vector <int > VI;
typedef vector < VI > VVI;
typedef long long LL;
typedef vector < LL > VLL;
typedef vector < double > VD;
typedef vector < string > VS;
typedef pair<int,int> PII;
typedef pair<double,double> PDD;
typedef pair<double,int> PDI;
typedef pair<LL,LL> PLL;
typedef pair<LD,LD> PLDD;
typedef vector <PLL> VLLL;
typedef vector <PLDD> VLDD;
typedef vector <PII> VII;
typedef vector <PDD> VDD;
typedef vector <PDI> VDI;
typedef istringstream ISS;
typedef priority_queue<PDI,VDI,greater<PDI> > PQ;


#define ALL(x) x.begin(),x.end()
#define FILL(a,c) memset(a, (c), sizeof(a))
#define REP(i,n) for (int i=0; i<(n); ++i)
#define REPS(i,s,n) for (int i=(s); i<(n); ++i)
#define FOR(var,bas,son) for (int var=(bas); var<=(son); ++var)
#define FORD(var,bas,son) for (int var=(bas); var>=(son); --var)
#define FOREACH(it, X) for(__typeof((X).begin()) it = (X).begin(); it != (X).end(); ++it)
#define PB push_back
#define PF push_front
#define MP(a,b) make_pair(a,b)
#define ME(a,b) max_element((a), (b))
#define FT first
#define SD second
#define X first
#define Y second
#define SIZE(x) (int)x.size()
#define P2(a) (a)*(a)
#define S2(a) sqrt((a))
#define DIST(x,y)   sqrt((x)*(x)+(y)*(y))
#define S2I(a) atoi((a).c_str())
#define S2L(a) atol((a).c_str())
#define S2D(a) atof((a).c_str())
#define PI 3.1415926


#define MAXP 1050
#define MAXK 1050
#define MAXL 1050

int btn[MAXK][MAXP];
int freq[MAXL];

int p,k,l;
VII ki;

int solve(){
	int rst=0;

	ki.clear();

	REP(i,l){	ki.PB(MP(freq[i],i));}

	sort(ALL(ki));
	reverse(ALL(ki));


	REP(j,p){
		REP(i,k){
			btn[i][j]=-1;
		}
	}

	int c=0;
	REP(j,p){
		if(c==l) break;
		REP(i,k){
			if(c==l) break;
			btn[i][j]=ki[c].SD;
			c++;
		}
	}
	
	REP(j,p){
		REP(i,k){
			if(btn[i][j]==-1) continue;
			rst+=freq[btn[i][j]]*(j+1);
		}
	}

	return rst;
}

int main(){


	ifstream in("input.txt");
	ofstream out("output.txt");

	long st = clock();
	string s;
	int nc;	in >> nc;

	REP(i,nc){	
		out<<"Case #"<<i+1<<": ";
		in>>p>>k>>l;
		REP(j,l) in>>freq[j];

		int rst=solve();
		out<<rst<<endl;
	}
	
	out.close();	
	cout<<"t: "<<(clock()-st);	
	return 0;
}




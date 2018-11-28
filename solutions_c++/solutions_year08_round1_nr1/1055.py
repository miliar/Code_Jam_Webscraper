#include <iostream>
#include <sstream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <list>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <complex>
#include <cstdio>
#include <cassert>
#include <cmath>

using namespace std;

#define FOR(i,a,b) for(int i=(a),_b=(b);i<=_b;i++)
#define REP(i,n) FOR(i,0,(n)-1)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;i--)
#define sz size()
template<class T> inline int size(const T& c) { return c.sz; }
#define FORA(i,c) REP(i,size(c))

#define itype(c) __typeof((c).begin())
#define FORE(e,c) for(itype(c) e=(c).begin();e!=(c).end();e++)
#define pb push_back
#define X first
#define Y second
#define mp make_pair
#define all(x) (x).begin(),(x).end()
#define SORT(x) sort(all(x))
#define REVERSE(x) reverse(all(x))
#define CLEAR(x,c) memset(x,c,sizeof(x)) 

typedef long long LL;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;
typedef vector<int>::iterator VIp;

LL s2i(string s) { istringstream i(s); LL x; i>>x; return x; }
template<class T> string i2s(T x) { ostringstream o; o << x; return o.str(); }
/*bool operator<( const int &a,const int &b){
	return a < b;
}*/

#define pi acos(-1.)
#define eps 1e-7

int main(){
	//char fname[]="C:\\Documents and Settings\\Administrator\\My Documents\\Visual Studio 2005\\Projects\\1\\input.txt";
	char fname[]="C:\\Documents and Settings\\Administrator\\My Documents\\Visual Studio 2005\\Projects\\1\\1\\A-small-attempt3.in";
	//	char fname[]="C:\\Documents and Settings\\Administrator\\My Documents\\Visual Studio 2005\\Projects\\1\\1\\A-small-attempt2.in";
	ifstream fin(fname);	
	if(!fin){
		cout << "Error.Can't open input data file."<< endl;
		exit(1);
	}

	int T;
	int n;
	int x[800],y[800];

	fin>>T;

	REP(num,T){
		fin>>n;
		CLEAR(x,0x00);
		CLEAR(y,0x00);
		REP(i,n) fin>>x[i];
		REP(j,n) fin>>y[j];
		
		sort(&x[0], &x[n]);
		sort(&y[0], &y[n]);
		
		long int ans=0;
		int nx=0,ny=0;
		REP(i,n){
			ans+=x[i]*y[n-i-1];
		}
		cout<<"Case #"<< num+1 <<": ";
		cout<< ans <<endl;	
	}
	fin.close();
	return 0;	
}

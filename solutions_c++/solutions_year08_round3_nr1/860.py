#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <fstream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

// typedefs
typedef vector<int> VI;
typedef vector<string> VS;
typedef long long LL;
typedef pair<int,int> PII;
typedef vector<LL> VLL;

// defines
#define SZ(x) x.size()
#define SWAP(x,y) (x)^=(y)^=(x)^=(y)
#define MAX(a,b)   (a)>(b)?(a):(b)
#define MIN(a,b)   (a)<(b)?(a):(b)
#define ABS(a) ((a)>0?(a):-(a))
#define STOI(s,d) istringstream(s)>>d
#define ITOS(d,s) {ostringstream t;t<<d;s=t.str();}
#define FOR(i,n) for(int i=0;i<n;i++)
#define FORI(i,a,b) for(int i=a;i<b;++i)
#define FORR(i,a,b) for(int i=a;i>=b;--i)
#define FORS(i,s) FOR(i,(int)s.length())
#define FORV(i,v) FOR(i,(int)SZ(v))

// common
int GCD(int a,int b){for(int c;b;c=a,a=b,b=c%b);return a;}
int LCM(int a,int b){return a/GCD(a,b)*b;}
const double pi = atan(1.0)*4.0;
const double eps = 1e-8;

// parsing,splitting
VS parse(const string &s, const string &delim = ", \t\n"){
  VS ret(0);
  for (int b,e=0;;ret.push_back(s.substr(b,e-b)))
    if ((b=s.find_first_not_of(delim,e))==(e=s.find_first_of(delim,b)))
      return ret;
}
VI parsei(const string &s, const string &delim=", \t\n"){
  VS tmp=parse(s,delim);
  VI ret(0);
  for (VS::iterator i=tmp.begin();i!=tmp.end();i++)
    {int t;STOI(*i,t);ret.push_back(t);}
  return ret;
}

inline bool isInteger(double value) {return value-floor(value) == 0 ? true:false;}

#define FILENAME "a-small-attempt0"

// my code
void testCase(int test, ifstream &in, ofstream &out) {
	//input params
	int P, L, K;
	in >> P >> K >> L;
	//printf("%d\n", n);
	
	VI F(L);
	FOR(i,L) in >> F[i];

	int cnt = 0;
	sort(F.begin(), F.end());
	reverse(F.begin(), F.end());
	
	cout << F[0] << endl;
	
	int keys[K][P];

	//work
	int r, c;
	r=c=1;
	bool ok = true;
	FOR(i,L) {
		//keys[r][c] = F[i];
		if (c>P) {
			ok = false;
			break;
		}
		cnt = cnt + (c * F[i]);
		//printf("%d at (%d,%d) for a cnt=%d\n", F[i], r, c, cnt);
		r++;
		if (r>K) {r=1; c++;}
	}
	
	//output
	if (ok) {
		out << "Case #" << (test+1) << ": " << cnt << endl;
		cout << "Case #" << (test+1) << ": " << cnt << endl;
	}
	else {
		out << "Case #" << (test+1) << ": " << "impossible" << endl;
		cout << "Case #" << (test+1) << ": " << "impossible" << endl;
	}
}

int main() {
	ifstream in(FILENAME ".in", ios::in);  // declare and open
	ofstream out("a-small.out", ios::out);
	int N;
	if (in.is_open())
  	{
		//test cases
		in >> N;
  		FOR(test,N) testCase(test, in, out);
    	in.close();
	}
	
	out.close();
	cin.get();
	return 0;
}

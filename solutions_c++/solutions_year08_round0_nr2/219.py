#define _USE_MATH_DEFINES
#include <iostream>
#include <fstream>
#include <sstream>
#include <iomanip>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <string>
#include <list>
#include <stack>
#include <queue>
#include <vector>
#include <deque>
#include <set>
#include <map>
using namespace std;

const int PINF = 1<<30;
const int NINF = -PINF;
const double EPSILON = 1e-10;
const double PI = M_PI;

typedef long long LL;
typedef vector<int> VI;
typedef pair<int,int> PII;
typedef vector<PII> VPII;
typedef vector<double> VD;
typedef pair<double,double> PDD;

#define ALL(a) (a).begin(), (a).end()
#define FOR(i,a,b) for (LL i=(a),_b(b); i<_b; ++i)
#define RFOR(i,a,b) for (int i=(a)-1,_b(b); i>=_b; --i)
#define FORV(i,v) for (int i=0; i<(v).size(); ++i)
#define ABS(a) ((a)>0?(a):-(a))
#define MAX(a,b) ((a)>(b)?(a):(b))
#define MIN(a,b) ((a)<(b)?(a):(b))
#define mp make_pair
#define pb push_back
#define sz size()
#define sqr(a) (a)*(a)
#define pow2(n) (1<<(n))
#define has(a,k) ((a).find(k)!=(a).end())


int gettime(string s)
{
	int h= 10*(s[0]-'0') + (s[1]-'0');
	int m= 10*(s[3]-'0') + (s[4]-'0');

	int t = h*60+m;
	return t;
}

int main()
{
	freopen("b.in","r",stdin);
	freopen("b.out","w",stdout);
	
	int TTT;
	cin >> TTT;
	FOR(ttt,0,TTT)
	{
		cout << "Case #" << ttt+1 << ": ";
		int NA,NB,T;

		cin >> T >> NA >> NB;

		VI As,Ae,Bs,Be;
		FOR(i,0,NA)
		{
			string s,e;
			cin >> s >> e;
			As.pb(gettime(s));
			Ae.pb(gettime(e)+T);
		}
		FOR(i,0,NB)
		{
			string s,e;
			cin >> s >> e;
			Bs.pb(gettime(s));
			Be.pb(gettime(e)+T);
		}

		sort(ALL(As));
		sort(ALL(Ae));
		
		sort(ALL(Bs));
		sort(ALL(Be));

		int cA=NA;
		int cB=NB;
	
		// delB
		int pAe=0;
		FOR(i,0,Bs.sz)
		{
			if (pAe>=Ae.sz) break;
			if (Ae[pAe]<=Bs[i]) { --cB; ++pAe; } 
		}
		// delA
		int pBe=0;
		FOR(i,0,As.sz)
		{
			if (pBe>=Be.sz) break;
			if (Be[pBe]<=As[i]) { --cA; ++pBe; } 
		}
		cout << cA << " " << cB << endl;
	}
	
	
	return 0;
}
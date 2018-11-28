//#pragma comment(linker, "/stack:1000000")

#include <string>
#include <vector>
#include <map>
#include <list>
#include <iterator>
#include <set>
#include <queue>
#include <iostream>
#include <sstream>
#include <stack>
#include <deque>
#include <cmath>
#include <memory.h>
#include <cstdlib>
#include <cstdio>
#include <cctype>
#include <algorithm>
#include <utility>

using namespace std;

#define FOR(i, a, b) for(int i = a; i < b; ++i)
#define RFOR(i, b, a) for(int i = b - 1; i >= a; --i)
#define REP(i, N) FOR(i, 0, N)
#define RREP(i, N) RFOR(i, N, 0)

#define MIN(A, B) ((A) < (B) ? (A) : (B))
#define MAX(A, B) ((A) > (B) ? (A) : (B))
#define ABS(A) ((A) < 0 ? (-(A)) : (A))
#define ALL(V) V.begin(), V.end()
#define SIZE(V) (int)V.size()
#define pb push_back
#define mp make_pair
#define EPS 1e-7
#define Pi 3.14159265358979
#define FILL(a,v) memset(a,v,sizeof(a))

typedef long long Long;
typedef unsigned long long ULong;
typedef unsigned int Uint;
typedef unsigned char Uchar;
typedef vector <int> VI;
typedef pair <int, int> PII;

string s[200];
int tg[200];
int tw[200];
double wp[200];
double owp[200];
double oowp[200];
int n;

void sol()
{
	FILL(tg, 0);
	FILL(tw, 0);
	cin>>n;
	REP(i,n)
		cin>>s[i];

	REP(i,n)
		REP(j,n)
			if(s[i][j] != '.')
			{
				tg[i]++;
				if(s[i][j] == '1')
					tw[i]++;
			}

	REP(i,n)
		wp[i] = (tw[i]+.0)/tg[i];

	REP(i,n)
	{
		double os = 0;
		REP(j,n)
			if(s[i][j] != '.')
				if(s[i][j] == '1')
					os += tw[j]/(tg[j]-1.);
				else
					os += (tw[j]-1)/(tg[j]-1.);
		owp[i] = os/tg[i];
	}

	REP(i,n)
	{
		double os = 0;
		REP(j,n)
			if(s[i][j] != '.')
				os += owp[j];
		oowp[i] = os/tg[i];
	}

	REP(i,n)
		cout<<(wp[i]+2*owp[i] + oowp[i])/4<<endl;
}

int main(int argc, char** argv)
{
	int T;
	cin >> T;
	cout.precision(9);
	REP(i,T)
	{
		cout<<"Case #"<<i+1<<":"<<endl;
		sol();
	}
	return 0;
}
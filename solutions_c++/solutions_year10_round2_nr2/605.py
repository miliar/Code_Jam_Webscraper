#include <vector>
#include <string>
#include <algorithm>
#include <stack>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <sstream>
#include <cmath>
#include <cassert>
#include <fstream>
using namespace std;
 
#define MSG(a)  cout << #a << "=" << a << endl;
#define VAR(a,b) __typeof(b) a=b
#define FORIT(it,v) for(VAR(it,(v).begin());it!=(v).end();++(it))
template<class T, class U> T cast (U x) { T y; ostringstream a; a<<x; 
istringstream b(a.str()); b>>y; return y; }
#define SZ(v) ((int)(v).size())
#define FU(i,a,b) for(int i=(a);i<int(b);++i)
#define FD(i,a,b) for(int i=(a);i>=int(b);--i)
#define REP(i,n) FU(i,0,n)
#define ALL(a) a.begin(),a.end()
#define ISS istringstream
#define OSS ostringstream

int N,K,B,T;

const int IMP = -2;

int memo[51][51];

struct Chick
{
	int x;
	int v;
};

bool operator<(const Chick& a, const Chick& b)
{
	return a.x < b.x;
}

vector<Chick> chicks;

int CanMake(int i)
{
	return chicks[i].x + chicks[i].v*T >= B;
}

int S(int n, int k)
{
	if( k == 0 ) return 0;
	if( n == -1 && k > 0 ) 
	{
		return IMP;
	}
	
	if(memo[n][k] != -1) return memo[n][k];

	if (CanMake(n))
	{
		if( S(n-1, k-1) == IMP ) memo[n][k] = IMP;
		else memo[n][k] = S(n-1,k-1);
	}
	else
	{
		if ( S(n-1,k) == IMP ) memo[n][k] = IMP;
		else memo[n][k] = k+S(n-1,k);
	}
	
	return memo[n][k];
}

void main()
{
	ifstream in("in.txt");
  ofstream out("out.txt");

	int C;
	in >> C;

	REP(zzz,C)
	{
		out << "Case #" << zzz+1 << ": ";

		in >> N >> K >> B >> T;
		
		chicks = vector<Chick>(N);

		FU(i,0,N) in >> chicks[i].x;
		FU(i,0,N) in >> chicks[i].v; 

		FU(i,0,51) FU(j,0,51) memo[i][j] = -1;

		if(S(N-1,K) == IMP) out << "IMPOSSIBLE" << endl;
		else out << S(N-1,K) << endl;
	}
}
#define _USE_MATH_DEFINES
#include <iostream>
#include <fstream>
#include <sstream>
#include <iomanip>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <utility>
#include <algorithm>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <list>
using namespace std;

typedef long long LL;
typedef long double LD;
typedef vector<int> VI;
typedef pair<int,int> PII;
typedef vector<PII> VPII;
typedef vector<LD> VD;
typedef pair<LD,LD> PDD;
typedef vector<PDD> VPDD;

const int PINF = 1<<30;
const int NINF = -PINF;
const LD EPSILON = 1e-10;
const LD PI = M_PI;

#define mp make_pair
#define pb push_back
#define sz size() 
#define sqr(a) (a)*(a)
#define ALL(a) (a).begin(), (a).end()
#define RALL(a) (a).rbegin(), (a).rend()
#define MAX(a,b) ((a)>(b)?(a):(b))
#define MIN(a,b) ((a)<(b)?(a):(b))
#define ABS(a) ((a)>0?(a):-(a))
#define HAS(a,k) ((a).find(k)!=(a).end())
#define POW2(a) (LL)(((LL)(1))  << (a))
#define FOR(i,a,b) for (int i=(a),_b(b); i<_b; ++i)
#define RFOR(i,a,b) for (int i=(a)-1,_b(b); i>=_b; --i)
#define FORV(i,v) FOR(i,0,(v).sz)

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int TTT;
	cin >> TTT;
	
FOR(ttt,1,TTT+1)
{
	cout << "Case #" << ttt << ": ";
//-----------------------------------------------------------------------------------------------------------	
	
	int N,M;
	LD X;
	cin >> N >> M >> X;
	
	FOR(x1,0,N+1)
	FOR(y1,0,M+1)
	FOR(x2,0,N+1)
	FOR(y2,0,M+1)
	if (x1!=x2 || y1!=y2)
	{
		LD a=sqrt((LD)sqr(x1)+(LD)sqr(y1));
		LD b=sqrt((LD)sqr(x2)+(LD)sqr(y2));
		LD c=sqrt((LD)sqr(x1-x2)+(LD)sqr(y1-y2));
		LD p=(a+b+c)/2.0;
		if (ABS(sqrt(p*(p-a)*(p-b)*(p-c))-X/2.0)<EPSILON)
		{
			cout << 0 << " " << 0 << " " << x1 << " " << y1 << " " << x2 << " " << y2 ;
			goto goto1;
		}
	}
	cout << "IMPOSSIBLE";
goto1:	cout << endl;
//-----------------------------------------------------------------------------------------------------------
}	
	return 0;
}
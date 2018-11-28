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

const int PINF = 1<<28;
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
	string S;
	int K;
	cin >> K >> S; 
	int U=PINF;
	VI P(K);
	FOR(i,1,K+1) P[i-1]=i-1;
	do
	{
		string S2; S2.resize(S.sz);
		for (int i=0; i<S.sz; i+=K)
		{
			FOR(j,0,K)
			{
				S2[i+j]=S[i+P[j]];
			}
		}

		int r=1;
		FOR(i,1,S2.sz) if (S2[i]!=S2[i-1]) ++r;
	
		U=MIN(U,r);
	}while (next_permutation(ALL(P)));
	cout << U << endl;
//-----------------------------------------------------------------------------------------------------------
}	
	return 0;
}
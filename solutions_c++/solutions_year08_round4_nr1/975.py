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

int M,W;


int V[2][20000];
int C[20000];
int B[20000];
int G[20000];

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
	cin >> M >> W;
	FOR(i,0,M) B[i]=0,C[i]=0,V[0][i]=PINF,V[1][i]=PINF;
	FOR(i,0,M)
	{
		if (i<M/2)
		{ // node
			int g,c;
			cin >> g >> c;
			G[i]=g;
			C[i]=c;
		}
		else
		{ // leaf
			int a; cin >>a;
			B[i]=1;
			V[a][i]=0;
			V[1-a][i]=PINF;
		}
	}
	
	RFOR(i,M,0) if (!B[i])
	{
		B[i]=1;
		int L=((i+1)<<1)-1,R=((i+1)<<1);
		// node is AND
		if (G[i])
		{
			if (V[0][L]!=PINF && V[0][R]!=PINF)   V[0][i]= MIN(V[0][i], V[0][L]+V[0][R]);
			if (V[1][L]!=PINF && V[0][R]!=PINF)   V[0][i]= MIN(V[0][i], V[1][L]+V[0][R]);
			if (V[0][L]!=PINF && V[1][R]!=PINF)   V[0][i]= MIN(V[0][i], V[0][L]+V[1][R]);
			if (V[1][L]!=PINF && V[1][R]!=PINF)   V[1][i]= MIN(V[1][i], V[1][L]+V[1][R]);

			if (C[i])
			{
				if (V[0][L]!=PINF && V[0][R]!=PINF)   V[0][i]= MIN(V[0][i], V[0][L]+V[0][R] +1);
				if (V[1][L]!=PINF && V[0][R]!=PINF)   V[1][i]= MIN(V[1][i], V[1][L]+V[0][R] +1);
				if (V[0][L]!=PINF && V[1][R]!=PINF)   V[1][i]= MIN(V[1][i], V[0][L]+V[1][R] +1);
				if (V[1][L]!=PINF && V[1][R]!=PINF)   V[1][i]= MIN(V[1][i], V[1][L]+V[1][R] +1);
			}
		}//OR
		else
		{
			if (V[0][L]!=PINF && V[0][R]!=PINF)   V[0][i]= MIN(V[0][i], V[0][L]+V[0][R] );
			if (V[1][L]!=PINF && V[0][R]!=PINF)   V[1][i]= MIN(V[1][i], V[1][L]+V[0][R] );
			if (V[0][L]!=PINF && V[1][R]!=PINF)   V[1][i]= MIN(V[1][i], V[0][L]+V[1][R] );
			if (V[1][L]!=PINF && V[1][R]!=PINF)   V[1][i]= MIN(V[1][i], V[1][L]+V[1][R] );

			if (C[i])
			{
				if (V[0][L]!=PINF && V[0][R]!=PINF)   V[0][i]= MIN(V[0][i], V[0][L]+V[0][R]+1);
				if (V[1][L]!=PINF && V[0][R]!=PINF)   V[0][i]= MIN(V[0][i], V[1][L]+V[0][R]+1);
				if (V[0][L]!=PINF && V[1][R]!=PINF)   V[0][i]= MIN(V[0][i], V[0][L]+V[1][R]+1);
				if (V[1][L]!=PINF && V[1][R]!=PINF)   V[1][i]= MIN(V[1][i], V[1][L]+V[1][R]+1);
			}
		}
		//

	}
	if (V[W][0]!=PINF) cout << V[W][0] << endl;
	else cout << "IMPOSSIBLE" << endl;
	
	
//-----------------------------------------------------------------------------------------------------------
}	
	return 0;
}
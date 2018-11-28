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



string getLine()
{
	char c[1000];
	cin.getline(c,1000);
	string r(c);
	return r;
}

int getNum()
{
	string s = getLine();
	istringstream iss(s);
	int t;
	iss >> t;
	return t;
}

int main()
{
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	int N;
	N = getNum();

	int A[110][1010];
	FOR(ttt,1,N+1)
	{
		int S,Q;
		S=getNum();

		map<string,int> M;
		FOR(i,0,S)
		{
			string s=getLine();
			M[s]=i;
		}
		Q=getNum();
		
		if (!Q)
		{
			cout << "Case #" << ttt << ": " << 0 << endl;
			continue;
		}
		string s;
		FOR(i,0,S) FOR(j,0,Q) A[i][j]=0; 
		FOR(i,1,Q+1)
		{
			s=getLine();
			int idx=M[s];

			FOR(k,0,S) 
			{
				if (idx==k)
				{
					int min=PINF;
					FOR(j,0,S) if (min>A[j][i-1] && j!=k) min = A[j][i-1];
					A[k][i] = min+1;
				}
				else
				{
					A[k][i] = A[k][i-1];
				}
			}
		}
		int min=A[0][Q];
		FOR(j,1,S) if (min>A[j][Q]) min = A[j][Q];
		cout << "Case #" << ttt << ": " << min << endl;
	}
	
	return 0;
}
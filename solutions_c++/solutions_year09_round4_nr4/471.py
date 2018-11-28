#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <algorithm>
#include <cmath>
using namespace std;

typedef long long LL;
typedef vector<int> VI;
typedef pair<int,int> PII;

#define pb push_back
#define mp make_pair
#define FOR(i,a,b) for(int i=(a),_b(b); i<_b; ++i)
#define RFOR(i,a,b) for(int i=(a)-1,_b(b); i>=_b; --i)
#define CLR(a,v) memset((a),(v),sizeof(a))
#define CPY(a,b) memcpy((a),(b),sizeof(a))
#define MIN(a,b) ((a)<(b)?(a):(b))
#define MAX(a,b) ((a)>(b)?(a):(b))
#define ABS(a) ((a)<(0)?-(a):(a))

int C[128][128];
int N,K;

int A[128][128];
char ch[1024];
int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);

	int TTT; scanf("%d",&TTT);
	int CASE=0;
	while(TTT--)
	{
		++CASE;
		scanf("%d",&N);
		//FOR(i,0,N)
		//	FOR(j,0,K) scanf("%d",&A[i][j]);
		int X[16],Y[16],R[16];
		FOR(i,0,N) scanf("%d%d%d",X+i,Y+i,R+i);
		double r=1e100;
		if (N<=2) r=MAX(R[0],R[1]);
		else
		{
			double v;
			FOR(a,0,3) FOR(b,0,3) if (b-a) FOR(c,0,3) if (c-b && c-a)
			{
				v=MAX(R[c], (hypot(X[a]-X[b],Y[a]-Y[b])+R[a]+R[b])/2.0);
				r=MIN(r,v);
			}
		}
		printf("Case #%d: %.6lf\n",CASE,r);
	}
	


	return 0;
}
using namespace std;

#include <set>
#include <map>
#include <list>
#include <deque>
#include <stack>
#include <queue>
#include <cmath>
#include <ctime>
#include <cctype>
#include <cstdio>
#include <vector>
#include <string>
#include <bitset>
#include <utility>
#include <iomanip>
#include <fstream>
#include <cstring>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <functional>

#define oo 1<<30
#define f first
#define s second
#define II inline
#define db double
#define ll long long
#define pb push_back
#define mp make_pair
#define Size(V) ((int)(V.size()))
#define all(v) v.begin() , v.end()
#define CC(v) memset((v),0,sizeof((v)))
#define CP(v,w) memcpy((v),(w),sizeof((w)))
#define FOR(i,a,b) for(int (i)=(a);(i)<=(b);++(i))
#define REP(i, N) for (int (i)=0;(i)<(int)(N);++(i))
#define FORit(it, x) for (__typeof((x).begin()) it = (x).begin(); it != (x).end(); ++it)

#define IN "code.in"
#define OUT "code.out"
#define N_MAX (1<<7)

typedef vector<int> VI;
typedef pair<int,int> pi;
typedef vector<string> VS;
template<class T> string toString(T n) {ostringstream ost;ost<<n;ost.flush();return ost.str();}

int T,R;
int C[N_MAX][N_MAX],A[N_MAX][N_MAX];

II void scan()
{
	freopen(IN,"r",stdin);
	freopen(OUT,"w",stdout);
	scanf("%d",&T);
}

II void solve(int TestCase)
{
	int x1,y1,x2,y2;
	
	scanf("%d",&R);
	FOR(i,1,R)
	{
		scanf("%d%d%d%d",&x1,&y1,&x2,&y2);
		
		FOR(k1,x1,x2)
		FOR(k2,y1,y2)
			A[k1][k2] = true;
	}
	
	int rez = 1;
	for(;;++rez)
	{
		CC(C);
		
		FOR(i,1,100)
		FOR(j,1,100)
			if(A[i][j] == true && !A[i-1][j] && !A[i][j-1])
				C[i][j] = -1;
			else if(A[i][j] == false && A[i-1][j] && A[i][j-1])
				C[i][j] = 1;
		
		FOR(i,1,100)
		FOR(j,1,100)
			if(C[i][j] == 1)
				A[i][j] = true;
			else if(C[i][j] == -1)
				A[i][j] = false;
		
		bool ok = false;
		FOR(i,1,100)
		FOR(j,1,100)
			if(A[i][j])
				ok = true;
		if(!ok)
			break;
	}
	
	
	printf("Case #%d: %d\n",TestCase,rez);
}

int main()
{
	scan();
	FOR(i,1,T)
		solve(i);
	return 0;
}

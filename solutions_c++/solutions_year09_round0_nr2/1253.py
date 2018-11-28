using namespace std;

#include <set>
#include <map>
#include <list>
#include <deque>
#include <stack>
#include <queue>
#include <cmath>
#include <cstdio>
#include <vector>
#include <string>
#include <bitset>
#include <utility>
#include <algorithm>

#define pb push_back
#define sz size
#define f first
#define s second
#define II inline
#define ll long long
#define db double
#define FOR(i,a,b) for(int i=a;i<=b;++i)
#define all(v) v.begin() , v.end()
#define CC(v) memset((v),0,sizeof((v)))
#define CP(v,w) memcpy((v),(w),sizeof((w)))
#define mp make_pair

#define IN "code.in"
#define OUT "code.out"
#define N_MAX 1<<7


typedef vector<int> VI;
typedef pair<int,int> pi;
typedef vector<string> VS;
typedef vector<pi> dataT;

int T,N,M,next;
int C[N_MAX][N_MAX],S[N_MAX][N_MAX];
vector< vector< dataT > > A; 


const int xx[] = {-1,0,0,1};
const int yy[] = {0,-1,1,0};

II void scan()
{
//	freopen(IN,"r",stdin);
//	freopen(OUT,"w",stdout);
	scanf("%d\n",&T);
}

II int ok(int x,int y)
{
	if(x < 1 || x > N || y < 1 || y > M)
		return (1<<30);
	return C[x][y];
}

II void fill(int x,int y)
{
	S[x][y] = next;
	
	for(vector<pi>::iterator it = A[x][y].begin();it != A[x][y].end();++it)
	{
		if(S[it->f][it->s])
			continue;
		fill(it->f,it->s);
	}
}

II void solve(int TestCase)
{
	scanf("%d%d\n",&N,&M);
	CC(C);
	CC(S);
	A.clear();
	A.resize(0);
	A.resize(N+1);
	
	FOR(i,1,N)
	{
		A[i].resize(M+1);
		FOR(j,1,M)
		{
			A[i][j].resize(0);
			scanf("%d",&C[i][j]);
		}
	}
	
	FOR(i,1,N)
	FOR(j,1,M)
	{
		int val = min( min( ok(i-1,j),ok(i,j-1) ),min( ok(i+1,j),ok(i,j+1) ) );
		if(val >= C[i][j])
			continue;
		
		for(int k = 0;k < 4;++k)
			if( C[ i + xx[k] ][ j + yy[k] ] == val && ok(i + xx[k],j +yy[k]) < (1<<20) )
			{
				A[ i + xx[k] ][ j + yy[k] ].pb( mp(i,j) );
				A[i][j].pb( mp( i + xx[k] , j + yy[k] ) );
				break;
			}
	}
	
	next = 'a' - 1;
	
	FOR(i,1,N)
	FOR(j,1,M)
		if(!S[i][j])
			++next,fill(i,j);
	
	printf("Case #%d:\n",TestCase);
	FOR(i,1,N)
	{
		FOR(j,1,M-1)
			printf("%c ",S[i][j]);
		printf("%c\n",S[i][M]);
	}   
	
}

int main()
{
	scan();
	FOR(i,1,T)
		solve(i);
	return 0;
}

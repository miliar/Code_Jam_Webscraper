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

#define T_MAX (1<<9)
#define D_MAX (1<<13)
#define L_MAX (1<<4)
#define SIGMA 26

typedef vector<int> VI;
typedef pair<int,int> pi;
typedef vector<string> VS;

int L,D,N;
int Dbit[L_MAX][D_MAX];
char buffer[1<<20];

II void scan()
{
//	freopen(IN,"r",stdin);
//	freopen(OUT,"w",stdout);
	
	scanf("%d%d%d\n",&L,&D,&N);
	
	FOR(i,1,D)
	{
		fgets(buffer,1<<20,stdin);
		
		for(int j = 0;j < L;++j)
			Dbit[j][i] = 1<<(buffer[j] - 'a');
	}
}

II void solve(int TestCase)
{
	fgets(buffer,1<<20,stdin);
	
	int Cbit[L_MAX] = {0};
	int rez = 0,next = 0;
	
	for(int j = 0;j < L;++j)
		if(buffer[next] == '(')
		{
			for(;buffer[++next] != ')';)
				Cbit[j] ^= 1<<(buffer[next] - 'a');
			++next;
		}
		else
			Cbit[j] = 1<<(buffer[next++] - 'a');
	
	FOR(i,1,D)
	{
		bool ok = true;
		
		for(int j = 0;j < L && ok;++j)
			if( !(Cbit[j] & Dbit[j][i]) )
				ok = false;
		if(ok)
			++rez;
	}
	
	printf("Case #%d: %d\n",TestCase,rez);
}

int main()
{
	scan();
	FOR(i,1,N)
		solve(i);
	
	return 0;
}

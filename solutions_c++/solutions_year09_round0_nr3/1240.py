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

#define IN  "code.in"
#define OUT "code.out"
#define mod 10000

typedef vector<int> VI;
typedef pair<int,int> pi;
typedef vector<string> VS;

int T;

const char SMEN[] = "welcome to code jam";
char buffer[1<<10];
int C[1<<10],D[1<<10];

II void scan()
{
//	freopen(IN,"r",stdin);
//	freopen(OUT,"w",stdout);
	scanf("%d\n",&T);
}

II void solve(int TestCase)
{
	fgets(buffer,1<<10,stdin);
	int N = 0;
	
	for(int i = 0;buffer[i] != '\n' && buffer[i] != '\0';N = i,++i);
	FOR(i,0,N)
		if(buffer[i] == 'm')
			C[i] = 1;
	
	for(int Ti = 17;Ti >= 0;--Ti)
	{
		FOR(i,0,N)
		{
			if(buffer[i] != SMEN[Ti])
				continue;
			int sum = 0;
			FOR(j,i+1,N)
				if(buffer[j] == SMEN[Ti+1])
					sum = (sum + C[j]) % mod;
			D[i] = sum;
		}
		
		CP(C,D);
	}
	
	int rez = 0;
	FOR(i,0,N)
		if(buffer[i] == 'w')
			rez = (rez + C[i]) % mod;
	printf("Case #%d: %04d\n",TestCase,rez);
}

int main()
{
	scan();
	FOR(i,1,T)
		solve(i);
	return 0;
}

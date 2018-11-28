using namespace std;

#include <set>
#include <map>
#include <list>
#include <deque>
#include <stack>
#include <queue>
#include <cmath>
#include <cctype>
#include <cstdio>
#include <vector>
#include <string>
#include <bitset>
#include <utility>
#include <iomanip>
#include <cstring>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <functional>

#define pb push_back
#define size(V) ((int)(V.size()))
#define f first
#define s second
#define II inline
#define ll long long
#define db double
#define FORit(it, x) for (__typeof((x).begin()) it = (x).begin(); it != (x).end(); ++it)
#define REP(i, N) for (int i = 0; i < (int)(N); ++i)
#define FOR(i,a,b) for(int i=a;i<=b;++i)
#define all(v) v.begin() , v.end()
#define CC(v) memset((v),0,sizeof((v)))
#define CP(v,w) memcpy((v),(w),sizeof((w)))
#define mp make_pair
#define oo 1<<30

#define IN "code.in"
#define OUT "code.out"

typedef vector<int> VI;
typedef pair<int,int> pi;
typedef vector<string> VS;
template<class T> string toString(T n) {ostringstream ost;ost<<n;ost.flush();return ost.str();}
typedef vector<string> VS;

int T;
int C[1<<7];

II void scan()
{
	freopen(IN,"r",stdin);
	freopen(OUT,"w",stdout);
	
	scanf("%d",&T);
}

II void solve(int TestCase)
{
	int N,last;
	char aux;
	scanf("%d\n",&N);
	
	FOR(i,1,N)
	{
		last = 0;
		
		FOR(j,1,N)
		{
			scanf("%c",&aux);
			if(aux == '1')
				last =  j;
		}
		
		scanf("%c",&aux);
		C[i] = last;
	}
	
	int rez = 0;
	
	FOR(i,1,N)
		if(C[i] > i)
		{
			FOR(i2,i+1,N)
				if(C[i2] <= i)
				{
					FOR(k,i+1,i2)
					{
						swap(C[i],C[k]);
						++rez;
					}	
					
					break;
				}	
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

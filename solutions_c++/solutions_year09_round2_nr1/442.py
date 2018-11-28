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
#define FOR(i,a,b) for(int i=a;i<=b;++i)
#define all(v) v.begin() , v.end()
#define CC(v) memset((v),0,sizeof((v)))
#define CP(v,w) memcpy((v),(w),sizeof((w)))
#define mp make_pair
#define mod 654321
#define oo 1<<30

#define IN "code.in"
#define OUT "code.out"

typedef vector<int> VI;
typedef pair<int,int> pi;
typedef vector<string> VS;
template<class T> string toString(T n) {ostringstream ost;ost<<n;ost.flush();return ost.str();}
typedef vector<string> VS;

int T;

II void scan()
{
	freopen(IN,"r",stdin);
	freopen(OUT,"w",stdout);
	scanf("%d\n",&T);
}

II void solve(int TestCase)
{
	int N;
	char A[1<<6];
	fgets(A+1,1<<6,stdin);
	
	for(int i = 1;A[i] >= '0' && A[i] <= '9';N = i,++i);
	FOR(i,1,N) A[i] -= '0';
	
	bool ok = false;
	FOR(i,1,N-1)
		if(A[i] < A[i+1])
			ok = true;
	
	printf("Case #%d: ",TestCase);
		
	if(!ok)
	{
		sort(A+1,A+N+1);
		
		if(!A[1])
		{
			pi poz1 = mp(10,0);
			FOR(i,2,N)
				if(A[i] && A[i] < poz1.f)
					poz1 = mp(A[i],i);
			swap(A[1],A[poz1.s]);
		}	
		
		printf("%d0",A[1]);
		FOR(i,2,N)
			printf("%d",A[i]);
		printf("\n");
		return;
	}	
	
	pi poz1,poz2;
	
	for(poz1.s = N;poz1.s >= 1;--poz1.s)
	{
		poz1 = mp(A[poz1.s],poz1.s),poz2 = mp(10,0);

		FOR(i,poz1.s+1,N)
			if(A[i] > poz1.f && A[i] <= poz2.f)
				poz2 = mp(A[i],i);
	
		if(poz2.f != 10)
			break;
	}
	
	swap(A[poz1.s],A[poz2.s]);
	sort(A+poz1.s+1,A+N+1);
	
	FOR(i,1,N)
		printf("%d",A[i]);
	printf("\n");
}

int main()
{
	scan();
	FOR(i,1,T)
		solve(i);
	return 0;
}

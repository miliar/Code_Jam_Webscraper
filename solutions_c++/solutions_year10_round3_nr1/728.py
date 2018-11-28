#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <string>
#include <ctime>
#include <cassert>
#include<climits>

using namespace std;

#define SZ(a) int((a).size())
#define PB push_back
#define MP make_pair
#define ALL(c) (c).begin(),(c).end()
#define TR(c,i) for(typeof((c).begin() i = (c).begin(); i != (c).end(); i++)
#define PRESENT(c,x) ((c).find(x) != (c).end())
#define FOR(i,a,b) for(int i=(int)a;i<(int)b;i++)
#define REV(i,a,b) for(int i=(int)a;i>(int)b;i--)
#define REP(i,n) for(int i=0;i<(int)n;i++)
#define SETBIT(a,b) a|=(1<<b)
#define UNSETBIT(a,b) a&=~(1<<b)
#define GETBIT(a,b) a&(1<<b)
#define FILL(a,b) memset(a,b,sizeof(a))
#define NBITS(a) __builtin_popcount(a)
#define INF 1000000000
#define EPS 1e-9
typedef long long LL;
typedef pair<int,int> PII;
vector<int> VI;
vector<vector<int> > VVI;
vector<string> VS;

////////// ACUTAL CODE STARTS HERE /////////
#define MAXN 10005
bool there[MAXN];
pair<LL,LL> A[MAXN];
LL N,ans;
int main()
{
	//freopen("A_in.txt","r",stdin);					 freopen("A_out.txt","w",stdout);
	//freopen("A-small-attempt0.in","r",stdin);freopen("A-small-attempt0OUT.out","w",stdout);
	//freopen("A-small-attempt1.in","r",stdin);freopen("A-small-attempt1OUT.out","w",stdout);
	//freopen("A-small-attempt2.in","r",stdin);freopen("A-small-attempt2OUT.out","w",stdout);
	freopen("A-large.in","r",stdin);freopen("A-largeOUT.out","w",stdout);
	
	int Tests;
	cin>>Tests;
	REP(tests,Tests)
	{
		cin>>N;
		REP(i,N) cin>>A[i].first>>A[i].second;
		sort(A,A+N);
		FILL(there,false);
		ans=0ll;
		REP(i,N)
		{
			LL temp=0ll;
			FOR(j,A[i].second+1,10001) if(there[j]) temp++;
			ans+=temp;
			there[A[i].second]=true;
		}
		cout<<"Case #"<<tests+1<<": "<<ans<<endl;
	}
	return 0;
}

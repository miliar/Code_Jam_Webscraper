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

int L,P,C;

int find()
{
	int div=0;
	int temp=L;
	while(temp<P) {temp*=C;div++;}
	int ret=0;
	for(ret=0;1<<ret <div;ret++);
	return ret;
}

int main()
{
	//freopen("B_in.txt","r",stdin);					 freopen("B_out.txt","w",stdout);
	freopen("B-small-attempt0.in","r",stdin);freopen("B-small-attempt0OUT.out","w",stdout);
	//freopen("B-small-attempt1.in","r",stdin);freopen("B-small-attempt1OUT.out","w",stdout);
	//freopen("B-small-attempt2.in","r",stdin);freopen("B-small-attempt2OUT.out","w",stdout);
	//freopen("B-large.in","r",stdin);				 freopen("B-largeOUT.out","w",stdout);

	int Tests;
	cin>>Tests;
	REP(tests,Tests)
	{
		cin>>L>>P>>C;
		cout<<"Case #"<<tests+1<<": "<<find()<<endl;
	}
 	return 0;
}

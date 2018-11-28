
#include <cstdio>
#include <iostream>
#include <cmath>
#include <string>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <queue>
#include <sstream>
#include <iterator>
#include <cstdlib>
#include <cstring>
#include <utility>
#include <cctype>
#include <limits>
#include<ctime>

using namespace std;

const double EPS = 1e-9;
//const long long  INF = 1000000000000000000;

typedef pair<int, int> PII;
typedef pair<double,double> PDD;
typedef vector<long long> VLL;
typedef vector<int> VI;

#define FOR(i,a,b) for (int _n(b), i(a); i < _n; i++)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;--i)
#define REP(i,n) FOR(i,0,n)

#define UNIQUE(v) SORT(v), v.erase(unique(v.begin(),v.end()),v.end())
#define SORT(c) sort((c).begin(),(c).end())
#define ll long long

const int MN = 27;
ll v[MN];
const int MNN = (1<<20)+ 7;
ll d[MNN];
pair<ll,int> fr[MNN];


void print(int s,int N)
{
	REP(k,N) if((1<<k)&s) printf("%d ",v[k]);
	printf("\n");
}

void solve(int t)
{
	int N,mask1=-1,mask2=-1;
	cin>>N; REP(i,N) cin>>v[i];
	memset(d,0,sizeof(d));

	REP(sum,1<<N) REP(k,N)
	{
		int next = sum|(1<<k);
		if(next == sum) continue;
		d[next] = d[sum] + v[k];
	}

	REP(s,1<<N) fr[s] = make_pair<int,int>(d[s],s);

	sort(fr,fr+(1<<N));
	int m = unique(fr,fr+(1<<N)) - fr;
	
	FOR(i,1,m)
	{
		if(fr[i].first == fr[i-1].first)
		{
			mask1 = fr[i].second, mask2 = fr[i-1].second;
			break;
		}
	}

	printf("Case #%d:\n",t);

	if(mask1 == -1)
	{
		printf("Impossible\n");
	}
	else
	{
		print(mask1,N);
		print(mask2,N);
	}
}

int main()
{
#ifdef LocalHost
	freopen("input.txt","r",stdin);
	//freopen("output.txt","w",stdout);
#endif

	freopen("input.txt","r",stdin);
	freopen("output_c_easy.txt","w",stdout);

	int T;
	cin>>T;

	REP(t,T)
	{
		solve(t+1);
	}

#ifdef LocalHost
	//cout<<endl<<endl<<"TIME: "<<clock()<<endl;
#endif

}
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
#include <memory.h>
#include <iostream> 
#include <iomanip> 
#include <cstdio> 
#include <cmath> 
#include <cstdlib> 
#include <ctime> 
using namespace std; 

const int inf = 1000*1000*1000; 
#define CL(x,a) memset(x,a,sizeof(x)); 
#define ALL(v) (v).begin(),(v).end() 
#define PII pair<int,int> 
#define PDI pair<double,int> 
#define MP(a,b) make_pair(a,b) 
#define FOR(i,n) for(int i=0;i<n;i++) 
typedef long long LL; 
typedef vector<int> vi; 
typedef vector< vi > vvi; 
typedef vector< vector<PII > > vvpii; 
map<int,int> mp;
int n;
int name[100009];
int D;
int marker;
int ID(int x)
{
	if(mp[x] == 0)
	{
		if (marker)
			cerr << "govno";
		mp[x] = mp.size();
		name[mp[x]-1] = x;
	}
	return mp[x] - 1;
}
const int N = 1<<17;
unsigned ar[1<<18];
void update(int L,int R,unsigned val)
{
	L+=N;
	R+=N;
	for(;L<R;L>>=1,R>>=1)
	{
		if (L&1)
		{
			ar[L]=min(ar[L],val);
			L++;
		}
		if (R&1)
		{
			R--;
			ar[R] = min(ar[R],val);
		}
	}
}
int query(int x)
{
	x+=N;
	unsigned res = -1;
	for(;x;x>>=1)
	{
		res = min(res,ar[x]);
	}
	return res;
}
set<int,greater<int> > st;
void Solve()
{
	st.clear();
	marker = 0;
	CL(ar,-1);
	mp.clear();
	scanf("%d",&n);
	vector<pair<int,int> > v;
	FOR(i,n)
	{
		int L,d;
		scanf("%d%d",&L,&d);
		v.push_back(MP(d,L));
	}
	scanf("%d",&D);
	vector<int> tv;
	tv.push_back(0);
	st.insert(0);
	tv.push_back(D);
	st.insert(D);
	tv.push_back(v[0].second*2);
	st.insert(v[0].second*2);
	FOR(i,v.size())
	{
		//tv.push_back(v[i].first+v[i].second);
		tv.push_back(v[i].second);
		tv.push_back(v[i].second+1);
		//st.insert(v[i].first+v[i].second);
		st.insert(v[i].second);
		st.insert(v[i].second+1);
	}
	sort(ALL(tv));
	FOR(i,tv.size())
		ID(tv[i]);
	marker = 1;
	update(ID(v[0].second+1),ID(v[0].second*2)+1,v[0].second);
	FOR(i,v.size())
		swap(v[i].first,v[i].second);
	sort(ALL(v));
	FOR(i,v.size())
	{
		unsigned t = query(ID(v[i].first));
		if (t == (unsigned)-1)
		{
			continue;
		}

		int Len = v[i].first - t;
		if (Len > v[i].second)
			Len = v[i].second;
		update(ID(v[i].first+1),ID(*st.lower_bound(v[i].first+Len))+1,v[i].first);
	}
	if (query(ID(D)) == (unsigned) -1)
		printf("NO\n");
	else
		printf("YES\n");
}
int main() 
{ 
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	int T;
	scanf("%d",&T);
	FOR(i,T)
	{
		printf("Case #%d: ",i+1);
		Solve();
	}
	return 0; 
}

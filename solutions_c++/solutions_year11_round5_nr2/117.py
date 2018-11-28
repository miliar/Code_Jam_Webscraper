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

int dp[1024][1024];
int DP(int pos, int Len)
{
	if (dp[pos][Len] != -1)
		return dp[pos][Len];
}
vector<int> v;
map<int,int> mp;
bool Check(int x, map<int,int> mp)
{
	multiset<int> st;
	int now = -inf;
	for (map<int,int>::iterator it = mp.begin();it!=mp.end();it++)
	{
		if (it->first != now + 1)
		{
			if (st.size() && now - *st.rbegin() + 1 < x)
				return 0;
			st.clear();
		}
		now = it->first;
		if (st.size() == it->second)
			continue;
		else
		if (st.size() < it->second)
		{
			int t = st.size();
			for (int i=0;i<it->second-t;i++)
				st.insert(now);
		}
		else
		{
			while(st.size() != it->second)
			{
				int t = *st.begin();
				if (now - t < x)
					return 0;
				st.erase(st.begin());
			}
		}
	}
	now++;
	while(st.size())
	{
		int t = *st.begin();
		if (now - t < x)
			return 0;
		st.erase(st.begin());
	}
	return 1;
}
void Solve()
{
	int n;
	scanf("%d",&n);
	v.assign(n,0);
	mp.clear();
	FOR(i,n)
	{
		scanf("%d",&v[i]);
		mp[v[i]]++;
	}
	if (n == 0)
	{
		printf("0");
		return;
	}
	int L=1,R=1024,m;
	while(R-L > 1)
	{
		m = (L+R)/2;
		if (Check(m,mp))
			L = m;
		else
			R = m;
	}
	printf("%d",L);
}
int main() 
{ 
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int T;
	scanf("%d",&T);
	for (int test=1;test<=T;test++)
	{
		printf("Case #%d: ",test);
		Solve();
		printf("\n");
	}
	return 0; 
}
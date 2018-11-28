#include <algorithm> 
#include <string> 
#include <set> 
#include <map> 
#include <vector> 
#include <queue> 
#include <iostream> 
#include <iterator> 
#include <sstream> 
#include <cmath> 
#include <cstdio> 
#include <cstdlib> 
#include <numeric>
#include <list>
 
using namespace std; 

#define FOR(i,a,b) for (int _n(b), i(a); i < _n; i++) 
#define REP(i,n) FOR(i,0,n) 
#define pb push_back 
#define sz size() 

#define ALL(c) (c).begin(), (c).end() 
#define SORT(c) sort(ALL(c))
#define UNIQUE(v) SORT(v),v.erase(unique(v.begin(),v.end()),v.end())
#define INF 2147483647
#define MAX(a,b) (((a) > (b)) ? (a) : (b))
#define MIN(a,b) (((a) < (b)) ? (a) : (b))
#define MP(a,b)	 make_pair((a), (b))
#define X first
#define Y second
#define CLR(a,v) memset((a),(v),sizeof(a)) 

typedef pair<int,int> II;
typedef vector<int> VI;
typedef vector<VI > VVI;
typedef vector<II > VII;
template<typename T>
void outV(const vector<T>& v){cout<<endl;REP(i,v.sz)cout<<v[i]<<" ";cout<<endl;}
template<typename T>
void outVV(const vector<vector<T> >& v){cout<<endl;REP(i,v.sz){REP(j, v[i].sz)cout<<v[i][j]<<" ";cout<<endl;}cout<<endl;}
void outVII(const VII& v){cout<<endl;REP(i,v.sz)cout<<"("<<v[i].first<<", "<<v[i].second<<") ";cout<<endl;}
int gcd(int a,int b){return a==0 ? b : gcd(b%a, a);}

int mem[30000][2];
int tr[30000];
int ch[30000];

int m, v;

int go(int ver, int val)
{
	if (mem[ver][val] != -1)
		return mem[ver][val];

	int ret = 100000;

	if (ch[ver] == -1)
	{
		if (tr[ver] == val)
			ret = 0;
	}	
	else
	{
		//or
		int ret_or = 100000, ret_and = 100000;
		int now;
		int r1,r2;
		if (val == 0)
		{
			r1 = go(2*ver, 0);
			r2 = go(2*ver + 1, 0);
			if (r1 >= 0 && r2 >= 0)
			{
				now = r1 + r2;
				if (now < ret_or)
					ret_or = now;
			}
		}
		else
		{
			REP(i,2)REP(j,2)
				if (i || j)
				{
					r1 = go(2*ver, i);
					r2 = go(2*ver + 1, j);
					if (r1 >= 0 && r2 >= 0)
					{
						now = r1 + r2;
						if (now < ret_or)
							ret_or = now;
					}
				}
		}

		//and
		if (val == 1)
		{
			r1 = go(2*ver, 1);
			r2 = go(2*ver + 1, 1);
			if (r1 >= 0 && r2 >= 0)
			{
				now = r1 + r2;
				if (now < ret_and)
					ret_and = now;
			}
		}
		else
		{
			REP(i,2)REP(j,2)
				if (i != 1 || j != 1)
				{
					r1 = go(2*ver, i);
					r2 = go(2*ver + 1, j);
					if (r1 >= 0 && r2 >= 0)
					{
						now = r1 + r2;
						if (now < ret_and)
							ret_and = now;
					}
				}
		}

		if (tr[ver] == 0)
		{
			if (ret_or < ret)
				ret = ret_or;
			if (ch[ver])
			{
				if (ret_and + 1 < ret)
					ret = ret_and + 1;
			}
		}
		else
		{
			if (ret_and < ret)
				ret = ret_and;
			if (ch[ver])
			{
				if (ret_or + 1 < ret)
					ret= ret_or + 1;
			}
		}
	}

	if (ret == 100000)
		ret = -2;
	mem[ver][val] = ret;
	return ret;
}

int main()
{
	freopen("input.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	
	int T;
	cin>>T;
	REP(test, T)
	{
		memset(mem, -1, sizeof(mem));
		memset(tr, -1, sizeof(tr));
		memset(ch, -1, sizeof(ch));
		cin>>m>>v;
		REP(i, (m-1)/2)
		{
			int g,c;
			scanf("%d %d", &g, &c);
			tr[i+1] = g;
			ch[i+1] = c;
		}
		for (int i = (m-1)/2 + 1; i <= m; i++)
		{
			int c;
			scanf("%d", &c);
			tr[i] = c;
		}
		int res = go(1, v);
		cout<<"Case #"<<test+1<<": ";
		if (res >= 0)
			cout<<res<<endl;
		else
			cout<<"IMPOSSIBLE"<<endl;
	}

	return 0;
}

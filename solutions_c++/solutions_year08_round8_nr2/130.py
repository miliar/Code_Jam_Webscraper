#include<set>
#include<iostream>
#include<cstdio>
#include<algorithm>
#include<string>
#include<cmath>
#include<vector>
#include<list>
#include<queue>
#include<utility>
using namespace std;
#define ST first
#define ND second
#define PB push_back
#define MP make_pair
typedef long long LL;
typedef pair<int,int> PII;
typedef vector<int> VI;
const int OO=(1<<30);
const bool dbg=0;
#define FOR(x, b, e) for(int x=b; x<=(e); ++x)
#define FORD(x, b, e) for(int x=b; x>=(e); ––x)
#define REP(x, n) for(int x=0; x<(n); ++x)
#define VAR(v,n) typeof(n) v=(n)
#define ALL(c) c.begin(),c.end()
#define SIZE(x) (int)x.size()
#define FOREACH(i,c) for(VAR(i,(c).begin());i!=(c).end();++i)
int n;
VI a,b;
vector<string> c;
void readCase()
{
	a.clear();b.clear();c.clear();
	string s;
	int A,B;
	cin>>n;
	for(int i=0;i<n;i++)
	{	
		cin>>s>>A>>B;
		c.PB(s);
		a.PB(A);
		b.PB(B);
	}
}

bool check(VI pro)
{
	if(dbg)
	{
		printf("Check:");
		for(int i=0;i<pro.size();i++)
			printf("%d ",pro[i]);
		printf("\n");
	}
	set<string> str;
	for(int i=0;i<pro.size();i++)
	{
		str.insert(c[pro[i]]);
	}
	if(str.size()>3)return 0;
	vector<PII> v;
	for(int i=0;i<pro.size();i++)
		v.PB(MP(a[pro[i]],b[pro[i]]));
	sort(ALL(v));
	if(dbg)
	{
		for(int i=0;i<v.size();i++)
			printf("[%d, %d]",v[i].ST,v[i].ND);
		printf("\n");
	}
	if(v[0].ST!=1)return 0;
	int ran=v[0].ND;
	for(int i=0;i<v.size();i++)
	{
		if(ran>=10000)return 1;
		if(v[i].ST>1+ran)return 0;
		ran=max(ran,v[i].ND);
	}
	if(ran>=10000)return 1;
	return 0;
}

void computeCase(int cas)
{
	VI v;
	v.resize(n);
	for(int i=1;i<=n;i++)
	{
		v.resize(0);
		for(int j=0;j<n-i;j++)
			v.PB(0);
		for(int j=n-i;j<n;j++)
			v.PB(1);
		do {
			VI arg;
			for(int j=0;j<n;j++)
				if(v[j]==1)arg.PB(j);
			if(check(arg))
			{
				printf("Case #%d: %d\n",cas,i);
				return;
			}
		}
		while(next_permutation(ALL(v)));
	}
	printf("Case #%d: IMPOSSIBLE\n",cas);

		
}

int main()
{
	int t;
	scanf("%d",&t);
	for(int i=0;i<t;i++)
	{
		readCase();
		computeCase(i+1);
	}
	return 0;
}


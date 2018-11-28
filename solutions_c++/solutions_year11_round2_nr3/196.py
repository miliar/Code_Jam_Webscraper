#include<map>
#include<set>
#include<list>
#include<cmath>
#include<ctime>
#include<deque>
#include<queue>
#include<stack>
#include<bitset>
#include<cctype>
#include<cstdio>
#include<string>
#include<vector>
#include<cstdlib>
#include<cstring>
#include<iomanip>
#include<numeric>
#include<utility>
#include<sstream>
#include<iostream>
#include<algorithm>
#include<functional>

using namespace std;

// Begin Template By yaymao

#ifndef ONLINE_JUDGE
	#define READ freopen("C-small.in","r",stdin)
	#define WRITE freopen("C-small.out","w",stdout)
#else
	#define READ
	#define WRITE
#endif

#ifdef _MSC_VER
	#define LL __int64
	#define ULL unsigned __int64
#else
	#define LL long long
	#define ULL unsigned long long
#endif

#define EPS 1E-9
#define D_INF 1E99
#define I_INF 0x7FFFFFFF
#define L_INF 0x7FFFFFFFFFFFFFFFLL

#define LENGTH(x) ((int)x.length())

#define SIZE(x) ((int)x.size())

#define PB(x) push_back(x)

#define MII map<int,int>
#define MSI map<string,int>
#define MIS map<int,string>

#define PII pair<int,int>
#define PSI pair<string,int>
#define PIS pair<int,string>

#define X first
#define Y second

#define MP(x,y) make_pair(x,y)

#define TWO(x)			(1<<(x))
#define TWOL(x)			(1LL<<(x))
#define LOWER_BIT(x)	((x)&(-(x)))
#define CONTAIN(s,x)	(((s)&TWO(x))!=0)
#define CONTAINL(s,x)	(((s)&TWOL(x))!=0)

template<class T>inline void checkMax(T &a,const T &b){if(a<b) a=b;}
template<class T>inline void checkMin(T &a,const T &b){if(b<a) a=b;}
template<class T>inline string toString(const T &n){ostringstream out;out<<n;out.flush();return out.str();}
template<class T>inline T toValue(const string &s){T x;istringstream in(s);in>>x;return x;}

#define setv(a,v) memset(a,v,sizeof(a))

#define range(i,l,r) for(int i=(l);i<(int)(r);++i)
#define rangeD(i,l,r) for(int i=(l);i>(int)(r);--i)
#define rep(i,n) for(int i=0;i<(int)(n);++i)
#define repD(i,n) for(int i=(int)(n)-1;i>=0;--i)

#define all(c) (c).begin(),(c).end()
#define foreach(it,c) for(__typeof((c).begin()) it=(c).begin();it!=(c).end();++it)

// End Template By yaymao

const int MAX_N=8;

int n;
bool g[MAX_N+1][MAX_N+1];

bool isFind;

int idN;
set<int> S[MAX_N+1];

int minC;
int color[MAX_N+1];

bool has[MAX_N+1];
void DFS(const int &i)
{
	if(i==n)
	{
		isFind=true;
		rep(i,idN)
		{
			int cnt=0;
			setv(has,false);
			foreach(it,S[i])
				if(!has[color[*it]])
				{
					has[color[*it]]=true;
					++cnt;
				}
			if(cnt!=minC)
			{
				isFind=false;
				break;
			}
		}
		return;
	}

	for(int c=0;c<minC;++c)
	{
		color[i]=c;
		DFS(i+1);
		if(isFind)
			return;
	}
	color[i]=-1;
}

int start;

bool visit[MAX_N+1];

void findC(const int &u)
{
	if(isFind)
		return;
	if(visit[u])
	{
		if(u!=start)
			return;

		int ncnt=0,mcnt=0;
		rep(i,n)
			if(visit[i])
			{
				++ncnt;
				rep(j,n)
					if(visit[j] && g[i][j])
						++mcnt;
			}
		
		if(2*ncnt!=mcnt)
			return;

		S[idN].clear();
		rep(i,n)
			if(visit[i])
				S[idN].insert(i);

		rep(i,idN)
			if(S[i]==S[idN])
				return;

		isFind=true;
		return;
	}

	visit[u]=true;
	rep(v,n)
		if(g[u][v])
		{
			findC(v);
			if(isFind)
				return;
		}
	visit[u]=false;
}

int m;
int u[MAX_N+1],v[MAX_N+1];

void run(const int &caseID)
{
	// read data
	cin>>n>>m;
	rep(i,m)
		cin>>u[i];
	rep(i,m)
		cin>>v[i];

	// make graph
	setv(g,false);
	rep(i,n)
	{
		g[i][(i+1)%n]=true;
		g[(i+1)%n][i]=true;
	}
	rep(i,m)
	{
		g[u[i]-1][v[i]-1]=true;
		g[v[i]-1][u[i]-1]=true;
	}

	// find circle
	idN=0;
	rep(i,n)
	{
		setv(visit,false);

		start=i;
		isFind=false;
		findC(i);

		if(isFind)
			++idN;
	}

	// find min circle
	minC=n;
	rep(i,idN)
		checkMin(minC,SIZE(S[i]));

	// find color
	setv(color,-1);
	isFind=false;
	DFS(0);

	printf("Case #%d: %d\n",caseID,minC);
	rep(i,n)
	{
		cout<<color[i]+1;
		if(i+1==n)
			cout<<endl;
		else
			cout<<" ";
	}
}

int main(int argc, char *argv[])
{
	READ;
	WRITE;

	int caseT;
	scanf("%d",&caseT);
	for(int caseID=1;caseID<=caseT;++caseID)
		run(caseID);

	return (EXIT_SUCCESS);
}

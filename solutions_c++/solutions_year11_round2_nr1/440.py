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
	#define READ freopen("A-large.in","r",stdin)
	#define WRITE freopen("A-large.out","w",stdout)
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

const int MAX_N=100;

int n;
char table[MAX_N+1][MAX_N+1];

double WP[MAX_N+1];
double OWP[MAX_N+1];
double OOWP[MAX_N+1];
double RPI[MAX_N+1];

double calcWP(char table[][MAX_N+1],const int &id)
{
	int w=0,t=n;
	rep(i,n)
		if(table[id][i]=='.')
			--t;
		else if(table[id][i]=='1')
			++w;
	return (double)w/(double)t;
}

double calcOWP(char table[][MAX_N+1],const int &id)
{
	char newTable[MAX_N+1][MAX_N+1];
	rep(i,n)
		rep(j,n)
			if(i==id || j==id)
				newTable[i][j]='.';
			else
				newTable[i][j]=table[i][j];
	int m=0;
	double sum=0.0;
	rep(i,n)
		if(table[id][i]!='.')
		{
			sum+=calcWP(newTable,i);
			++m;
		}

	return sum/(double)m;
}

double calcOOWP(char table[][MAX_N+1],const int &id)
{
	int m=0;
	double sum=0.0;
	rep(i,n)
		if(table[id][i]!='.')
		{
			sum+=calcOWP(table,i);
			++m;
		}

	return sum/(double)m;
}

void run(const int &caseID)
{
	cin>>n;
	rep(i,n)
		rep(j,n)
			scanf(" %c",&table[i][j]);

	rep(i,n)
		WP[i]=calcWP(table,i);

	rep(i,n)
		OWP[i]=calcOWP(table,i);

	rep(i,n)
		OOWP[i]=calcOOWP(table,i);

	rep(i,n)
		RPI[i]=0.25*WP[i]+0.50*OWP[i]+0.25*OOWP[i];

	printf("Case #%d:\n",caseID);
	rep(i,n)
		printf("%.9lf\n",RPI[i]);
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

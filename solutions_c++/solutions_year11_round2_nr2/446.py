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
	#define READ freopen("B-small.in","r",stdin)
	#define WRITE freopen("B-small.out","w",stdout)
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

inline double sign(const double &x)
{
	if(fabs(x)<EPS)
		return 0;
	return x<0?-1:1;
}

inline double dc(const double &a,const double &b)
{
	return sign(a-b);
}

const int MAX_N=1000000;

int n;
double x[MAX_N+1];
pair<double,double> seg[MAX_N+1];

double D;

bool ok(const double &times)
{
	rep(i,n)
		seg[i]=MP(x[i]-times,x[i]+times);
	double preX=seg[0].X;
	range(i,1,n)
	{
		double nowX=max(preX+D,seg[i].X);
		if(nowX>seg[i].Y)
			return false;
		preX=nowX;
	}
	return true;
}

void run(const int &caseID)
{
	int C;
	cin>>C>>D;

	n=0;
	rep(i,C)
	{
		int P,V;
		cin>>P>>V;
		rep(j,V)
			x[n++]=P;
	}

	sort(x,x+n);

	double l=0,r=1E10;
	while(l+EPS<r)
	{
		double mid=0.5*(l+r);
		if(!ok(mid))
			l=mid;
		else
			r=mid;
	}

	double reslut=0.5*(l+r);

	printf("Case #%d: %.9lf\n",caseID,reslut);
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

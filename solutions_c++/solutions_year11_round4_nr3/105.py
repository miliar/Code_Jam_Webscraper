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
	#define READ freopen("C-large.in","r",stdin)
	#define WRITE freopen("C-large.out","w",stdout)
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

const static int MAX_V=2000000;

bool isP[MAX_V+1];
vector<int> prime;

void init() {

	for(int i=0;i<=MAX_V;++i)
		isP[i]=true;
	isP[0]=isP[1]=false;
	for(int i=2;i*i<=MAX_V;++i)
		if(isP[i])
			for(int j=i*i;j<=MAX_V;j+=i)
				isP[j]=false;
	prime.clear();
	for(int i=2;i<=MAX_V;++i)
		if(isP[i])
			prime.PB(i);
}

int calc(LL n,int p) {
	int r=0;
	while(n>=p) {
		++r;
		n/=p;
	}
	return r;
}

LL solve(LL n) {
	if(n==1)
		return 0;

	LL res=1;
	foreach(it,prime) {
		if(*it>n)
			break;
		res+=calc(n,*it)-1;
	}

	return res;
}

void run(const int &caseID)
{
	LL n;
	cin>>n;

	printf("Case #%d: %lld\n",caseID,solve(n));
}

int main(int argc, char *argv[])
{
	READ;
	WRITE;

	init();

	int caseT;
	scanf("%d",&caseT);
	for(int caseID=1;caseID<=caseT;++caseID)
		run(caseID);

	return (EXIT_SUCCESS);
}

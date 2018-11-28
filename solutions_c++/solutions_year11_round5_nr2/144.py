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
	#define READ freopen("B-large.in","r",stdin)
	#define WRITE freopen("B-large.out","w",stdout)
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

#define range(i,l,r) for(int i=(l);i<=(int)(r);++i)
#define rangeD(i,l,r) for(int i=(l);i>=(int)(r);--i)
#define rep(i,n) for(int i=0;i<(int)(n);++i)
#define repD(i,n) for(int i=(int)(n)-1;i>=0;--i)

#define all(c) (c).begin(),(c).end()
#define foreach(it,c) for(__typeof((c).begin()) it=(c).begin();it!=(c).end();++it)

// End Template By yaymao

const int N=1000;
const int V=10000;

int n;
int v[N+1];

int cnt[V+1];

bool isConsecutive(int l,int r) {
	for(int i=l+1;i<=r;++i)
		if(v[i-1]+1!=v[i])
			return false;
	return true;
}

struct Node
{
	int l;
	int end;

	Node(){}
	Node(int l,int end)
		:l(l),end(end){}

	bool operator < (const Node &p) const {
		return l<p.l || (l==p.l && end<p.end);
	}
};

vector<Node> ls;

bool ok(const int &minLen) {
	ls.clear();

	for(int i=0;i<n;++i) {
		bool updata=false;
		for(int j=0;j<SIZE(ls);++j)
			if(ls[j].end+1==v[i]) {
				++ls[j].l;
				++ls[j].end;
				updata=true;
				break;
			}
		if(updata==false)
			ls.PB(Node(1,v[i]));
		sort(all(ls));
	}
	return ls[0].l>=minLen;
}

int stupid() {
	int res=0;

	for(int l=n;l>=1;--l)
		if(ok(l)) {
			res=l;
			break;
		}

	return res;
}

int binarySeach() {
	int l=0,r=n;
	while(l<=r) {
		int mid=(l+r)>>1;
		if(ok(mid))
			l=mid+1;
		else
			r=mid-1;
	}
	return r;
}

void run(const int &caseID)
{
	setv(cnt,0x00);

	cin>>n;
	rep(i,n) {
		cin>>v[i];
		++cnt[v[i]];
	}

	sort(v,v+n);

	int res=binarySeach();

	printf("Case #%d: %d\n",caseID,res);
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

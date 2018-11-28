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

#define range(i,l,r) for(int i=(l);i<(int)(r);++i)
#define rangeD(i,l,r) for(int i=(l);i>(int)(r);--i)
#define rep(i,n) for(int i=0;i<(int)(n);++i)
#define repD(i,n) for(int i=(int)(n)-1;i>=0;--i)

#define all(c) (c).begin(),(c).end()
#define foreach(it,c) for(__typeof((c).begin()) it=(c).begin();it!=(c).end();++it)

// End Template By yaymao

struct Point
{
	LL x,y;

	Point(){}
	Point(const LL &x,const LL &y)
		:x(x),y(y){}

	Point operator + (const Point &p) const {
		return Point(x+p.x,y+p.y);
	}

	Point operator - (const Point &p) const {
		return Point(x-p.x,y-p.y);
	}

	Point operator * (const int &r) const {
		return Point(x*r,y*r);
	}
};

const int MAX_R=512;
const int MAX_C=512;

int R,C;
LL w[MAX_R+1][MAX_C+1];
LL wSum[MAX_R+1][MAX_C+1];

Point pw[MAX_R+1][MAX_C+1];
Point pwSum[MAX_R+1][MAX_C+1];

LL D;

bool ok(const int &l) {
	Point nowPW;
	LL nowW;
	for(int sx=1;sx+l-1<=R;++sx)
		for(int sy=1;sy+l-1<=C;++sy) {
			int tx=sx+l-1;
			int ty=sy+l-1;

			LL cnt=(LL)l*l-4;

			nowW=wSum[tx][ty]-wSum[tx][sy-1]-wSum[sx-1][ty]+wSum[sx-1][sy-1];
			nowW-=w[sx][sy];
			nowW-=w[sx][ty];
			nowW-=w[tx][sy];
			nowW-=w[tx][ty];

			nowPW=pwSum[tx][ty]-pwSum[tx][sy-1]-pwSum[sx-1][ty]+pwSum[sx-1][sy-1];
			nowPW=nowPW-pw[sx][sy];
			nowPW=nowPW-pw[sx][ty];
			nowPW=nowPW-pw[tx][sy];
			nowPW=nowPW-pw[tx][ty];

			if(2*nowPW.x%nowW==0 && 2*nowPW.y%nowW==0 && sx+tx==2*nowPW.x/nowW && sy+ty==2*nowPW.y/nowW)
				return true;
			else
				continue;
		}
	return false;
}

void run(const int &caseID)
{
	cin>>R>>C>>D;

	setv(wSum,0);
	setv(pwSum,0);

	for(int i=1;i<=R;++i)
		for(int j=1;j<=C;++j) {
			char c;
			scanf(" %c",&c);

			w[i][j]=D+c-'0';
			wSum[i][j]=wSum[i-1][j]+wSum[i][j-1]-wSum[i-1][j-1]+w[i][j];

			pw[i][j]=Point(i,j)*w[i][j];
			pwSum[i][j]=pwSum[i-1][j]+pwSum[i][j-1]-pwSum[i-1][j-1]+pw[i][j];
		}

	int res=-1;
	for(int K=min(R,C);K>=3;--K)
		if(ok(K)) {
			res=K;
			break;
		}
	
	printf("Case #%d: ",caseID);
	if(res==-1)
		printf("IMPOSSIBLE\n");
	else
		printf("%d\n",res);

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

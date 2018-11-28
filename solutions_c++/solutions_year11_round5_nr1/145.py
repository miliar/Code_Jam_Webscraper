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

struct Point {
	double x,y;

	Point(){}
	Point(const double &x,const double &y)
		:x(x),y(y){}

	void read() {
		scanf("%lf %lf",&x,&y);
	}

	Point operator + (const Point &p) const {
		return Point(x+p.x,y+p.y);
	}

	Point operator - (const Point &p) const {
		return Point(x-p.x,y-p.y);
	}

	Point operator * (const double &r) const {
		return Point(x*r,y*r);
	}
};

const int N=100;

int upperN;
Point upper[N+1];

int lowerN;
Point lower[N+1];

const double LIMIT=10000;

double calcArea(const double &rx) {
	double area=(LIMIT+LIMIT)*rx;

	for(int i=1;i<upperN;++i) {
		double nowX=upper[i].x,nowY=upper[i].y;
		if(rx+EPS<upper[i].x) {
			nowX=rx;
			double k=(upper[i].y-upper[i-1].y)/(upper[i].x-upper[i-1].x);
			double b=upper[i].y-upper[i].x*k;
			nowY=k*nowX+b;
		}

		area-=((LIMIT-upper[i-1].y)+(LIMIT-nowY))*(nowX-upper[i-1].x)/2.0;

		if(rx+EPS<upper[i].x)
			break;
	}

	for(int i=1;i<lowerN;++i) {
		double nowX=lower[i].x,nowY=lower[i].y;
		if(rx+EPS<lower[i].x) {
			nowX=rx;
			double k=(lower[i].y-lower[i-1].y)/(lower[i].x-lower[i-1].x);
			double b=lower[i].y-lower[i].x*k;
			nowY=k*nowX+b;
		}
		area-=((LIMIT+lower[i-1].y)+(LIMIT+nowY))*(nowX-lower[i-1].x)/2.0;

		if(rx+EPS<lower[i].x)
			break;
	}

	return area;
}

double binarySeach(const double &lx,const double &rx,const double &target) {
	double low=lx,high=rx;
	for(int t=0;t<500 && low+EPS<high;++t) {
		double mid=(low+high)/2.0;
		double area=calcArea(mid)-calcArea(lx);
		if(area+EPS<target)
			low=mid;
		else
			high=mid;
	}
	return (low+high)/2.0;
}

int W;
int G;
 

void run(const int &caseID)
{
	cin>>W>>lowerN>>upperN>>G;

	rep(i,lowerN)
		lower[i].read();
	rep(i,upperN)
		upper[i].read();

	printf("Case #%d:\n",caseID);

	double totalArea=calcArea(W);
	double averArea=totalArea/G;

	double preX=0.0;

	rep(i,G-1) {
		double nowX=binarySeach(preX,W,averArea);
		printf("%.9lf\n",nowX);
		preX=nowX;
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

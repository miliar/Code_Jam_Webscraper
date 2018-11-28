#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <cstring>
#include <string>
#include <map>
#include <queue>
#include <sstream>
#include <numeric>
#include <functional>
#include <set>
#include <cmath>
#include <stack>
#include <fstream>
#include <cassert>
#ifdef HOME_PC
#include <ctime>
#endif
using namespace std;

#pragma comment(linker,"/stack:16000000")
#pragma warning (disable : 4996)

#define ALL(v) v.begin(),v.end()
#define SZ(v) ((int)(v.size()))
#define mset(A,x) memset((A),(x),sizeof(A))
#define FOR(i,start,N) for(int i=(start);i<(N);++i)
#define FORSZ(i,start,v) FOR(i,start,SZ(v))
#define REPSZ(i,v) FORSZ(i,0,v)
#define FORE(i,start,N) FOR(i,start,N+1)
#define make_unique(v) v.resize(unique(ALL(v))-v.begin())
#define debug(x) cout<<#x<<" = "<<x<<endl;
#define adebug(A,N) FOR(i,0,N) cout<<#A<<"["<<i<<"] = "<<A[i]<<endl;
#define adebug2d(a,n,m) FOR(i,0,n) { FOR(j,0,m) { cout<<a[i][j]<<" ";} cout<<endl;}
#define vdebug(v) REPSZ(i,v) cout<<#v<<"["<<i<<"] = "<<v[i]<<endl;
#define selfx(x,f,a) x = f(x,a)
#define sqr(x) ((x)*(x))


typedef pair<int,int> pii;
typedef long long i64;
typedef vector<int> VI; typedef vector< vector<int> > VVI;
typedef vector<string> VS;

const int inf = 1<<25;
const double eps = 1e-9;

typedef pair<double, double> pdd;
typedef vector<pdd> vpdd;

//double dist(const pdd& a, const pdd& b)
//{
//	return sqrt(sqr(a.first - b.first) + sqr(a.second + b.second)); 
//}

//bool isOk(const vpdd& p,const VI& r, int W,int L)
//{
//	REPSZ(i,p)
//	{
//		if(p[i].first < -eps || p[i].first >= W+eps ||
//			p[i].second < -eps || p[i].second >= L + eps)
//				return false;
//		FORSZ(j,i + 1,p)
//		{
//			double d = dist(p[i], p[j]);
//			if(d <= r[i] + r[j] - eps)
//				return false;
//		}
//	}
//	return true;
//}
i64 dist2(const pii& a, const pii& b)
{
	return sqr((i64)a.first - b.first) + sqr((i64)a.second - b.second); 
}


bool isOk(const vector<pii>& p,const VI& r, int W,int L)
{
	REPSZ(i,p)
	{
		if(p[i].first < 0 || p[i].first > W ||
			p[i].second < 0 || p[i].second > L)
			return false;
		FORSZ(j,i + 1,p)
		{
			i64 d2 = dist2(p[i], p[j]);
			if(d2 < sqr((i64)r[i] + r[j]))
				return false;
		}
	}
	return true;
}
struct Brick
{
public:
	Brick(int x0,int x1,int yMin):x0(x0),x1(x1),yMin(yMin){}
	bool CanPlace(const int r, int W,int L) const
	{
		if(!(x0 == 0 && x1 == W))
		{if(x0 == 0 || x1 == W)
		{
			if(GetLength() < r)
				return false;
		}
		else
		{
			if(GetLength() < 2*r)
				return false;
		}}
		if(yMin == 0)
			return true;
		return  yMin + r <= L;
	}
	int GetLength() const { return x1 - x0;}
	int Left() const { return x0; }
	int Right() const { return x1; }
	int MinY() const { return yMin; }

	bool operator<(const Brick& other) const 
	{
		return Triplet() < other.Triplet();
	}
	pair<int , pii > Triplet() const 
	{
		return make_pair(yMin, pii(x0,x1));
	}
	pii GetCoords(const int r)
	{
		return pii(x0+ ((x0 != 0)*r), yMin + (yMin!=0)*r);
	}
private:
	int x0, x1, yMin;
};


bool GetGoodBrick(Brick& good, const set<Brick>& bricksSet, const int r, const int W, const int L)
{
	bool foundAns = false;
	vector<Brick> bricks(ALL(bricksSet));
	REPSZ(i,bricks)
		if(bricks[i].CanPlace(r,W,L) && (!foundAns || good.GetLength() > bricks[i].GetLength()))
		{
			good = bricks[i];
			foundAns = true;
		}
	return foundAns;
}

vector<Brick> split(const Brick& brick, const int r)
{
	// attach to the left
	vector<Brick> result;
	result.push_back(Brick(brick.Left(),brick.Left() + (brick.Left() == 0? r : 2*r), brick.MinY() + (brick.MinY() == 0? r : 2*r)));
	result.push_back(Brick(result[0].Right(), brick.Right(), brick.MinY()));
	return result;
}

int main()
{
#ifdef HOME_PC
	freopen ("B-large(2).in","r",stdin);
	//freopen ("in.txt","r",stdin);
	freopen ("output.txt","w",stdout);
#else
	//freopen ("input.txt","r",stdin);
	//freopen ("output.txt","w",stdout);
#endif
	int numTests = 0;
	cin>>numTests;
	FORE(testCase,1,numTests)
	{
		int N,W,L;
		cin>>N>>W>>L;
		vector<pii> r(N);
		FOR(i,0,N)
			cin>>r[i].first, r[i].second = i;
		sort(ALL(r), greater<pii>());

		set<Brick> bricks;
		bricks.insert(Brick(0,W,0));
		vector<pii> ans(N);

		REPSZ(i,r)
		{
			Brick good(0,0,0);
			int ri = r[i].first;
			if(!GetGoodBrick(good, bricks, ri, W, L))
			{
				GetGoodBrick(good,bricks,ri,W,L);
				throw 0;
			}
			
			vector<Brick> result = split(good, ri);
			pii coords = good.GetCoords(ri);
			bricks.erase(good);
			REPSZ(j,result)
			{
				if(result[j].CanPlace(r.back().first, W, L))
					bricks.insert(result[j]);
			}
			ans[r[i].second] = coords;
		}

		printf("Case #%d:",testCase);
		FOR(i,0,N)
			printf(" %d %d",ans[i].first, ans[i].second);
		puts("");
		VI rs(N);
		REPSZ(i,r)
			rs[r[i].second] = r[i].first;
		if(!isOk(ans,rs,W,L))
		{
			cerr<<"Fail #"<<testCase<<endl;
			continue;
		}
	}
	
#ifdef HOME_PC
	cerr<<endl<<"Execution time = "<<clock()<<" ms"<<endl;
#endif
	return 0;
}

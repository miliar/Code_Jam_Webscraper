
#include <cstdio>
#include <cmath>
#include <boost/thread/thread.hpp>
#include <iostream>
#include <vector>
#include <iterator>
#include <algorithm>
using namespace std;
using namespace boost;
//By chyx111
typedef long long ll;
#define SZ(a) ((int)(a).size())
#define Rep(i,n) for(int n_ = (n), i = 0; i< n_; ++i)
#define ALL(x) (x).begin(), (x).end()

struct Point{
	int pos, cnt;
	bool operator<(const Point& other)const{
		return pos < other.pos;
	}
	void scan(){
		scanf("%d%d", &pos, &cnt);
	}
};
struct Solver{
	int ncase;

	int n, D;
	ll ans;
	vector<Point> vendors;
	vector<int> points;

	bool solve(ll len){
		ll curr = points[0] - len;
		for(int i = 1; i < SZ(points); ++i){
			if( points[i] + len < curr + D * 2 ){
				return false;
			}else{
				curr = max( curr + D * 2, points[i] - len );
			}
		}
		return true;
	}
	void run(){
		Rep(i, SZ(vendors)){
			Rep(c, vendors[i].cnt){
				points.push_back( vendors[i].pos * 2 );
			}
		}
		ll lo = 0, hi = 0x3f3f3f3f3f3f3f3fLL, mid;
		while( lo != hi ){
			mid = (lo+hi)/2;
			if( solve(mid) ){
				hi = mid;
			}else{
				lo = mid + 1;
			}
		}
		ans = lo;
	}
	void parse_input(){
		scanf("%d%d", &n, &D);
		vendors.clear();
		Rep(i,n){
			vendors.push_back( Point() );
			vendors.back().scan();
		}
	}
	void output_result(){
		printf("Case #%d: ", ncase+1);
		printf("%.20f\n", ans / 2. );
	}
};

vector<Solver> solvers;
void thread_solver(int icase){
	solvers[icase].run();
}

int main()
{
//	freopen("B.txt", "r", stdin);
//	freopen("B-small-attempt0.in", "r", stdin);
//	freopen("B-small-attempt0.out", "w", stdout);
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	int n_cases;
	scanf("%d", &n_cases);

	vector<thread> threads(n_cases);
	solvers.resize(n_cases);
	Rep(icase,n_cases){
		solvers[icase].ncase = icase;
		solvers[icase].parse_input();
		threads[icase] = thread(boost::bind(thread_solver, icase));
	}
	Rep(i,n_cases){
		threads[i].join();
		solvers[i].output_result();
	}
}

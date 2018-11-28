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
#define Rep(i,n) for(int n_ = (n), i = 0; i< n_; ++i)
#define ALL(x) (x).begin(), (x).end()
#define SZ(x) (int)((x).size())
template<class T> void inline checkMin(T& a, T b){if(a > b) a = b;};

int const N = 1024;
struct WalkWay{
	int x, y, w;
	WalkWay(int x, int y, int w):x(x), y(y), w(w){}
	WalkWay(){}
	void scan(){
		scanf("%d%d%d", &x, &y, &w);
	}
	bool operator<(const WalkWay &other)const{
		return x < other.x;
	}
};
struct Solver{
	int ncase;

	int n, speed, runspeed, total;
	double time_run;
	double ans;
	vector<WalkWay> way;

	Solver(int ncase = 0):ncase(ncase){}
	void run(){
		sort(ALL(way));
		int curr = 0;
		vector<WalkWay> normal;
		Rep(i,n){
			normal.push_back(WalkWay(curr, way[i].x, 0));
			normal.push_back(WalkWay(way[i].x, way[i].y, way[i].w));
			curr = way[i].y;
		}
		normal.push_back(WalkWay(curr, total, 0));

		sort(ALL(normal), [](const WalkWay& a, const WalkWay& b){return a.w < b.w;});
		ans = 0;
		Rep(i, SZ(normal)){
//			cout<<normal[i].y-normal[i].x<<" "<<time_run<<endl;
			double len = normal[i].y - normal[i].x;
			checkMin(len, time_run * (normal[i].w + runspeed) );
			time_run -= len / (normal[i].w + runspeed);
			ans += (len) / static_cast<double>(normal[i].w + runspeed);
			ans += (normal[i].y - normal[i].x - len) / static_cast<double>(normal[i].w + speed);
		}
	}
	void parse_input(){
		scanf("%d%d%d%lf%d", &total, &speed, &runspeed, &time_run, &n);
		way = vector<WalkWay>(n);
		Rep(i,n)way[i].scan();
	}
	void output_result(){
		printf("Case #%d: ", ncase+1);
		printf("%.10f\n", ans);
	}
};

vector<Solver> solvers;
void thread_solver(int icase){
	solvers[icase].run();
}

int main()
{
//	freopen("A.txt", "r", stdin);
//	freopen("A-small-attempt0.in", "r", stdin);
//	freopen("A-small-attempt0.out", "w", stdout);
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
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


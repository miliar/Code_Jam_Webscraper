
#include <complex>
#include <cstdio>
#include <cmath>
#include <ctime>
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
typedef complex<ll> Pt;

int const N = 512;
struct Solver{
	int ncase;

	int n, m, D, ans;
	string maze[N];
	vector<Pt> pt[N];
	vector<Pt> sum[N];
	vector<ll> w[N];
	vector<ll> sumw[N];

	void run(){
		ans = -1;
		Rep(i,n)Rep(j,m){
			pt[i][j] = Pt(D + maze[i][j] - '0', 0) * Pt(i,j);
			w[i][j] = D + maze[i][j] - '0';
		}
		Rep(i,n)Rep(j,m){
			sum[i+1][j+1] = sum[i][j+1] + sum[i+1][j] - sum[i][j] + pt[i][j];
			sumw[i+1][j+1] = sumw[i][j+1] + sumw[i+1][j] - sumw[i][j] + w[i][j];
		}
		for(int E = min(n,m); E >= 3; --E){
			Rep(i,n-E+1)Rep(j,m-E+1){
				Pt asum = sum[i+E][j+E] - sum[i][j+E] - sum[i+E][j] + sum[i][j];
				asum -= pt[i+E-1][j+E-1] + pt[i][j+E-1] + pt[i+E-1][j] + pt[i][j];

				ll bsum = sumw[i+E][j+E] - sumw[i][j+E] - sumw[i+E][j] + sumw[i][j];
				bsum -= w[i+E-1][j+E-1] + w[i][j+E-1] + w[i+E-1][j] + w[i][j];
				Pt center(i*2+E-1, j*2+E-1);
//				if( E == 5 ){ cout<<center*Pt(bsum,0)<<" "<<asum*Pt(2,0)<<endl; }
				if( center * Pt(bsum, 0) == asum * Pt(2,0) ){
					ans = E;
					return;
				}
			}
		}
	}
	void parse_input(){
		cin>>n>>m>>D;
		Rep(i,n)cin>>maze[i];
		Rep(i,n)pt[i] = vector<Pt>(m);
		Rep(i,n+1)sum[i] = vector<Pt>(m+1, Pt(0,0));
		Rep(i,n)w[i] = vector<ll>(m);
		Rep(i,n+1)sumw[i] = vector<ll>(m+1, 0LL);
//		run();
	}
	void output_result(){
		printf("Case #%d: ", ncase+1);
		if( ans == -1 ){
			puts("IMPOSSIBLE");
		}else{
			printf("%d\n", ans);
		}
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
	cin>>n_cases;
	time_t start_time;
	time(&start_time);

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

	time_t curr_time;
	time(&curr_time);
//	double duration = difftime(curr_time, start_time);
//	cerr<<"Duration: "<<duration<<endl;
}

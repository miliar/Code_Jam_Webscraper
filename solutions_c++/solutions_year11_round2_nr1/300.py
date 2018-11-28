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

int const N = 128;
struct Solver{
	int ncase;

	int n;
	double RPI[N], WP[N], OWP[N], OOWP[N], WP2[N];
	char maze[N][N];
	Solver(int ncase = 0):ncase(ncase){}
	void run(){
		memset(WP, 0, (sizeof WP));
		memset(OWP, 0, (sizeof OWP));
		memset(OOWP, 0, (sizeof OOWP));
		Rep(i,n){
			int cnt_oponent = 0;
			Rep(j,n)if( maze[i][j] == '1' )WP[i]++, cnt_oponent++;
			Rep(j,n)if( maze[i][j] == '0' )cnt_oponent++;
			WP[i] /= cnt_oponent;
		}

		Rep(i,n){
			int cnt_oponent = 0;
			memset(WP2, 0, (sizeof WP2));
			Rep(a,n){
				int cnt_oponent = 0;
				Rep(b,n)if( b != i && maze[a][b] == '1' )WP2[a]++, cnt_oponent++;
				Rep(b,n)if( b != i && maze[a][b] == '0' )cnt_oponent++;
				WP2[a] /= cnt_oponent;
			}
			Rep(j,n)if( maze[i][j] == '0' )cnt_oponent++, OWP[i] += WP2[j]; 
			Rep(j,n)if( maze[i][j] == '1' )cnt_oponent++, OWP[i] += WP2[j]; 
			OWP[i] /= cnt_oponent;
		}

		Rep(i,n){
			double sum = 0;
			int cnt_oponent = 0;
			Rep(j,n)if( maze[i][j] == '0' )cnt_oponent++, OOWP[i] += OWP[j]; 
			Rep(j,n)if( maze[i][j] == '1' )cnt_oponent++, OOWP[i] += OWP[j]; 
			OOWP[i] /= cnt_oponent;
		}

		Rep(i,n){
			RPI[i] = 0.25 * WP[i] + 0.50 * OWP[i] + 0.25 * OOWP[i];
		}
	}
	void parse_input(){
		scanf("%d", &n);
		Rep(i,n){
			scanf("%s", maze[i]);
		}
	}
	void output_result(){
		printf("Case #%d: \n", ncase+1);
		Rep(i,n)printf("%.20f\n", RPI[i]);
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


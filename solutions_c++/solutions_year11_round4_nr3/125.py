#include <cstdio>
#include <bitset>
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
#define two(x) (1<<(x))
typedef pair<int,int> pii;

int const N = 1100000;
bitset<N> isprime;
struct Solver{
	int ncase;

	ll n, ans;
	void run(){
		if( n == 1 ){
			ans = 0;
			return;
		}
		ans = 1;
		for(ll i = 2; i * i <= n; ++i)if( isprime[i] ){
			int t = 0;
			for(ll k = n / i; k; k /= i){
				t++;
			}
			ans += t - 1;
//			cout<<i<<" "<<t<<endl;
		}
	}
	void parse_input(){
		cin>>n;
		run();
	}
	void output_result(){
		printf("Case #%d: ", ncase+1);
		printf("%d\n", ans);
	}
};

vector<Solver> solvers;
void thread_solver(int icase){
//	solvers[icase].run();
}

int main()
{
	isprime.set();
	isprime[0] = isprime[1] = false;
	for(int i = 4; i < isprime.size(); i += 2 )isprime[i] = false;
	for(int i = 3; i < isprime.size(); i += 2 )if( isprime[i] ){
		for(int k = i * 3; k < isprime.size(); k += i + i) isprime[k] = false;
	}

//	freopen("C.txt", "r", stdin);
//	freopen("C-small-attempt0.in", "r", stdin);
//	freopen("C-small-attempt0.out", "w", stdout);
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);
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

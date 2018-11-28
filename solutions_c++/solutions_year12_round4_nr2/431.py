#include <bitset>
#include <cassert>
#include <cctype>
#include <complex>
#include <cstdio>
#include <cstring>
#include <ctime>
#include <deque>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <utility>
#include <valarray>
#include <vector>
using namespace std;
#include <ext/algorithm>
#include <ext/functional>
#include <ext/hash_map>
#include <ext/hash_set>
#include <ext/iterator>
#include <ext/numeric>
#include <ext/rope>
#include <ext/slist>
using namespace __gnu_cxx;
#include <boost/rational.hpp>
#include <boost/regex.hpp>
#include <boost/thread.hpp>
#include <boost/thread/mutex.hpp>
using namespace boost;
#define LL long long
#define VI vector<int>
#define VS vector<string>
#define VLL vector<long long>
#define VD vector<double>
#define VVI vector< vector<int> >
#define VVS vector< vector<string> >
#define VVLL vector< vector<long long> >
#define VVD vector< vector<double> >
#define HMII hash_map<int,int>
#define HMIS hash_map<int,string>
#define HMSI hash_map<string,int,stringhash>
#define HMSS hash_map<string,string,stringhash>
#define PII pair<int,int>
#define PL4 pair<long long,long long>
#define PDD pair<double,double>
#define VPII vector< pair<int,int> >
#define OSS ostringstream
#define ISS istringstream
#define ALL(x) x.begin(),x.end()
#define PB push_back
#define MP make_pair
#define forUp(i,n) for (int i=0; i<n; i++)
#define forDown(i,n) for (int i=n-1; i>=0; i--)
#define forEach(it,c) for (typeof(c.begin()) it = c.begin(); it!=c.end(); ++it)
#define for2d(i,j,v) for (int i=0; i<v.size(); i++) for (int j=0; j<v[i].size(); j++)
#define fir(n) for (int i=0; i<n; i++)
#define fjr(n) for (int j=0; j<n; j++)
#define fkr(n) for (int k=0; k<n; k++)
#define firv(v) for (int i=0; i<v.size(); i++)
#define fjrv(v) for (int j=0; j<v.size(); j++)
#define fkrv(v) for (int k=0; k<v.size(); k++)
#define INF 1000000000
#define EPS 1e-12
#define PI acos(-1.0L)
#define ZERO(arr) memset(arr, 0, sizeof(arr))
string d2s(double d) {
  ostringstream oss; oss << setprecision(12) << d; return oss.str();
}


struct semaphore {
  int count;
  mutex mtx;
  condition_variable cond;
  semaphore(int count_) : count(count_) {}
  void acquire() {
    unique_lock<mutex> lock(mtx);
    while (!count) cond.wait(lock);
    count--;
  }
  void release() {
    { lock_guard<mutex> lock(mtx); count++; }
    cond.notify_one();
  }
};

semaphore cin_semaphore(1);

struct RunnerBase {
  bool indone() {
    cin_semaphore.release();
    return false;
  }
};

//######################################################################

#line 2
struct Runner : RunnerBase {

  void run(istream &cin, ostream &cout) {
    int N, W, L; cin >> N >> W >> L;
    VPII r(N); firv(r) {cin >> r[i].first;r[i].second=i;}
    sort(ALL(r)); reverse(ALL(r));
    if (indone()) return;
    vector<pair<double, double> > res(N);
    int dummy;
    for (dummy=0;dummy<2;dummy++) {
      VPII hor; hor.PB(MP(W, L));
      bool cnt = false;
      firv(r) {
	int t = 2*r[i].first;
	int k=-1;
	double x = 0.0;
	fjrv(hor) {
	  if ((hor[j].first >= t && (2*hor[j].second >= t || hor[j].second==L)))
	    {k = j; break;}
	  x += hor[j].first;
	}
	if (k==-1) {
	  if (dummy==1) { cerr << "fail" << endl; return; }
	  res.clear();
	  res.resize(N);
	  swap(W,L);
	  cnt = true;
	  break;
	}
	res[r[i].second] = MP(x + r[i].first, max(0, hor[k].second - r[i].first));
	if (res[r[i].second].second > L) {cerr << "OOOPS" << r[i].first << " " << hor[k].second << endl; return; }
      hor.insert(hor.begin() + k, hor[k]);
      hor[k].first = t;
      hor[k].second = max(-1, hor[k].second-t);
      hor[k+1].first -= t;
      }
      if (cnt) continue;
      break;
    }
    fir(N)
      fjr(N)
      if (i!=j) {
	double ix=res[r[i].second].first;
	double iy=res[r[i].second].second;
	double jx=res[r[j].second].first;
	double jy=res[r[j].second].second;
	assert(ix >=0);
	assert(ix <= W);
	assert(iy >=0);
	assert(iy <= L);
	assert(jx >=0);
	assert(jx <= W);
	assert(jy >=0);
	assert(jy <= L);
	double rd = r[i].first + r[j].first;
	assert((ix-jx)*(ix-jx) + (iy-jy)*(iy-jy) >= (rd)*(rd));
      }
    firv(res) {
      if (dummy==1) {
	cout << d2s(res[i].second) << " " << d2s(res[i].first) << " ";
      } else {
	cout << d2s(res[i].first) << " " << d2s(res[i].second) << " ";
      }
    }
      cout << endl;

  }
};

//######################################################################

semaphore concurrency_semaphore(4);

void run_and_delete(Runner *r, istream *cin, ostream *cout) {
  r->run(*cin, *cout);
  delete r;
  concurrency_semaphore.release();
}

int main(int argc, const char **argv) {
  ifstream fin(argc > 1 ? argv[1] : "/dev/stdin");
  ofstream fout(argc > 1 ? (argv[1] + string(".out")).c_str() : "/dev/stdout");
  int T; fin >> T; string dummy; getline(fin, dummy); assert(dummy.empty());
  thread_group threads;
  vector<ostringstream*> couts;
  fir(T) {
    cin_semaphore.acquire();
    concurrency_semaphore.acquire();
    cerr << i << endl;
    couts.push_back(new ostringstream());
    threads.add_thread(new thread(run_and_delete, new Runner, &fin, couts.back()));
  }
  threads.join_all();
  fir(T) {
    fout << "Case #" << (i+1) << ":";
    string s = couts[i]->str();
    if (s[0] != '\n') fout << " ";
    fout << s;
    delete couts[i];
  }
  couts.clear();
  return 0;
}

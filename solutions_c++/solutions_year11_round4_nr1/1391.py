#include <iostream>
#include <sstream>
#include <queue>
#include <map>
#include <set>
#include <vector>
#include <numeric>
#include <algorithm>
#include <string>
#include <complex>

#include <cassert>
#include <cstdlib>
#include <cmath>
#include <cstdio>
#include <cstring>

#define REP(i,e) for(int i=0;i<(int)(e);i++)
#define FOR(i,b,e) for(int i=(int)(b);i<(int)(e);i++)
#define ALL(c) (c).begin(), (c).end()
#define EACH(it,c) for(__typeof((c).begin()) it=(c).begin();it!=(c).end();++it)
#define RALL(c) (c).rbegin(), (c).rend()
#define ALLA(a,n) ((a)+0), ((a)+n)

using namespace std;

typedef long long ll;
typedef vector<int> vint;
typedef vector<long long> vll;
typedef vector<string> vstring;
typedef vector<double> vdouble;

template<class T>void pp(T v,int n){ REP(i,n)cout<<v[i]<< ' ' ; cout << endl; }
template<class T>void pp(T v){ EACH(it,v) cout << *it << ' ' ; cout << endl;  }
template<class T>T& ls(T& a,T b){ if(b<a) a=b; return a; }
template<class T>T& gs(T& a,T b){ if(b>a) a=b; return a; }
inline ll to_i(const string& s){ll n;sscanf(s.c_str(),"%lld",&n);return n;}
inline string to_s(ll n){char buf[32];sprintf(buf,"%lld",n);return string(buf);}

struct __scanner__{ bool e; operator bool(){ return e; } } IN = { false };
inline __scanner__& operator>>(__scanner__& in,int &n)
{ in.e = scanf("%d",&n)==1; return in; }
inline __scanner__& operator>>(__scanner__& in,ll &n)
{ in.e = scanf("%lld",&n)==1; return in; }
inline __scanner__& operator>>(__scanner__& in,double &n)
{ in.e = scanf("%lf",&n)==1; return in; }
inline __scanner__& operator>>(__scanner__& in,char &n)
{ in.e = scanf(" %c",&n)==1; return in; }
inline __scanner__& operator>>(__scanner__& in,string &n) // BUFFER SIZE!
{ static char buf[1000000]; in.e = scanf(" %s",buf)==1; n = buf; return in; } 

#include <fstream>

#ifndef SINGLE_PROC
#include <mpi.h>
class SolverBaseParallel{
protected:
  int MPI_NumProcs;
  int MPI_Rank;
  int CaseCount;

  ifstream is;
  ofstream os;

public:
  SolverBaseParallel(){
    MPI_NumProcs = MPI::COMM_WORLD.Get_size();
    MPI_Rank = MPI::COMM_WORLD.Get_rank();
  }
  void run(char *input_filename){
    is.open(input_filename, ios::in);
    is >> CaseCount;

    REP(i,CaseCount){
      input();
      if(i % MPI_NumProcs == MPI_Rank){
	cout << "proc " << MPI_Rank << " solves case " << i << endl;

	char buf[32]; sprintf(buf, "out_case%04d", i);
	os.open(buf, ios::out);
	os << "Case #" << i+1 << ": ";
	solve();
	os.close();
      }
    }
  }
  virtual void input() = 0;
  virtual void solve() = 0;
  virtual ~SolverBaseParallel(){
    MPI::Finalize();
  }
};
#endif

struct dat{
  double dist, w, r;
};
bool cmp(const dat& a,const dat& b){
  return a.w < b.w;
}



class SolverBaseSingle{
protected:
  int CaseCount;

  ifstream is;
  ofstream os;

public:
  SolverBaseSingle(){
  }
  void run(char *input_filename){
    is.open(input_filename, ios::in);
    is >> CaseCount;

    REP(i,CaseCount){
      input();
      char buf[32]; sprintf(buf, "out_case%04d", i);
      clog << "solving case " << i << "..." << endl;
      os.open(buf, ios::out);
      os << "Case #" << i+1 << ": ";
      solve();
      os.close();
    }
  }
  virtual void input() = 0;
  virtual void solve() = 0;
  virtual ~SolverBaseSingle(){
  }
};



#ifdef SINGLE_PROC
class Solver : public SolverBaseSingle{
#else
class Solver : public SolverBaseParallel{
#endif
public:
  int w, r, t, n, x;
  vint src,dst,vel;
  void init(){
  }
  void input(){
    // INPUT FROM is!
    init();
    is >> x >> w >> r >> t >> n;
    src = vint(n);
    dst = vint(n);
    vel = vint(n);
    REP(i,n){
      is >> src[i];
      is >> dst[i];
      is >> vel[i];
    }
  }

  void solve(){
    vector<double> cost(n, 1e256);
    vint prev(n, -1);
    REP(i,n) cost[i] = (double)src[i] / w + (double)(dst[i]-src[i]) / (w + vel[i]);
    
    REP(i,n) REP(j,n) if(dst[j]<=src[i]){
      double nc = cost[j] + (double)(src[i]-dst[j])/w + 
	(double)(dst[i]-src[i])/(w + vel[i]);
      if(nc < cost[i]){
	cost[i] = nc;
	prev[i] = j;
      }
    }
    assert(n > 0);

    vint path;
    
    int best = 0;
    REP(i,n) if(cost[i]+(double)(x-dst[i])/w < cost[best]+(double)(x-dst[best])/w) best = i;
    for(int i = best; i != -1; i = prev[i]) path.push_back(i);
    reverse(ALL(path));

    double res = 0;
    double dt = t;

    vector<dat> v;
    v.push_back((dat){src[path[0]], w, r});
    REP(i,path.size()-1) 
      v.push_back((dat){src[path[i+1]]-dst[path[i]], w, r});

    REP(i,path.size())
      v.push_back((dat){dst[path[ i ]]-src[path[i]], w+vel[path[i]], r+vel[path[i]]});

    v.push_back((dat){x-dst[path.back()], w, r});

    sort(ALL(v),cmp);
    REP(i,v.size()) res += calc(v[i].dist, v[i].w, v[i].r, dt);

    char buf[32]; sprintf(buf, "%.12lf\n", res); os << buf;
    // OUTPUT TO os!
  }
  double calc(double dist, double w, double r, double &t){
    double runTime = min(t, dist / r);
    t -= runTime;
    dist -= r * runTime;
    return runTime + dist / w;
  }

};

int main(int argc, char *argv[]){
#ifndef SINGLE_PROC
  MPI::Init(argc, argv);
#endif
  Solver *solver = new Solver();
  solver->run(argv[argc - 1]);
  delete solver;
}


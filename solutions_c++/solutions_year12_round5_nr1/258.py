// compile with "g++ XXX.cc -mno-cygwin -O2" in Cygwin (gcc version 3.4.4)

#include<iostream>
#include<sstream>
#include<cstdio>
#include<cstring>
#include<algorithm>
#include<string>
#include<vector>
#include<cmath>
#include<set>
#include<map>
#include<stack>
#include<queue>
#include<numeric>
#include<functional>
#include<complex>
#include<cassert>

#include<windows.h>
#include<process.h>

using namespace std;
#define BET(a,b,c) ((a)<=(b)&&(b)<(c))
#define FOR(i,n) for(int i=0,i##_end=(int(n));i<i##_end;i++)
#define FOR3(i,a,b) for(int i=a,i##_end=b;i<i##_end;i++)
#define FOR_EACH(it,v) for(__typeof(v.begin()) it=v.begin(),it_end=v.end() ; it != it_end ; it++)
#define SZ(x) (int)(x.size())
#define ALL(x) (x).begin(),(x).end()
#define MP make_pair
#define CLS(x,val) memset((x) , val , sizeof(x)) 
typedef long long ll_t;
typedef long double ld_t;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef complex<int> xy_t;

template<typename T> void debug(T v , string delimiter = "\n")
{ for(__typeof(v.begin()) it=v.begin(),it_end=v.end() ; it != it_end ; it++) cout << *it << delimiter; cout << flush ;}

int dx[]  = {0,1,0,-1};
int dy[]  = {1,0,-1,0};
string ds = "SENW";

const int CPU_NUM=1;

const double PI = 4.0*atan(1.0);

struct data
{
  int L,P,id;
  friend bool operator<(const data& d , const data& d2){
    if(d.P != d2.P) return d.P > d2.P;
    if(d.P == 0){
      if(d.id != d2.id) return d.id < d2.id;
    }else{
      if(d.L != d2.L) return d.L < d2.L;
    }
    return d.id < d2.id;
  }
};

struct solver 
{
  static void init(){ 
  }
  void solve()
  {
    int N;
    cin>>N;
    VI L(N),P(N);
    FOR(i,N) cin>>L[i];
    FOR(i,N) cin>>P[i];
    END_INPUT();
    vector<data> dat; 
    FOR(i,N){
      dat.push_back((data){L[i],P[i],i});
    }
    sort(ALL(dat));


    FOR(i,N){
      cout<<(i?" ":"")<<dat[i].id;
    }
  }

// Begin multi thread code 

  string result(){ return cout.str(); }
  void END_INPUT(){
    if(cs){
      LeaveCriticalSection(cs);
      cs=NULL;
    }
  }
  CRITICAL_SECTION* cs;
  ostringstream cout ;   
  solver():cs(NULL){}
};

template<typename T>
class multi_solver
{
  map<int,string> output;
  enum{ RUN = 0 , OUTPUT = 1};
  int cpu ; 
  int running_thread ;
  int outputed ;

  volatile int     case_no;
  int              cases;
  CRITICAL_SECTION mutex[2];
public : 
  multi_solver(int cpu) :
    cpu(cpu) , running_thread(0), outputed(1){    
    case_no=1;
  }

  void wait(){

  }

  void run(){
    scanf("%d",&cases);
    cerr << "Case Num : " << cases << endl;
    InitializeCriticalSection(&mutex[RUN]);
    InitializeCriticalSection(&mutex[OUTPUT]);
    vector<HANDLE> thread_list;
    solver::init();
    for(int i=0; i<cpu; ++i)
      thread_list.push_back( (HANDLE)_beginthreadex(0, 0, &thread_start, this, 0, 0) );
    WaitForMultipleObjects( thread_list.size(), &thread_list[0], TRUE, INFINITE );
    DeleteCriticalSection(&mutex[RUN]);
    DeleteCriticalSection(&mutex[OUTPUT]);
  }

  void output_remain_result()
  {
    for(; output.find(outputed) != output.end() ; outputed++){
      cerr << "[" << outputed << "]" ;
      printf("Case #%d: %s\n" , outputed , output[outputed].c_str());
    }
  }

  void add_output(int case_no , solver* solver)
  {
    output[case_no] = solver->result();
    output_remain_result();
  }

  static unsigned __stdcall thread_start( void* arg ) {
    multi_solver* ms = (multi_solver*) arg;
    for(;;) {
      EnterCriticalSection(&ms->mutex[RUN]);
      const int id = ms->case_no++;
      if(id>ms->cases) { LeaveCriticalSection(&ms->mutex[RUN]); break; }
      solver* solve = new solver();

      solve->cs = &ms->mutex[RUN];
      solve->solve();
      solve->END_INPUT();

      EnterCriticalSection(&ms->mutex[OUTPUT]);
      ms->add_output(id , solve);
      LeaveCriticalSection(&ms->mutex[OUTPUT]);

      delete solve;
    }
    return 0;
  }

};

int main() {
  multi_solver<solver>(CPU_NUM).run();
  return 0 ;
}

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

#include<windows.h>
#include<process.h>

using namespace std;
#define BET(a,b,c) ((a)<=(b)&&(b)<(c))
#define FOR(i,n) for(int i=0,i##_end=(int(n));i<i##_end;i++)
#define SZ(x) (int)(x.size())
#define ALL(x) (x).begin(),(x).end()
#define MP make_pair
#define CLS(x,val) memset((x) , val , sizeof(x)) 
typedef long long ll_t;
typedef long double ld_t;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef complex<int> xy_t;
const double PI = 4.0*atan(1.0);
int dx[] = {0,-1,1,0};
int dy[] = {-1,0,0,1};
struct solver 
{
  static void init(){ 
  }
  int dat[120][120];
  int ans[120][120];
  int H,W,idx;
  void solve()
  {
    cin>>H>>W;
    FOR(i,H) FOR(j,W) cin>>dat[i][j];
    END_INPUT();
    memset(ans , -1 , sizeof(ans));
    idx = 0 ;
    FOR(i,H) FOR(j,W){
      if(ans[i][j]==-1){
        dfs(i,j);
      }
    }
    cout << endl;
    FOR(i,H) {
      FOR(j,W){
        cout << (j?" ":"") << (char)(ans[i][j]+'a');
      }
      cout << endl;
    }
  }
  int dfs(int row , int col)
  {
    if(ans[row][col]!=-1) return ans[row][col];
    int minv = 1<<28;
    int tr=-1,tc=-1;
    FOR(i,4){
      int nr = row + dy[i];
      int nc = col + dx[i];
      if(BET(0,nr,H) && BET(0,nc,W) && minv > dat[nr][nc]){
        minv = dat[nr][nc];
        tr = nr;
        tc = nc;
      }
    }
    int val = 0;
    if(dat[row][col]<=minv){
      val = idx++;
    }else{
      val = dfs(tr,tc);
    }
    return ans[row][col] = val;
  }

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
      printf("Case #%d: %s" , outputed , output[outputed].c_str());
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
  multi_solver<solver>(2).run();
  return 0 ;
}

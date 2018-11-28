#include <iostream>
#include <sstream>
#include <iomanip>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <complex>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <cctype>

#include <pthread.h>

using namespace std;

typedef complex<double> pt;
typedef long long ll;

//-----

template <class T>
class parallel_scheduler{
public:
  parallel_scheduler(int cpu_num):cpu_num(cpu_num){
    T::init();
    init();
  }

  void go(){
    string line;getline(cin,line);
    int cases=atoi(line.c_str());
    for (int i=1;i<=cases;i++){
      T *t=new T();
      t->read();
      while (running>=cpu_num)
	usleep(10*1000);
      schedule(i,t);
    }
    while(running>0)
      usleep(10*1000);
  }

private:
  void init(){
    running=0;
    next=1;
    pthread_mutex_init(&run_m,NULL);
    pthread_mutex_init(&ans_m,NULL);
  }

  void schedule(int cn,T *t){
    pthread_mutex_lock(&run_m);
    running++;
    pthread_mutex_unlock(&run_m);

    pthread_t tid;
    pair<int,pair<T*,parallel_scheduler*> > *p=
      new pair<int,pair<T*,parallel_scheduler*> >(cn,make_pair(t,this));
    pthread_create(&tid,NULL,start,p);
    pthread_detach(tid);
  }

  static void *start(void *arg){
    pair<int,pair<T*,parallel_scheduler*> > *p=
      (pair<int,pair<T*,parallel_scheduler*> >*)arg;
    int cn=p->first;
    T *t=p->second.first;
    parallel_scheduler *ps=p->second.second;
    delete p;

    ostringstream oss;
    t->solve(oss);
    delete t;

    ps->register_ans(cn,oss.str());
    ps->end();

    return NULL;
  }

  void end(){
    pthread_mutex_lock(&run_m);
    running--;
    pthread_mutex_unlock(&run_m);
  }

  void register_ans(int cn,const string &ans){
    pthread_mutex_lock(&ans_m);
    anss.insert(make_pair(cn,ans));
    while(anss.count(next)!=0){
      cout<<"Case #"<<next<<": "<<anss[next]<<endl;
      anss.erase(next);
      next++;
    }
    pthread_mutex_unlock(&ans_m);
  }

  int cpu_num;
  int running;

  map<int,string> anss;
  int next;

  pthread_mutex_t run_m;
  pthread_mutex_t ans_m;
};

template <class T>
class sequential_scheduler{
public:
  sequential_scheduler(){
    T::init();
  }

  void go(){
    string line;getline(cin,line);
    int cases=atoi(line.c_str());
    for (int i=1;i<=cases;i++){
      T *t=new T();
      t->read();
      ostringstream oss;
      t->solve(oss);
      delete t;
      cout<<"Case #"<<i<<": "<<oss.str()<<endl;
    }
  }
};

//-----

class solver;

int main(int argc,char *argv[])
{
  int cpu_num=1;
  if (argc==2) cpu_num=atoi(argv[1]);
  if (cpu_num>1){
    cerr<<"PAR: "<<cpu_num<<endl;
    parallel_scheduler<solver>(cpu_num).go();
  }
  else{
    cerr<<"SEQ:"<<endl;
    sequential_scheduler<solver>().go();
  }
  return 0;
}

//-----

class solver{
public:
  solver(){
  }
  ~solver(){
  }

  static void init(){
  }

  int w,h;
  vector<vector<int> > bd;

  void read(){
    cin>>h>>w;
    bd=vector<vector<int> >(h,vector<int>(w,0));
    for (int y=0;y<h;y++)
      for (int x=0;x<w;x++)
	cin>>bd[y][x];
  }

  void solve(ostream &cout){
    int ans=0;
    for (int c=0;c<(1<<(w*h));c++){
      bool ok=true;
      for (int y=0;y<h;y++){
	for (int x=0;x<w;x++){
	  int cnt=0;
	  for (int dx=-1;dx<=1;dx++){
	    for (int dy=-1;dy<=1;dy++){
	      int cx=x+dx;
	      int cy=y+dy;
	      if (!(cx>=0&&cx<w&&cy>=0&&cy<h)) continue;

	      cnt+=(c>>(cx+cy*w))&1;
	    }
	  }

	  if (bd[y][x]!=cnt){
	    ok=false;
	    goto _next;
	  }
	}
      }

      if (ok){
	int cnt=0;
	for (int x=0;x<w;x++)
	  cnt+=(c>>(x+(h/2)*w))&1;
	ans=max(ans,cnt);
      }
      _next:;
    }
    cout<<ans;
  }
};

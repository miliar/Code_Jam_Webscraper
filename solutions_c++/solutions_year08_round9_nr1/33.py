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

// fenwick tree
class fenwick{
public:
  fenwick(int n) :v(n,0) {}

  ll query(int a){
    return a>=0?v[a]+query((a&(a+1))-1):0;
  }

  ll query(int a, int b){
    return query(b)-query(a-1);
  }

  void inc(int k, int n){
    if (k<(int)v.size()){
      v[k]+=n;
      inc(k|(k+1),n);
    }
  }

private:
  vector<ll> v;
};

class solver{
public:
  solver(){
  }
  ~solver(){
  }

  static void init(){
  }

  int n;
  vector<vector<int> > dat;

  void read(){
    cin>>n;
    dat=vector<vector<int> >(n,vector<int>(3));
    for (int i=0;i<n;i++){
      for (int j=0;j<3;j++)
	cin>>dat[i][j];
    }
  }

  void solve(ostream &cout){
    int ans=0;

    sort(dat.begin(),dat.end());
    multiset<pair<int,int> > rst;

    for (int i=0;i<dat.size();i++){
      int a=dat[i][0];
      rst.insert(make_pair(dat[i][1],dat[i][2]));

      fenwick fw(10001);
      for (multiset<pair<int,int> >::iterator p=rst.begin();
	   p!=rst.end();p++){
	int b=p->first;
	fw.inc(p->second,1);

	int c=10000-a-b;
	if (c<0) continue;
	ans=max(ans,(int)fw.query(0,c));
      }
    }

    cout<<ans;
  }

  /*
  void solve(ostream &cout){
    int ans=0;
    for (int c=0;c<(1<<n);c++){
      int ms[3]={0};
      int pn=0;
      for (int i=0;i<n;i++){
	if (!(c&(1<<i))) continue;
	pn++;
	for (int j=0;j<3;j++)
	  ms[j]=max(ms[j],dat[i][j]);
      }
      int tot=0;
      for (int i=0;i<3;i++)
	tot+=ms[i];
      if (tot<=10000)
	ans=max(ans,pn);
    }
    cout<<ans;
  }
  */
};

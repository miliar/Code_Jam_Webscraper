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
  vector<string> bd;

  vector<int> af,bf,cf;

  vector<vector<int> > tbl;

  vector<int> sctbl;
  vector<int> petbl;

  void read(){
    cin>>h>>w;
    bd=vector<string>(h);
    for (int y=0;y<h;y++)
      cin>>bd[y];
  }

  int rec(int pos, int flg){
    if (pos==h) return 0;

    int &ret=tbl[pos][flg];
    if (ret>=0) return ret;
    ret=0;

    if (cf[pos]==0){
      int c=af[pos];
      int sc=sctbl[c]-petbl[flg&c];
      ret=max(ret, sc+rec(pos+1,c));
      return ret;
    }

    for (int c=0;c<(1<<w);c++){

      /*
      bool ok=true;
      for (int i=0;i<w;i++){
	int b=(c>>i)&1;
	if (bd[pos][i]=='.'&&b){
	  ok=false;
	  break;
	}
	if (bd[pos][i]=='#'&&!b){
	  ok=false;
	  break;
	}
      }
      if (!ok) continue;
      */

      if ((af[pos]&~c)!=0) continue;
      if ((c&bf[pos])!=0) continue;
 
      int sc=sctbl[c]-petbl[flg&c];
      /*
      int sc=0;
      for (int i=0;i<w;i++){
	if (c&(1<<i)){
	  int add=4;
	  if (i>0&&(c&(1<<(i-1)))) add--;
	  if (i<w-1&&(c&(1<<(i+1)))) add--;
	  if (flg&(1<<i)) add-=2;
	  sc+=add;
	}
      }
      */
      //if (pos==0) cout<<sc<<endl;
      //if (pos==0) cout<<hex<<c<<endl;
      ret=max(ret, sc+rec(pos+1,c));
    }
    return ret;
  }

  void solve(ostream &cout){

    for (int y=0;y<h;y++){
      int f=0;
      for (int i=0;i<w;i++)
	if (bd[y][i]=='#')
	  f|=(1<<i);
      af.push_back(f);
    }

    for (int y=0;y<h;y++){
      int f=0;
      for (int i=0;i<w;i++)
	if (bd[y][i]=='.')
	  f|=(1<<i);
      bf.push_back(f);
    }

    for (int y=0;y<h;y++){
      int f=0;
      for (int i=0;i<w;i++)
	if (bd[y][i]=='?')
	  f|=(1<<i);
      cf.push_back(f);
    }

    sctbl=vector<int>(1<<w,0);
    petbl=vector<int>(1<<w,0);

    for (int c=0;c<(1<<w);c++){
      int sc=0,pe=0;
      for (int i=0;i<w;i++){
	if (c&(1<<i)){
	  sc+=4;
	  if (i>0&&(c&(1<<(i-1)))) sc--;
	  if (i<w-1&&(c&(1<<(i+1)))) sc--;
	  pe+=2;
	}
      }
      sctbl[c]=sc;
      petbl[c]=pe;
    }

    tbl=vector<vector<int> >(h,vector<int>(1<<w,-1));
    cerr<<h<<" "<<w<<endl;
    cout<<rec(0,0);
  }
};

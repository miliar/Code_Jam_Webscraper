#include <iostream>
#include <sstream>
#include <iomanip>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <cctype>

#include <pthread.h>

using namespace std;

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

#define PARALLEL

int main(int argc,char *argv[])
{
#ifdef PARALLEL
  int cpu_num=2;
  if (argc==2) cpu_num=atoi(argv[1]);
  cerr<<"PAR: "<<cpu_num<<endl;
  parallel_scheduler<solver>(cpu_num).go();
#else
  cerr<<"SEQ:"<<endl;
  sequential_scheduler<solver>().go();
#endif
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

  void read(){
    int l;cin>>l;
    for (int i=0;i<l;i++){
      string s;
      int t;
      cin>>s>>t;
      while(t--) inp+=s;
    }
  }

  void solve(ostream &cout){
    int cx=0,cy=0;
    int dx=0,dy=2;

    int ofs=6020;
    vector<vector<bool> > ss(12040,vector<bool>(12040,false));
    //set<pair<int,int> > ss;

    for (int i=0;i<inp.length();i++){
      if (inp[i]=='F'){
	int nx=cx+dx;
	int ny=cy+dy;
	ss[(cy+ny)/2+ofs][(cx+nx)/2+ofs]=true;
	cx=nx;
	cy=ny;
      }
      else if (inp[i]=='L'){
	swap(dx,dy);
	dx=-dx;
      }
      else if (inp[i]=='R'){
	swap(dx,dy);
	dy=-dy;
      }
    }

    set<pair<int,int> > pock;

    for (int y=-6011;y<=6011;y+=2){
      bool inside=false;
      int bef_ins=-10000;

      for (int x=-6011;x<=6011;x+=2){
	if (ss[y+ofs][x+1+ofs]){
	  if (inside){
	    bef_ins=x;
	    inside=false;
	  }
	  else{
	    if (bef_ins>-10000){
	      for (int ix=bef_ins+2;ix<=x;ix+=2){
		pock.insert(make_pair(ix,y));
		//cerr<<ix<<" "<<y<<endl;
	      }
	    }
	    inside=true;
	  }
	}
      }
    }

    for (int x=-6011;x<=6011;x+=2){
      bool inside=false;
      int bef_ins=-10000;

      for (int y=-6011;y<=6011;y+=2){
	if (ss[y+1+ofs][x+ofs]){
	  if (inside){
	    bef_ins=y;
	    inside=false;
	  }
	  else{
	    if (bef_ins>-10000){
	      for (int iy=bef_ins+2;iy<=y;iy+=2){
		pock.insert(make_pair(x,iy));
		//cerr<<x<<" "<<iy<<endl;
	      }
	    }
	    inside=true;
	  }
	}
      }
    }

    cout<<pock.size();
  }

  string inp;
};

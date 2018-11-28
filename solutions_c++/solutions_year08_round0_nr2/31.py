// NigelTufnel
// start 21:23 end 21:54

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <vector>
#include <list>
#include <string>
#include <algorithm>

using namespace std;

static char *sep = " \r\n\t";

void chomp(char *s) {
  while(strlen(s)>0 && s[strlen(s)-1] < 32)
    s[strlen(s)-1] = 0;
}

int timeparse(char *p) {
  char *s = strdup(p);
  char *t;
  int v;
  t =strchr(s,':');
  *t = 0;
  v = 60*atoi(s);
  v +=atoi(t+1);
  free(s);
  return v;
}

class trip {
public:
  trip() { source=begin=end=ready=0; }
  trip(int s,int b,int e,int r) {
    source=s; begin=b; end=e; ready=r;
  }
  trip(const trip &c) {
    source=c.source;
    begin=c.begin;
    end=c.end;
    ready=c.ready;
  }
  trip &operator=(const trip &c) {
    source=c.source;
    begin=c.begin;
    end=c.end;
    ready=c.ready;
    return(*this);
  }
  int operator<(const trip &t) const {
    return(begin < t.begin);
  }

  int source,begin,end,ready;
};

class train {
public:
  vector<trip> routine;

  int gap(trip &n) {
    int nr = routine.size();
    if (routine.empty()) return 0;
    if (routine[nr-1].ready > n.begin || 
	routine[nr-1].source == n.source) return -1;
    return(n.begin - routine[nr-1].ready);
  }
};


void solve(int index) {
  int T,NA,NB,i;
  char line[512], *p;
  list<trip> todo;
  list<trip>::iterator ii,tg;
  vector<train> trains;  

  int bg,bgi,gap;
  int ra,rb;

  fgets(line,512,stdin);
  chomp(line);
  T=atoi(line);

  fgets(line,512,stdin);
  p = strtok(line,sep);
  NA=atoi(p);
  p = strtok(NULL,sep);
  NB=atoi(p);

  for(i=0;i<NA;i++) {
    trip t;
    fgets(line,512,stdin);
    //printf("line=%s",line);
    p=strtok(line,sep);
    t.source = 0;
    t.begin=timeparse(p);
    p=strtok(NULL,sep);
    t.end=timeparse(p);
    t.ready=t.end+T;
    todo.push_back(t);
  }
  for(i=0;i<NB;i++) {
    fgets(line,512,stdin);
    p=strtok(line,sep);
    trip t;
    t.source = 1;
    t.begin=timeparse(p);
    p=strtok(NULL,sep);
    t.end=timeparse(p);
    t.ready=t.end+T;
    todo.push_back(t);
  }

  while(!todo.empty()) {
    //printf("todo=%d\n",todo.size());

    tg = todo.begin();
    for(ii=todo.begin();ii!=todo.end();ii++)
      if ( (*ii) < (*tg) )
	tg = ii;


    bg = 99999;
    bgi = -1;

    for(i=0;i<trains.size();i++) {
      gap = trains[i].gap( *tg );
      if (gap >= 0 && gap < bg) {
	bg = gap;
	bgi = i;
      }
    }

    
    if (bgi < 0) {
      // need new train
      train q;
      q.routine.push_back(*tg);
      trains.push_back(q);
    } else {
      // push trip to the latest available train (minimize gap)
      trains[bgi].routine.push_back(*tg);
    }


    todo.erase(tg);
  }
  ra=rb=0;
  for(i=0;i<trains.size();i++)
    if (trains[i].routine[0].source == 0) ra++; else rb++;

  printf("Case #%d: %d %d\n",index,ra,rb);
}

int main(int argc, char **argv) {
  char line[512];
  int i,n;

  fgets(line,512,stdin);
  chomp(line);
  
  n = atoi(line);
  for(i=0;i<n;i++) {
    solve(i+1);
  }
  return 0;
}

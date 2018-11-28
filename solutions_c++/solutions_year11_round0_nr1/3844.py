#include "template.cc"

/* actual solution follows */

void init() {  }

struct lastmove {
  int pos;
  int time; // time of the last button push @pos (we have free moves at time+1 ...)
  lastmove() : pos(1),time(0) {  }
  int push(int topos,int last_push) { // update time of push (to the latter of move time,last_push)+1
    int d=abs(topos-pos);
    pos=topos;
    return time=max(time+d,last_push)+1;
  }
};

int t; // the previous push happened at this time; next push may happen at t+1 or later
lastmove bot[2];
int ci(char c) { return c=='O'; }
void solve() // solve as we read.
{
  t=0;
  bot[0]=bot[1]=lastmove();

  char c;
  int to;
  for (int i=0;i<nfields;++i) {
    read(c);
    read(to);
    t=bot[ci(c)].push(to,t);
  }
  cout<<t;
}

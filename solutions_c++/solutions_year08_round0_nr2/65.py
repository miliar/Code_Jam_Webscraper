#include <iostream>
#include <algorithm>

using namespace std;

#define for_to(i,j,k) for(i=j; i<=k; ++i)
#define for_downto(i,j,k) for(i=j; i>=k; --i)

#define AVAIL 0
#define NEED 1

struct event
{
  int t,type,place;
};

event new_event(int t,int type,int place)
{
  event e;
  e.t=t;
  e.type=type;
  e.place=place;
  return e;
}

bool operator <(event a,event b)
{
  if (a.t != b.t) return a.t < b.t;
  if (a.type != b.type) return a.type < b.type;
  return a.place < b.place;
}

int n_tests,test,delay,place;
int i,j,k;
int n[2],avail[2],needed[2];
event Q[1000];
int h,m,departure,arrival,n_events;

int main()
{
  scanf("%d",&n_tests);
  for_to(test,1,n_tests)
  {
    scanf("%d",&delay);
    scanf("%d %d",&n[0],&n[1]);
    n_events=0;
    for_to(place,0,1)
    {
      for_to(i,1,n[place])
      {
        scanf("%d:%d",&h,&m);
        departure=60*h+m;
        scanf("%d:%d",&h,&m);
        arrival=60*h+m;
        Q[n_events++]=new_event(arrival+delay,AVAIL,1-place);
        Q[n_events++]=new_event(departure,NEED,place);
        //cout << "from " << departure << " to " << arrival << endl;
      }
    }
    //cout << "n_events=" << n_events << endl;
    sort(Q,Q+n_events);
    avail[0]=avail[1]=needed[0]=needed[1]=0;
    for_to(i,0,n_events-1)
    {
      if (Q[i].type==AVAIL)
      {
        ++avail[Q[i].place];
      }
      else
      {
        if (avail[Q[i].place]==0)
        {
          ++needed[Q[i].place];
          ++avail[Q[i].place];
        }
        --avail[Q[i].place];
      }
    }
    printf("Case #%d: %d %d\n",test,needed[0],needed[1]);
  }
  return 0;
}

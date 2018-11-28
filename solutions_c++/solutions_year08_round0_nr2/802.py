#include <stdio.h>
#include <algorithm>
#include <vector>

using namespace std;
class event
{
public:
  int time;
  enum {DEPARTA,DEPARTB,AVAILA,AVAILB} type;
  const int operator< (const event b)
    const
  {
    if (this->time==b.time)
      return this->type>b.type;
    return this->time<b.time;
  }
};


int
main ()
{
  int N, tn;
  scanf ("%d", &N);
  for (tn=0;tn<N;tn++)
    {
      vector <event> events;
      int NA, NB, T, poola=0,poolb=0, depa=0,depb=0, i, h1, m1,h2,m2;
      scanf ("%d", &T);
      scanf ("%d %d", &NA, &NB);
      events.resize (2*(NA+NB));
      for (i=0;i<NA;i++)
	{
	  scanf ("%d:%d %d:%d", &h1,&m1,&h2,&m2);
	  events[2*i].time=60*h1+m1;
	  events[2*i].type=event::DEPARTA;
	  events[2*i+1].time=60*h2+m2+T;
	  events[2*i+1].type=event::AVAILB;	  
	}
      for (;i<NA+NB;i++)
	{
	  scanf ("%d:%d %d:%d", &h1,&m1,&h2,&m2);
	  events[2*i].time=60*h1+m1;
	  events[2*i].type=event::DEPARTB;
	  events[2*i+1].time=60*h2+m2+T;
	  events[2*i+1].type=event::AVAILA;	  
	}
      sort (events.begin (),events.end ());
      for (i=0;i<2*(NA+NB);i++)      
	switch (events[i].type)
	  {
	  case event::DEPARTA:
	    if (poola>0)
	      poola--;
	    else
	      depa++;
	    break;
	  case event::DEPARTB:
	    if (poolb>0)
	      poolb--;
	    else
	      depb++;
	    break;
	  case event::AVAILA:
	    poola++;
	    break;
	  case event::AVAILB:
	    poolb++;
	    break;
	  }
      printf ("Case #%d: %d %d\n",tn+1,depa,depb);
    }
  return 0;
}

//
// Qualification round 2011  problem A
//
// Usually built with g++ 4.4.5 on Linux
//
#include <iostream>
#include <iomanip>
#include <vector>
#include <set>
#include <gmpxx.h>

#include <cstdlib>
#include <math.h>

using namespace std;

enum bot {
     orange,
     blue,
     unknown
};

string to_name( bot b )
{
     switch (b) {
     case orange:
	  return "orange";
     case blue:
	  return "blue";
     default:
	  return "?";
     }
}

struct dest {
     unsigned int pos;
     bot          b;

     dest( unsigned int p, bot bb) : pos(p),b(bb) {}

     dest( void ) {
	  pos=0;
	  b=unknown;
     }
};
 
struct bot_state {
     unsigned int pos;

     bot_state() { pos=1;}
     bot_state(unsigned int p, bool c) { pos=p;}
};

unsigned int next_target=0;
vector<dest> v;
bot_state bot_orange;
bot_state bot_blue;

void step_on( bot b )
{
     unsigned int target_posn = 0;
     bot_state *s = (b==orange ? &bot_orange : &bot_blue);

     for (unsigned int i=next_target; i<v.size(); i++) {
	  if (v[i].b == b) {
	       target_posn = v[i].pos;

	       if (s->pos < target_posn) {
		    s->pos++;
	       } else if (s->pos > target_posn) {
		    s->pos--;
	       }
	       return ;
	  }
     }
}

int main( int argc, char ** argv )
{
     unsigned int n;
     unsigned int i;
     unsigned int r ;
     string w;
     bot b ;
     unsigned int p;

     cin >> n;

     cerr << n << endl;

     for (i=1; i<=n; i++) {
	  
	  // cin >> a >> b >> c ;
	  cin >> r;

	  v.resize(0);
	  for (unsigned int j=0; j<r; j++) {
	       cin >> w;
	       cin >> p ;

	       if (w == "O") {
		    b = orange;
	       } else if (w == "B") {
		    b = blue;
	       }
	       else {
		    b = unknown ;
	       }

	       v.push_back( dest(p,b) );
	  }
	       
	  unsigned int ticks=0;

	  bot_orange = bot_state(1,false);
	  bot_blue   = bot_state(1,false);

	  next_target=0;

	  while (next_target < v.size()) {
	       
	       ticks++;
	       if (v[next_target].b == orange &&
		   bot_orange.pos == v[next_target].pos)
	       {
		    next_target++;
		    step_on(blue);
	       }
	       else if (v[next_target].b == blue &&
			bot_blue.pos == v[next_target].pos)
	       {
		    next_target++;
		    step_on(orange);
	       }
	       else
	       {
		    step_on(blue);
		    step_on(orange);
	       }	       
	  }

	  cout << "Case #" << i << ": ";
	  cout << ticks << endl;
     }

     return 0;
}

#include <iostream>
#include <vector>
#include <map>
#include <sstream>
#include <algorithm>
#include <cmath>
#include <cassert>
#include <list>
#include <queue>

using namespace std;

#define FOR(i,a,b) for(int i=(a); i<(b);++i)
#define REP(i,n) FOR(i,0,n)
#define itype(c) __typeof((c).begin())
#define FORE(c,i) for(itype(c) i=(c).begin();i!=(c).end();++i)
#define PB push_back
#define PF pop_front
#define SORT(c) sort((c).begin(),(c).end());
#define SZ size()
#define PI acos(-1.)
#define HAS(c,e) (find((c).begin(),(c).end(),e)!=(c).end())
#define CHOMP string chomp;getline(cin,chomp)

typedef unsigned long long int ULL;

int main()
{
  int Case;
  cin>>Case;
  REP(_case,Case)
  {
    int seq; cin>>seq;
    queue<int> Oqueue; queue<int> Bqueue; queue<char> OBqueue;
    REP(i,seq) {
      char OB;int button; cin>>OB>>button; 
      OBqueue.push(OB);
      if(OB=='O') { Oqueue.push(button); } else { Bqueue.push(button);} 
    }
 //   while(!Oqueue.empty()) { cout<<"O "<<Oqueue.front()<<endl; Oqueue.pop(); }
 //   while(!Bqueue.empty()) { cout<<"B "<<Bqueue.front()<<endl; Bqueue.pop(); }
 //   while(!OBqueue.empty()) { cout<<"OB "<<OBqueue.front()<<endl; OBqueue.pop(); }
    int Opos=1; int Bpos=1; int time=0;

    while(!OBqueue.empty()) {
      time++;//time lapse by 1 sec
      //cout<<"new sec\n";

      char nextRobotToPush=OBqueue.front();
      bool buttonHasBeenPressedThisSecond=false;

      //O action
      int distOFromNextButton=!Oqueue.empty()?Oqueue.front()-Opos:0;
      if(nextRobotToPush=='O' && distOFromNextButton==0) { /*O pushes*/ OBqueue.pop(); Oqueue.pop(); buttonHasBeenPressedThisSecond=true; }//cout<<"O push\n";}
      else if(distOFromNextButton>0) { /*O step fwd*/ Opos++; }//cout<<"O step fwd\n";}
      else if(distOFromNextButton<0) { /*O step bwd*/ Opos--; }// cout<<"O step bwd\n";}
      else { /*O stays*/ }

      //B action
      int distBFromNextButton=!Bqueue.empty()?Bqueue.front()-Bpos:0;
      if(nextRobotToPush=='B' && distBFromNextButton==0 && !buttonHasBeenPressedThisSecond) { /*B pushes*/ OBqueue.pop(); Bqueue.pop(); }//cout<<"B push\n";}
      else if(distBFromNextButton>0) { /*B step fwd*/ Bpos++; }//cout<<"B step fwd\n";}
      else if(distBFromNextButton<0) { /*B step bwd*/ Bpos--; }// cout<<"B step bwd\n";}
      else { /*B stays*/ }

    }

    printf("Case #%d: %d\n",_case+1,time);
  }

  return 0;
}

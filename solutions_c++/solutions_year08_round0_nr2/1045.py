#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
using namespace std;

#define SMALL_FILE "B-small.in"
#define LARGE_FILE "B-large.in"

struct Event{
  int hh;
  int mm;
  int from; // 0---A, 1---B
  int status; // -1---depart, 1---arrive
};

bool operator<(const Event& a, const Event& b)
{
  if ( a.hh == b.hh )
    if ( a.mm == b.mm )
      return a.status > b.status;
    else
      return a.mm < b.mm;
  else
    return a.hh < b.hh;
}

int main()
{
  //ifstream in(SMALL_FILE);
  ifstream in(LARGE_FILE);
  ofstream out("out.txt");
  vector<Event> elist;
  vector<Event>::iterator it;

  int N, numA, numB, T;
  in>>N;

  // read file
  for ( int ca = 0; ca < N; ca++) {
    elist.clear();
    in>>T>>numA>>numB;
    int countA = numA, countB = numB;
    int minA = numA, minB = numB;
    char tt[10];
    Event ce;
    for ( int i = 0; i < numA; i++ ) {
      in>>tt;
      ce.from = 0;
      ce.hh = (tt[0] - '0') * 10 + tt[1] - '0';
      ce.mm = (tt[3] - '0') * 10 + tt[4] - '0';
      ce.status = -1;
      elist.push_back(ce);
      in>>tt;
      ce.from = 1;
      ce.hh = (tt[0] - '0') * 10 + tt[1] - '0';
      ce.mm = (tt[3] - '0') * 10 + tt[4] - '0';
      ce.hh += (ce.mm + T) / 60;
      ce.mm = (ce.mm + T) % 60;
      ce.status = 1;
      elist.push_back(ce);
    }
    for ( int i = 0; i < numB; i++ ) {
      in>>tt;
      ce.from = 1;
      ce.hh = (tt[0] - '0') * 10 + tt[1] - '0';
      ce.mm = (tt[3] - '0') * 10 + tt[4] - '0';
      ce.status = -1;
      elist.push_back(ce);
      in>>tt;
      ce.from = 0;
      ce.hh = (tt[0] - '0') * 10 + tt[1] - '0';
      ce.mm = (tt[3] - '0') * 10 + tt[4] - '0';
      ce.hh += (ce.mm + T) / 60;
      ce.mm = (ce.mm + T) % 60;
      ce.status = 1;
      elist.push_back(ce);
    }
    
    // sorting
    sort(elist.begin(), elist.end());

    // simulating
    for ( it = elist.begin(); it != elist.end(); it++) {
      //cout<<it->hh<<':'<<it->mm<<endl;
      if ( it->from == 0 ) {
	countA += it->status;
	if ( minA > countA ) minA = countA;
      }
      else {
	countB += it->status;
	if ( minB > countB ) minB = countB;
      }
    }

    out<<"Case #"<<ca+1<<": "<<numA-minA<<' '<<numB-minB<<endl;
    //cout<<"Case #"<<ca+1<<": "<<numA-minA<<' '<<numB-minB<<endl;

  }

  return 0;
}

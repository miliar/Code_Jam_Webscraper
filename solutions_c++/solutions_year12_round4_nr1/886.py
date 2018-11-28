#include <cmath>
#include <cstdio>
#include <algorithm>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <string>
#include <sstream>
#include <utility>
#include <vector>
#include <deque>
#include <list>
#include <iostream>
#include <iomanip>
#include <stdint.h>



using namespace std;


string doCase(istream & in)
{
  ostringstream resultstr;
  int vines;
  in >> vines;
  vector<uint64_t> vine_spot;
  vector<uint64_t> vine_length;
  for(int i = 0; i < vines; i++)
  {
    uint64_t a;
    uint64_t b;
    in >> a >> b;
    vine_spot.push_back(a);
    vine_length.push_back(b);
  }
  uint64_t D;
  in >> D;
  {
  uint64_t bestLength[vines];
  for(int i= 0; i < vines; i++)
    bestLength[i] = 0;
  bestLength[0] = vine_spot[0];
  deque<int> processqueue;
  processqueue.push_back(0);
  while(processqueue.size() != 0)
  {
    int process = processqueue.front();
    processqueue.pop_front();
    uint64_t thisloc = vine_spot[process];
    uint64_t thislen = bestLength[process];
    uint64_t minloc = 0;
    if(thisloc > thislen)
    {
      minloc = thisloc - thislen;
    }
    uint64_t maxloc = thisloc + thislen;
    if(minloc <= D && maxloc >= D)
      return "YES";
    for(int i = process-1; i >= 0 ; i--)
    {
      //look at earlier vines
      uint64_t tloc = vine_spot[i];
      if(tloc < minloc)
        break;
      uint64_t dist = thisloc-tloc;
      uint64_t grabsize = vine_length[i];
      if(dist < grabsize)
        grabsize = dist;

      uint64_t prevl = bestLength[i];
      if(prevl < grabsize)
      {
        bestLength[i] = grabsize;
        processqueue.push_back(i);
      }
    }
    for(int i = process+1; i < vines ; i++)
    {
      //look at later vines
      uint64_t tloc = vine_spot[i];
      if(tloc > maxloc)
        break;
      uint64_t dist = tloc-thisloc;
      uint64_t grabsize = vine_length[i];
      if(dist < grabsize)
        grabsize = dist;

      uint64_t prevl = bestLength[i];
      if(prevl < grabsize)
      {
        bestLength[i] = grabsize;
        processqueue.push_back(i);
      }
    }
  }
  return "NO";
}
}

int main() {
  uint64_t T;
  cin >> T;
  for (uint64_t Ti = 1; Ti <= T; ++Ti) {
    cout << "Case #" << Ti << ": " << doCase(cin) << endl;
  }
  return 0;
}

#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <fstream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <limits>

#include <time.h>

using namespace std;

int Case;

class Station
{
  /*
  struct Trip
  {
    Trip(int the_dep, int the_arv)
      :dep(the_dep),
      arv(the_arv)
    {
    }

    int dep;
    int arv;
  }
  */

public:
  int NTrains;
  multimap<int, int> trip;
  list<int> train;

  Station()
    :trip(), train(), NTrains(0)
  {
  }
  void readTrips(ifstream& ifs, int NTrips)
  {
    if (0 != NTrips)
    {
      for (int i = 0; i < NTrips; ++i)
      {
        int h1, m1, h2, m2;
        char c;
        ifs>>h1>>c>>m1>>h2>>c>>m2;
        trip.insert(pair<int, int>(h1 * 60 + m1, h2 * 60 + m2));
      }
    }
  }
  void sendFirst(Station& dest, int T)
  {
    int dept = trip.begin()->first;
    int arv = trip.begin()->second;
    trip.erase(trip.begin());

    dest.train.push_back(arv + T);
    ++NTrains;

    for (list<int>::iterator itr = train.begin(); itr != train.end(); ++itr)
    {
      if (*itr <= dept)
      {
        train.erase(itr);
        --NTrains;
        break;
      }
    }
  }
};

class Solution
{
public:

  Station A;
  Station B;
  int T;

  void Solve()
  {
    while(true)
    {
      bool sendA = !A.trip.empty() && (B.trip.empty() 
        || A.trip.begin()->first < B.trip.begin()->first);
      if (sendA)
      {
        A.sendFirst(B, T);
      }
      else if (!B.trip.empty())
      {
        B.sendFirst(A, T);
      }
      else
      {
        break;
      }
    }
  }
  int getNTrainsA()
  {
    return A.NTrains;
  }
  int getNTrainsB()
  {
    return B.NTrains;
  }
};


int main(int argc, char* argv[])
{
  ifstream ifs(argv[1]);
  if (!ifs) return 1;

  ofstream ofs(argv[2]);
  if (!ofs) return 2;

  time_t timeStart;
	time(&timeStart);

  int N;
  ifs>>N;

  for(Case = 1; Case <= N; ++Case)
  {
    cout<<"Case #"<<Case<<": "<<endl; 
    Solution s;
    ifs>>s.T;
    int NA, NB;
    ifs>>NA>>NB;
    s.A.readTrips(ifs, NA);
    s.B.readTrips(ifs, NB);
    s.Solve();

    ofs<<"Case #"<<Case<<": "<<s.getNTrainsA()
      <<" "<<s.getNTrainsB()<<endl; 
  }
  
	time_t timeEnd;
	time(&timeEnd);

	double the_diffTime = difftime(timeEnd, timeStart);
	long long diffTime = static_cast<long long>(the_diffTime);

	cout<<diffTime / (60 * 60)<<" hours; "<< diffTime % (60 * 60) / 60<<" minutes; "
		<<diffTime % (60 * 60) % 60<<" seconds; "<<endl;
  
	return 0;
}

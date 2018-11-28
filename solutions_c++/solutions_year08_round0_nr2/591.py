#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct evt_point { int time; bool arrival; bool arriving_at_b; 
  evt_point(int a, bool b, bool c) : time(a), arrival(b), arriving_at_b(c) { }
  bool operator<(const evt_point b) const
  {
    if(time < b.time) return true;
    if(time == b.time && (arrival && !b.arrival)) return true;
    if(time == b.time && arrival == b.arrival && (arriving_at_b && !b.arriving_at_b)) return true;
    return false;
  }
};

int main()
{
  vector<evt_point> coord;
  int N, T, NA, NB;
  cin >> N;

  for(int z = 0; z < N; z++)
    {
      coord.clear();
      cin >> T >> NA >> NB;
      for(int i = 0; i < NA; i++)
	{
	  int hrSt, minSt, hrEnd, minEnd;
          scanf("%d:%d %d:%d", &hrSt, &minSt, &hrEnd, &minEnd);
	  coord.push_back(evt_point(hrSt*60 + minSt, false, false));
	  coord.push_back(evt_point(hrEnd*60 + minEnd + T, true, true));
	}

      for(int i = 0; i < NB; i++)
	{
	  int hrSt, minSt, hrEnd, minEnd;
          scanf("%d:%d %d:%d", &hrSt, &minSt, &hrEnd, &minEnd);
	  coord.push_back(evt_point(hrSt*60 + minSt, false, true));
	  coord.push_back(evt_point(hrEnd*60 + minEnd + T, true, false));
	}

  sort(coord.begin(), coord.end());

  int trains_at_a = 0, trains_at_b = 0;
  int retA = 0, retB = 0;
  for(int i = 0; i < coord.size(); i++)
    {
      int delta;
      if(coord[i].arrival) delta = 1; else delta = -1;
      if(coord[i].arriving_at_b) trains_at_b += delta;
      else trains_at_a += delta;

      retA = max(-trains_at_a, retA);
      retB = max(-trains_at_b, retB);
    }

   cout << "Case #" << z + 1 << ": " << retA << " " << retB << endl;
  }
}

#include <iostream>
#include <string>
#include <set>

using namespace std;

int main()
{
  int nCases, turnAround, nA, nB;
  multiset<pair <int, int> > AEvents, BEvents;
  int i, j, hour, minute;
  string time;
  int ARequired, BRequired;
  multiset<pair <int, int> >::iterator it;

  cin >> nCases;

  for (i = 0; i < nCases; ++i)
  {
    cin >> turnAround >> nA >> nB;
    AEvents.clear();
    BEvents.clear();
    
    for (j = 0; j < nA; ++j)
    {
      cin >> time;
      hour = atoi(time.substr(0,2).c_str());
      minute = atoi(time.substr(3,2).c_str());
      AEvents.insert(pair<int, int>(60 * hour + minute, 1));
      cin >> time;
      hour = atoi(time.substr(0,2).c_str());
      minute = atoi(time.substr(3,2).c_str());
      BEvents.insert(pair<int, int>(60 * hour + minute + turnAround, -1));
    }

    for (j = 0; j < nB; ++j)
    {
      cin >> time;
      hour = atoi(time.substr(0,2).c_str());
      minute = atoi(time.substr(3,2).c_str());
      BEvents.insert(pair<int, int>(60 * hour + minute, 1));
      cin >> time;
      hour = atoi(time.substr(0,2).c_str());
      minute = atoi(time.substr(3,2).c_str());
      AEvents.insert(pair<int, int>(60 * hour + minute + turnAround, -1));
    }

    j = 0;
    ARequired = 0;
    BRequired = 0;

    for (it = AEvents.begin(); it != AEvents.end(); ++it)
    {
      j -= it->second;
      if (j < 0)
      {
	++j;
	++ARequired;
      }
    }

    j = 0;
    for (it = BEvents.begin(); it != BEvents.end(); ++it)
    {
      j -= it->second;
      if (j < 0)
	{
	  ++j;
	  ++BRequired;
	}
    }

    cout << "Case #" << i + 1 << ": " << ARequired << ' ' << BRequired << endl;
  }

  return 0;
}

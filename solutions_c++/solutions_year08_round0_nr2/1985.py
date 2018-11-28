#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
using namespace std;


struct Time {
  int hh;
  int mm;
};

Time addT(Time a, int turnaround)
{
  Time b;

  b.hh = a.hh;
  while (a.mm + turnaround >= 60)
  {
    b.hh = b.hh + 1;
    turnaround = turnaround - 60;
  }
  b.mm = a.mm + turnaround;

  return b;
}

int duration (Time a, Time b)
{
  return (b.hh - a.hh) * 60 + b.mm - a.mm;
}


bool earlier (Time a, Time b)
{
  return (a.hh < b.hh || (a.hh == b.hh && a.mm <= b.mm));
}

struct Schedule {
  char direction;
  Time start;
  Time end;
};


bool compares (const Schedule& s1, const Schedule& s2)
{
  return ((s1.start.hh < s2.start.hh) || (s1.start.hh == s2.start.hh && s1.start.mm <= s2.start.mm));
}


int main (int argc, char* argv[])
{
  ifstream fin (argv[1]);

  if (fin.is_open())
  {
    int samples;
    fin >> samples;
//    cout << "number of samples = " << samples << endl;

    for (int j=0; j < samples; j++)
    {
      int turnT;
//      cout << " !!!!!!! Case " << j << endl;

      fin >> turnT;  
      // get the numbers of A trains and B trains
      int Atrain = 0, Btrain = 0;
      fin >> Atrain >> Btrain;
//      cout << "number of A trains = " << Atrain << endl;
//      cout << "number of B trains = " << Btrain << endl;

      vector<Schedule> trains;

      for (int i=0; i < Atrain; i++)
      {
        string startT, endT;
        fin >> startT >> endT;
        Schedule s;
        s.direction = 'A';
        s.start.hh = atoi(startT.substr(0,2).c_str());
        s.start.mm = atoi(startT.substr(3,2).c_str());
        s.end.hh = atoi(endT.substr(0,2).c_str());
        s.end.mm = atoi(endT.substr(3,2).c_str());
        trains.push_back(s);
      }

      for (int i=0; i < Btrain; i++)
      {
        string startT, endT;
        fin >> startT >> endT;
        Schedule s;
        s.direction = 'B';
        s.start.hh = atoi(startT.substr(0,2).c_str());
        s.start.mm = atoi(startT.substr(3,2).c_str());
        s.end.hh = atoi(endT.substr(0,2).c_str());
        s.end.mm = atoi(endT.substr(3,2).c_str());
        trains.push_back(s);
      }

      sort (trains.begin(), trains.end(), compares);
/*
      for (int i=0; i < Atrain + Btrain; i++)
      {
        cout << trains.at(i).direction << " " << trains.at(i).start.hh << ":" << trains.at(i).start.mm << " " << trains.at(i).end.hh << ":" << trains.at(i).end.mm << endl;
      }
*/
      int counterA = 0, counterB = 0;
      vector<Schedule> retTrains;
      char found = 0;
      while (trains.size() > 0)
      {
        Schedule currT = trains.front();
        // find return train
        found = 0;
        for (int i = 0; i < retTrains.size(); i++)
        {
          if (retTrains.at(i).direction == currT.direction && earlier(retTrains.at(i).start, currT.start))
          {
// cout << "found return train from " << retTrains.at(i).direction << " starting " << retTrains.at(i).start.hh << ":" << retTrains.at(i).start.mm << endl;
            Schedule ret;
            if (currT.direction == 'A')
            {
              ret.direction = 'B';
            }
            else if (currT.direction == 'B')
            {
              ret.direction = 'A';
            }
            ret.start = addT(currT.end, turnT);
            ret.end = addT(ret.start, duration(retTrains.at(i).start, retTrains.at(i).end));
            retTrains.erase(retTrains.begin()+i);
            trains.erase(trains.begin());
            retTrains.push_back(ret);
            sort (retTrains.begin(), retTrains.end(), compares);
            found = 1;
            break;
          }
        }
        // found no return train
        if (found == 0)
        {
            Schedule ret;
            if (currT.direction == 'A')
            {
              counterA++;
              ret.direction = 'B';
            }
            else if (currT.direction == 'B')
            {
              counterB++;
              ret.direction = 'A';
            }
            ret.start = addT(currT.end, turnT);
            ret.end = addT(ret.start, duration(currT.start, currT.end));
            trains.erase(trains.begin());
            retTrains.push_back(ret);
            sort (retTrains.begin(), retTrains.end(), compares);
// cout << "found NO return train starting " << currT.start.hh << ":" << currT.start.mm << endl;
        }
      }
      cout << "Case #" << j+1 << ": " << counterA << " " << counterB << endl;
    }
  }

  return 0;
}

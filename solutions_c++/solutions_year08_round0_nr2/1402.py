#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <sstream>
#include <list>
#include <algorithm>

using namespace std;


template<class T>
void k_readline(istream &in, T &t)
{
  string line;
  getline(in, line);
  istringstream ss(line);
  ss >> t;
}


template<class T1, class T2>
void k_readline(istream &in, T1 &t1, T2 &t2)
{
  string line;
  getline(in, line);
  istringstream ss(line);
  ss >> t1 >> t2;
}

template<class T1, class T2, class T3>
void k_readline(istream &in, T1 &t1, T2 &t2, T3 &t3)
{
  string line;
  getline(in, line);
  istringstream ss(line);
  ss >> t1 >> t2 >> t3;
}

template<class T>
void convert(const string &s, T &t)
{
  istringstream ss(s);
  ss >> t;
}


struct Time
{
  unsigned hr;
  unsigned min;

  Time(): hr(0), min(0) 
  {}

  Time(unsigned ahr, unsigned amin): hr(ahr), min(amin) 
  {}

  Time(string time)
  {
    convert(time.substr(0,2), hr);
    convert(time.substr(3,2), min);
  }
};

bool operator<(const Time &t1, const Time &t2)
{
  if(t1.hr < t2.hr) return true;
  if( (t1.hr == t2.hr) && (t1.min < t2.min) ) return true;
  return false;
}
bool operator==(const Time &t1, const Time &t2)
{
  if( (t1.hr == t2.hr) && (t1.min == t2.min) ) return true;
  return false;
}
bool operator>(const Time &t1, const Time &t2)
{
  return !(t1<t2) && !(t2==t1);
}
bool operator<=(const Time &t1, const Time &t2)
{
  return (t1<t2)||(t1==t2);
}
bool operator>=(const Time &t1, const Time &t2)
{
  return (t1>t2)||(t1==t2);
}
Time addMins(const Time &t, unsigned mins)
{
  Time t1 = t;
  t1.min+=mins;
  if( t1.min >= 60 )
  {
    t1.min -= 60;
    t1.hr += 1;
  }
  return t1;
}


struct Trip
{
  bool direction;
  Time start;
  Time end;

  Trip(bool adir, string astart, string aend)
    : direction(adir), start(astart), end(aend)
  {}

};
bool operator<(const Trip &t1, const Trip &t2)
{
  return t1.start < t2.start;
}
bool operator==(const Trip &t1, const Trip &t2)
{
  return t1.start == t2.start;
}


ostream& operator<<(ostream& out, const Time &time)
{
  out << time.hr << ":" << time.min;
}

ostream& operator<<(ostream& out, const Trip &trip)
{
  if(trip.direction) out << "[A->B ";
  else out << "[B->A ";
  out << trip.start << " " << trip.end << "]";
}

bool enoughTime(const Trip &t1, const Trip &t2, unsigned t)
{
  if (t1.direction == t2.direction) return false;

  Time end = t1.end;
  end.min += t;
  if( end.min >=60 )
  {
    end.hr += 1;
    end.min -= 60;
  }

  Time start = t2.start;

  if( 
      (end.hr < start.hr) ||
      ((end.hr==start.hr) && (end.min<=start.min))
    )
  {
    return true;
  }

  return false;
}

void compute(vector<Trip> &atrips, const unsigned &t, unsigned &astarta, unsigned &astartb)
{
  list<list<Trip> > trips;

  for(unsigned i=0; i<atrips.size(); i++)
  {
    list<Trip> lt;
    lt.push_back(atrips[i]);
    trips.push_back(lt);
  }

  bool run = true;
  while(run)
  {
    run = false;
    for(list<list<Trip> >::iterator it1=trips.begin(); it1!=trips.end(); it1++)
    {
      for(list<list<Trip> >::iterator it2=trips.begin(); it2!=trips.end(); it2++)
      {
        if(it2 == it1)
        {
          continue;
        }
        // try to append it2 to it2
        else if( enoughTime( it1->back(), it2->front(), t ) )
        {
          copy(it2->begin(), it2->end(), back_inserter(*it1));
          trips.erase(it2);
          run = true;
          break;
        }
      }
      if(run) break;
    }
  }

  for(list<list<Trip> >::iterator it1=trips.begin(); it1!=trips.end(); it1++)
  {
    if(it1->front().direction) astarta++;
    else astartb++;

    /*for(list<Trip>::iterator it2=it1->begin(); it2!=it1->end(); it2++)
    {
      cout << *it2 << " ";
    }
    cout << endl;*/
  }

}

int main(int argc, char *argv[])
{
  ifstream in(argv[1]);

  unsigned n,na,nb;

  string line;

  k_readline(in, n);

  for(unsigned i=1; i<=n; i++)
  {
    unsigned t,na,nb;

    k_readline(in, t);
    k_readline(in, na, nb);

    vector<Trip> trips;
    for(int a=0; a<na; a++)
    {
      string st, en;
      k_readline(in, st, en);
      trips.push_back(Trip(true, st, en));
    }
    for(int a=0; a<nb; a++)
    {
      string st, en;
      k_readline(in, st, en);
      trips.push_back(Trip(false, st, en));
    }
    unsigned counta=0, countb=0;
    sort(trips.begin(), trips.end());
    compute(trips, t, counta, countb);

    cout << "Case #" << i << ": " << counta << " " << countb << endl;
  }

  return 0;
}


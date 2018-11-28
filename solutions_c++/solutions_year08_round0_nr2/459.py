#include <iostream>
#include <string>
#include <vector>
#include <list>
#include <algorithm>
using namespace std;

//typedef unsigned long long tull;
//const int MAX = 100000;

struct Ttrip
{
  int depart;
  int arrive;
  bool stA;

};

struct comp
{
     bool operator()(Ttrip rpStart, Ttrip rpEnd)
     {
          return rpStart.depart < rpEnd.depart;
     }
};

int main() 
{
  freopen("B-large.in", "rt", stdin);
  freopen("B-large.out", "wt", stdout);
  int N;
  cin >> N;

  int T, NA, NB, hh, mm, sumA, sumB;
  char ch;
  vector<Ttrip> trs;
  Ttrip train;
  list<Ttrip*> pendA, pendB;
  //list<Ttrip>::iterator it;

  for (int inn=0; inn<N; ++inn)
  {
    trs.clear();
    pendA.clear(); pendB.clear(); sumA = 0; sumB = 0;
    cin >> T >> NA >> NB;
    for (int i=0; i<NA; ++i)
    {
      cin >> hh >> ch >> mm;
      train.depart = hh*60+mm;
      cin >> hh >> ch >> mm;
      train.arrive = hh*60+mm+T;
      train.stA = true;
      trs.push_back(train);
    }
    for (int i=0; i<NB; ++i)
    {
      cin >> hh >> ch >> mm;
      train.depart = hh*60+mm;
      cin >> hh >> ch >> mm;
      train.arrive = hh*60+mm+T;
      train.stA = false;
      trs.push_back(train);
    }

    sort(trs.begin(), trs.end(),comp()); 

    for (unsigned int i=0; i<trs.size(); ++i)
    {
      if (trs[i].stA)
      {
        if (!pendA.empty())
        {
          list<Ttrip*>::iterator it = pendA.begin();
          while (it != pendA.end() && (*it)->arrive > trs[i].depart)
            ++it;
          if (it == pendA.end())
          {
            ++sumA;
            pendB.push_back(&trs[i]);
          }
          else
          {
            pendA.erase(it);
            pendB.push_back(&trs[i]);
          }
        }
        else //(!pendA.empty())
        {
          ++sumA;
          pendB.push_back(&trs[i]);
        }
      }
      else //  (trs[i].stA)
      {
        if (!pendB.empty())
        {
          list<Ttrip*>::iterator it = pendB.begin();
          while (it != pendB.end() && (*it)->arrive > trs[i].depart)
            ++it;
          if (it == pendB.end())
          {
            ++sumB;
            pendA.push_back(&trs[i]);
          }
          else
          {
            pendB.erase(it);
            pendA.push_back(&trs[i]);
          }
        }
        else //(!pendA.empty())
        {
          ++sumB;
          pendA.push_back(&trs[i]);
        }      
      }

    }
    cout << "Case #" << inn+1 << ": " << sumA << " " << sumB << endl;
  }
  return 0;
}

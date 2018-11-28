#include <vector>
#include <list>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <cstdlib>
#include <cstring>

struct itin
{
  int d;
  int a;
  int station;
};

bool operator<(const itin &a, const itin &b)
{
  return a.d < b.d;
}

std::ostream& operator<< (std::ostream& os, const itin& q)
{
  os << "depart:"<<q.d<<" arrive:"<<q.a<<"\n";
  return os;
}
std::istream& operator>> (std::istream& is, itin& q)
{
  char dep[255];
  char arr[255];
  char depm[3];
  char arrm[3];
  char deph[3];
  char arrh[3];
  is >> dep;
  is >> arr;

  deph[0] = dep[0]; deph[1] = dep[1]; deph[2] = '\0';
  depm[0] = dep[3]; depm[1] = dep[4]; depm[2] = '\0';
  arrh[0] = arr[0]; arrh[1] = arr[1]; arrh[2] = '\0';
  arrm[0] = arr[3]; arrm[1] = arr[4]; arrm[2] = '\0';

  int ah, am, dh, dm;
  ah = std::atoi(arrh);
  dh = std::atoi(deph);
  am = std::atoi(arrm);
  dm = std::atoi(depm);

  q.a = 60*ah + am;
  q.d = 60*dh + dm;
  return is;
}
void readProblem(std::ifstream &f, std::vector<itin> &sched)
{
  int T;
  f >> T;
  int na, nb;
  f >> na >> nb;
  for (int i = 0; i < na; i++)
  {
    itin q;
    f >> q;
    q.a += T;
    q.station = 0;
    sched.push_back(q);
  }
  for (int i = 0; i < nb; i++)
  {
    itin q;
    f >> q;
    q.a += T;
    q.station = 1;
    sched.push_back(q);
  }
}


void findAllotment(std::vector<itin> &sched, int *t)
{
  t[0] = 0;
  t[1] = 0;
  std::sort(sched.begin(), sched.end());
  std::list<int> train_avail[2];
  for (int i=0; i < sched.size(); i++)
  {
    int station = sched[i].station;
    std::list<int>::iterator next_train = train_avail[station].end();
    int earliest_arrival = sched[i].d;
    for (std::list<int>::iterator j = train_avail[station].begin();
        j != train_avail[station].end();
        ++j)
    {
        if ( (*j) <= earliest_arrival)
        {
          earliest_arrival = (*j);
          next_train = j;
        }
    }
    if (next_train == train_avail[station].end())     //new train
    {
      t[station]++;
      train_avail[1-station].push_back(sched[i].a);
    }
    else
    {
      train_avail[1-station].push_back(sched[i].a);
      train_avail[station].erase(next_train);
    }

  }
}
int main(int argc, char **argv)
{
  std::ifstream f(argv[1]);
  int ncases;
  f >> ncases;
  for (int i=0; i < ncases; i++)
  {
    int t[2];
    std::vector<itin> sched;
    readProblem(f,sched);
    findAllotment(sched, t);
    std::cout <<"Case #"<<i+1<<": "<<t[0]<<" "<<t[1]<<"\n";
  }
  return 0;
}

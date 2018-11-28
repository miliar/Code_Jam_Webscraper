#include <iostream>
#include <deque>
#include <algorithm>
#include <fstream>

class Time {
public:
  Time(int dep, int arv):dep(dep), arv(arv) {}

  int dep;
  int arv;

  bool operator<(const Time& time) const {
    return dep < time.dep;
  }
};

class Count {
public:
  Count():numA(0), numB(0) {}

  int numA;
  int numB;
};

int atstation(std::deque<Time>& table,
	      std::deque<int>& availDep,
	      std::deque<int>& availArv,
	      int now,
	      int tat)
{
  if(!table.empty() && now == table[0].dep) {
    int availTime = table[0].arv+tat;

    std::deque<int>::iterator i = std::lower_bound(availArv.begin(),
						   availArv.end(),
						   availTime);

    availArv.insert(i, availTime);

    table.pop_front();
    if(!availDep.empty() && availDep[0] <= now) {
      availDep.pop_front();
      return 0;
    } else {
      return 1;
    }
  }
  return 0;
}
	      

void countTrains(std::deque<Time>& tableA,
		 std::deque<Time>& tableB,
		 std::deque<int>& availA,
		 std::deque<int>& availB,
		 int now,
		 int tat,
		 Count& count)
{
  if(tableA.empty() && tableB.empty()) {
    return;
  }
  if(tableA.empty()) {
    now = tableB[0].dep;
  } else if(tableB.empty()) {
    now = tableA[0].dep;
  } else {
    now = std::min(tableB[0].dep, tableA[0].dep);
  }
  count.numA += atstation(tableA, availA, availB, now, tat);
  count.numB += atstation(tableB, availB, availA, now, tat);

  countTrains(tableA, tableB, availA, availB, now, tat, count);
}

int main(int argc, char** argv)
{
  std::ifstream in(argv[1]);

  int numCase;
  in >> numCase;
  for(int cases = 0; cases < numCase; ++cases) {
    int tat;
    in >> tat;
    int numA;
    int numB;
    in >> numA >> numB;
    in >> std::ws;

    std::deque<Time> tableA;
    std::deque<Time> tableB;

    for(int i = 0; i < numA; ++i) {
      std::string dep;
      in >> dep;
      int h1;
      int m1;
      sscanf(dep.c_str(), "%d:%d", &h1, &m1);
      std::string arv;
      in >> arv;
      int h2;
      int m2;
      sscanf(arv.c_str(), "%d:%d", &h2, &m2);
      tableA.push_back(Time(h1*60+m1, h2*60+m2));
    }
    for(int i = 0; i < numB; ++i) {
      std::string dep;
      in >> dep;
      int h1;
      int m1;
      sscanf(dep.c_str(), "%d:%d", &h1, &m1);
      std::string arv;
      in >> arv;
      int h2;
      int m2;
      sscanf(arv.c_str(), "%d:%d", &h2, &m2);
      tableB.push_back(Time(h1*60+m1, h2*60+m2));
    }

    std::deque<int> availA;
    std::deque<int> availB;

    std::sort(tableA.begin(), tableA.end());
    std::sort(tableB.begin(), tableB.end());
    Count c;
    countTrains(tableA, tableB, availA, availB, 0, tat, c);
    
    std::cout << "Case #" << cases+1 << ": "
	      << c.numA << " " << c.numB << std::endl;
  }
}

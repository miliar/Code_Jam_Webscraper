#include <iostream>
#include <fstream>
#include <list>
#include <sstream>

using namespace std;

int calc_money(list<int>&);
int total_money(int, int, list<int>&);

int main(int argc, char** argv)
{
  ifstream input;
  ofstream output;
  if(argc > 1) {
    input.open(argv[1]);
    output.open("output.txt");
  }
  else
    exit(1);
  int i = 0;
  input >> i;
  list<int> groups;
  for(int c = 1; i > 0; i--, c++) {
    int r = 0, k = 0, n = 0;
    stringstream ss;
    input >> r >> k >> n;
    for(; n > 0; n--) {
      int temp = 0;
      input >> temp;
      groups.push_back(temp);
    }
    output << "Case #" << c << ": ";
    ss << total_money(r, k, groups);
    output << ss.str() << endl;
    groups.clear();
  }
  output.close();
}

int calc_money(list<int>& on_coaster)
{
  typedef list<int>::iterator Iter;
  double sum = 0;
  for(Iter it = on_coaster.begin(); it != on_coaster.end(); it++)
    sum += *it;
  return sum;
}

int total_money(int r, int k, list<int>& groups)
{
  int sum = 0;
  list<int> on_coaster;
  for(; r > 0; r--) {
    int on_coast = 0;
    while(on_coast < k) {
      int temp = groups.front();
      if(on_coast + temp <= k) {
	on_coast += temp;
	groups.pop_front();
      }
      else
	break;
      on_coaster.push_back(temp);
    }
    sum += calc_money(on_coaster);
    groups.splice(groups.end(), on_coaster);
  }
  return sum;
}

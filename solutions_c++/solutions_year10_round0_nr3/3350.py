#ifndef themepark
#define themepark


#include <vector>
#include <algorithm>
#include <numeric>
#include <stdexcept>
#include <iostream>
#include <cassert>


double average(std::vector<long> v, int n);
unsigned long long earned_euros(long R, long k, const std::vector<long> groups);

class CircQueue
{
public:
  CircQueue(std::vector<long> init_list);
  long length();
  void inc_head(int by);
  void inc_head() { inc_head(1); };
  long at_head() { return c[head]; };
  long pop_head();
  void return_all_passangers();
  
//private:
  std::vector<long> c;
  long N;
  long head;
  long tail;
  long len;
};





#endif
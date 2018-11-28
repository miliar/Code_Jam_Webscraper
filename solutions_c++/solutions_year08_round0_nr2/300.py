#include <iostream>
#include <map>
#include <set>

typedef int minutes_t;

minutes_t parse(const std::string &str)
{
  return ((str[0] - '0') * 10 + (str[1] - '0')) * 60
    + (str[3] - '0') * 10 + (str[4] - '0');
}

void read(std::multimap<minutes_t, int> &src,
          std::multimap<minutes_t, int> &dst,
          minutes_t turnaround)
{
  std::string line;
  std::getline(std::cin, line);
  minutes_t need = parse(line.substr(0, 5));
  minutes_t ready = parse(line.substr(6, 5)) + turnaround;
  src.insert(std::make_pair(need, -1));
  dst.insert(std::make_pair(ready, +1));
}

int need(const std::multimap<minutes_t, int> &schedule)
{
  int worst = 0;
  int cur = 0;
  for (std::multimap<minutes_t, int>::const_iterator it = schedule.begin();
       it != schedule.end(); ) {
    minutes_t time = it->first;
    do {
      cur += it->second;
      ++it;
    } while (it != schedule.end() && it->first == time);
    if (cur < worst)
      worst = cur;
  }
  return -worst;
}

void calc()
{
  minutes_t turnaround;
  size_t nab, nba;
  std::cin >> turnaround >> nab >> nba;
  std::string dummy;
  std::getline(std::cin, dummy);

  std::multimap<minutes_t, int> a, b;

  for (size_t i = 0; i < nab; i++)
    read(a, b, turnaround);
  for (size_t i = 0; i < nba; i++)
    read(b, a, turnaround);
  std::cout << need(a) << " " << need(b) << std::endl;
}

int main()
{
  size_t count;
  std::cin >> count;
  for (size_t i = 0; i < count; i++) {
    std::cout << "Case #" << (i + 1) << ": ";
    calc();
  }
}

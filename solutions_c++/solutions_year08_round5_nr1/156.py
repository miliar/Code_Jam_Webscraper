#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <iostream>

class Plane {
public:

  Plane(): x(0), y(0), dir(SOUTH) {}

  void forward() {
    //std::cerr << "forward" << std::endl;
    switch (dir) {
    case NORTH:
      rows[y++].insert(x);
      break;
    case EAST:
      cols[x++].insert(y);
      break;
    case SOUTH:
      rows[--y].insert(x);
      break;
    case WEST:
      cols[--x].insert(y);
      break;
    default:
      abort();
    }
  }

  void left() {
    //std::cerr << "left" << std::endl;
    dir = (dir_t)(((int)dir + 3) % 4);
  }

  void right() {
    //std::cerr << "right" << std::endl;
    dir = (dir_t)(((int)dir + 1) % 4);
  }

  void done() {
    if (x || y) {
      //std::cerr << "End of walk: " << x << ", " << y << std::endl;
      abort();
    }
  }

  size_t calc() {
    std::set<std::pair<int, int> > res;
    for (intersect_t::const_iterator it = cols.begin();
         it != cols.end(); ++it) {
      const int x = it->first;
      bool inside = false;
      std::set<int>::const_iterator last_y = it->second.end();
      for (std::set<int>::const_iterator y = it->second.begin();
           y != it->second.end(); ++y) {
        if (!inside && last_y != it->second.end()) {
          for (int i = *last_y; i < *y; i++)
            res.insert(std::make_pair(x, i));
        }
        last_y = y;
        inside = !inside;
      }
    }
    for (intersect_t::const_iterator it = rows.begin();
         it != rows.end(); ++it) {
      const int y = it->first;
      bool inside = false;
      std::set<int>::const_iterator last_x = it->second.end();
      for (std::set<int>::const_iterator x = it->second.begin();
           x != it->second.end(); ++x) {
        if (!inside && last_x != it->second.end()) {
          for (int i = *last_x; i < *x; i++)
            res.insert(std::make_pair(i, y));
        }
        last_x = x;
        inside = !inside;
      }
    }
    return res.size();
  }

private:
  int x, y;

  typedef std::map<int, std::set<int> > intersect_t;
  intersect_t cols, rows;

  enum dir_t { NORTH = 0, EAST = 1, SOUTH = 2, WEST = 3 };
  dir_t dir;

};



void calc()
{
  Plane plane;
  size_t l;
  std::cin >> l;
  for (size_t i = 0; i < l; i++) {
    std::string str;
    size_t rep;
    std::cin >> str >> rep;
    while (rep--) {
      for (size_t j = 0; j < str.size(); j++) {
        switch (str[j]) {
        case 'F':
          plane.forward();
          break;
        case 'L':
          plane.left();
          break;
        case 'R':
          plane.right();
          break;
        }
      }
    }
  }
  plane.done();
  std::cout << plane.calc();
}

int main()
{
  size_t count;
  std::cin >> count;
  for (size_t i = 0; i < count; i++) {
    std::cout << "Case #" << (i + 1) << ": ";
    calc();
    std::cout << std::endl;
  }
}

#include <vector>
#include <list>
#include <map>
#include <algorithm>
#include <iostream>
#include <math.h>

struct ship_t {
  int x, y, z, p;
};

void calc()
{
  // Find minimum power to reach any pair of receivers, and hope that
  // this is enough to cover all at once
  size_t n;
  std::cin >> n;
  std::vector<ship_t> ships;
  for (size_t i = 0; i < n; i++) {
    ship_t ship;
    std::cin >> ship.x >> ship.y >> ship.z >> ship.p;
    ships.push_back(ship);
  }

  double min_power = 0.0;

  for (size_t i = 0; i < n - 1; i++) {
    for (size_t j = i + 1; j < n; j++) {
      double dist = fabs(ships[i].x - ships[j].x)
        + fabs(ships[i].y - ships[j].y)
        + fabs(ships[i].z - ships[j].z);
      double power = dist / (ships[i].p + ships[j].p);
      if (power > min_power)
        min_power = power;
    }
  }

  std::cout << min_power;
}

int main()
{
  std::cout.precision(6);
  std::cout.setf ( std::ios::fixed, std::ios::floatfield );
  size_t count;
  std::cin >> count;
  for (size_t i = 0; i < count; i++) {
    std::cout << "Case #" << (i + 1) << ": ";
    calc();
    std::cout << std::endl;
  }
}

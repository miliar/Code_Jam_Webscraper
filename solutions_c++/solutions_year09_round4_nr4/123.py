#include <iostream>
#include <fstream>
#include <sstream>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cctype>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <functional>
#include <iterator>
#include <utility>

using namespace std;


struct Plant {
  double x, y, radius;
};

double sqr(const double arg) {
  return arg * arg;
}

double dist(const Plant first, const Plant second) {
  return sqrt(sqr(first.x - second.x) + sqr(first.y - second.y));
}

int main() {
  freopen("test.in", "r", stdin);
  freopen("test.out", "w", stdout);

  int test_cases;
  cin >> test_cases;
  for (int test = 1; test <= test_cases; ++test) {

    int number_of_plants;
    cin >> number_of_plants;
    vector<Plant> plants(number_of_plants);
    for (int i = 0; i < number_of_plants; ++i) {
      cin >> plants[i].x >> plants[i].y >> plants[i].radius;
    }

    double answer = 1e9;

    if (number_of_plants == 1) {
      answer = plants[0].radius;
    }
    if (number_of_plants == 2) {
      answer = max(plants[0].radius, plants[1].radius);
    }

    if (number_of_plants == 3) {
      for (int i = 0; i < number_of_plants; ++i) {
        for (int j = i + 1; j < number_of_plants; ++j) {
          int k = 3 - i - j;

          double d = dist(plants[i], plants[j]);
          double diameter = d + max(plants[i].radius, plants[j].radius - d) + max(plants[j].radius, plants[i].radius - d);
          answer = min(answer, max(diameter / 2, plants[k].radius));

        }
      }
    }

    printf("Case #%i: %.9lf\n", test, answer);
  }

  return 0;
}
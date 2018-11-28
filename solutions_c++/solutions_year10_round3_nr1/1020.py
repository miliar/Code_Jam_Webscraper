#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

class Point {
  private:
    int _x, _y;
  public:
    Point(int x, int y): _x(x), _y(y) {}
    bool operator==(Point &p) {
      return (_x > p._x && _y < p._y) || (_x < p._x && _y > p._y);
    }
};

int main(int argc, char **argv) {

  char *filename = argv[1];
  ifstream file(filename);

  int T, N, num_intersect, x, y;

  vector<Point> points;
  Point *p;

  file >> T;

  for (int t = 0; t < T; t++) {
    file >> N; // cout << N << endl;

    num_intersect = 0;
    points.clear();
    for (int n = 0; n < N; n++) {
      file >> x >> y;
      p = new Point(x,y);
      for (unsigned int i = 0; i < points.size(); i++) {
       if (points[i] == *p) num_intersect++;
      }
      points.push_back(*p);
    }

    cout << "Case #" << (t+1) << ": " << num_intersect << endl;

  }

  file.close();
}

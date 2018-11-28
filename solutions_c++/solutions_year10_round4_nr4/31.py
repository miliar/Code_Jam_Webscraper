#include <cmath>
#include <iomanip>
#include <iostream>
using namespace std;

double distance(double x1, double y1, double x2, double y2) {
  return hypot(x1 - x2, y1 - y2);
}

double area(double x0, double y0, double x1, double y1, double x, double y) {
  double r0 = distance(x0, y0, x, y);
  double r1 = distance(x1, y1, x, y);
  double c = distance(x0, y0, x1, y1);
  double cosCBA = (r1 * r1 + c * c - r0 * r0) / (2 * r1 * c);
  double CBD = 2 * acos(cosCBA);
  double cosCAB = (r0 * r0 + c * c - r1 * r1) / (2 * r0 * c);
  double CAD = 2 * acos(cosCAB);
  double area = 0.5 * CBD * r1 * r1 - 0.5 * r1 * r1 * sin(CBD)
              + 0.5 * CAD * r0 * r0 - 0.5 * r0 * r0 * sin(CAD);
  return area;
}

int main() {
  cout << fixed << setprecision(7);
  int T;
  cin >> T;
  for (int t = 1; t <= T; t++) {
    int N, M;
    cin >> N >> M;
    double x1, y1;
    double x2, y2;
    cin >> x1 >> y1;
    cin >> x2 >> y2;
    cout << "Case #" << t << ":";
    for (int i = 0; i < M; i++) {
      double x, y;
      cin >> x >> y;
      cout << " " << area(x1, y1, x2, y2, x, y);
    }
    cout << endl;
  }
}

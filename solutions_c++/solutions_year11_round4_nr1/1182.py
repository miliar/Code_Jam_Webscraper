#include <algorithm>
#include <iostream>
#include <fstream>
#include <map>
#include <string>
#include <vector>

using namespace std;

class Walkway {
public:
    Walkway(int b_, int e_, int w_):
        b(b_), e(e_), w(w_)
        {
        }
    int b;
    int e;
    int w;
};

class wcomp {
public:
    bool operator()(const Walkway w1, const Walkway w2){return (w1.w-w2.w)<0;}
};

int main(int argc, char* argv[]) {
  if(argc != 2) {
    cout << "please pass exactly one argument" << endl;
    exit(1);
  }
  ifstream input;
  input.open(argv[1]);
  int num_test_cases(0);
  input >> num_test_cases;
  for(int test(0); test != num_test_cases; ++test) {
      double x(0);
      double s(0);
      double r(0);
      double t(0);
      int n(0);
      input >> x >> s >> r >> t >> n;
      vector<Walkway> ws;
      int last_end(0);
      for(int i(0); i != n; ++i) {
          int temp1,temp2,temp3;
          input >> temp1 >> temp2 >> temp3;
          if(last_end != temp1){
              ws.push_back(Walkway(last_end, temp1, 0));
          }
          ws.push_back(Walkway(temp1, temp2, temp3));
          last_end = temp2;
      }
      if (last_end != x) {
          ws.push_back(Walkway(last_end, x, 0));
      }
      sort(ws.begin(), ws.end(), wcomp());
      double time(0);
      for(int i(0); i != ws.size(); ++i) {
          double w_length = ws[i].e - ws[i].b;
          double speed = r+ws[i].w;
          double slow_speed = s+ws[i].w;
          double run_length = min(t*speed, w_length);
          t -= run_length / speed;
          time += run_length / speed;
          time += (w_length - run_length) / slow_speed;
      }
      cout.precision(10);
      cout << "Case #" << test + 1 << ": " << time << endl;
  }
  input.close();
  return 0;
}

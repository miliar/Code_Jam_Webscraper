#include <vector>
#include <fstream>
#include <iostream>

struct snapper
{
  int num;
  bool on;
  bool powered;

  snapper(int n) : num(n), on(false), powered(false)
  {
  }

  bool is_on() const { return on; }
  bool is_powered() const { return powered; }

  void toggle() { on = !on; }
};

void run(int & count, std::ostream & os, int N, int K)
{
  std::vector<snapper> snappers;

  for(int n=1; n <= N; ++n) {
    snappers.push_back(snapper(n));
  }

  // give the first snapper power
  snappers.begin()->powered = true;

  for (int n, k=0; k < K; ++k) {
    for (n=0; n < snappers.size(); ++n) {
      if (snappers[n].is_powered())
        snappers[n].toggle();
    }

    for (n=0; n < snappers.size()-1; ++n) {
      snappers[n+1].powered = snappers[n].is_powered()
        && snappers[n].is_on();
    }
  }

  const snapper & last = snappers[snappers.size()-1];
  bool is_light_on = last.is_powered() && last.is_on();

  os<<"Case #"<<++count<<": "
    <<(is_light_on ? "ON" : "OFF")
    <<std::endl;
}

int main(int argc, char**argv)
{
  int count = 0;
  std::ifstream ifs(2<=argc ? argv[1] : "a.in");
  std::ofstream out(3<=argc ? argv[2] : "A.txt");
  if (ifs) {
    int r, n, k;
    if (!(ifs>>r && 0 < r)) {
      std::cerr<<"bad input"<<std::endl;
      return 0;
    }

    for (int i=0; i<r; ++i) {
      if (ifs>>n>>k) {
        run(count, out, n, k);
      }
      else {
        std::cerr<<"bad input at trial #"<<i+1<<std::endl;
        break;
      }
    }
  }
}


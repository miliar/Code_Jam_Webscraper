#include <iostream>
#include <string>
#include <fstream>
#include <iomanip>
using namespace std;


class CodeJam {
  private:
    string line;
    string golden;
    int index;
  public:
    CodeJam (string s) : line(s) { golden = "welcome to code jam"; index = 0; total = 0; }
     ~CodeJam () {}
    void compute (int);
    int total;
};

void CodeJam::compute (int from)
{
  if(index == 19) {
    ++total;
    return;
  }
  for(int i = from; i < line.size(); ++i) {
    size_t pos = line.find_first_of(golden[index], i);
    if(pos == string::npos)
      return;
    ++index;
    compute(pos+1);
     --index;
    i = pos;
  }
  return ;
}

int main(int argc, char **argv)
{
  if(argc != 2) {
    cout << "Error. Usage: a.out <testcase>" << endl;
    return -1;
  }

  ifstream f (argv[1], ifstream::in);

  int N;
  f >> N;


  for(int i = 0; i <= N; ++i) {
    string line;
    getline(f, line);
    if(i == 0)
      continue;
    CodeJam cj(line);
    cj.compute (0);
    cout << "Case #" << i << ": " << setw (4) << setfill('0') << cj.total << endl;
  }
}???
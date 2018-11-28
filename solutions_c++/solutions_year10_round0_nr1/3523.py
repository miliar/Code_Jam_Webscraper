#include<vector>
#include<iostream>
#include<fstream>

using namespace std;

class SnapperChain{
public:
};

int main(int argc, char** argv){
  ifstream ifs(argv[1]);
  ofstream ofs("snapper_output");
  int t;
  ifs >> t;

  for(int i=1;i<=t;++i){
    ofs << "Case #" << i << ": ";
    int n;
    long long k;
    ifs >> n;
    ifs >> k;

    if((k+1)%(1<<n) == 0)
      ofs << "ON";
    else
      ofs << "OFF";
    ofs << endl;
  }

  ifs.close();
  ofs.close();
  return 0;
}

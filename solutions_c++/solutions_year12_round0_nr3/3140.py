#include <fstream>
#include <string>
#include <sstream>
#include <vector>
#include <set>
#include <map>
#include <list>
#include <iostream>
#include <algorithm>
#include <cstdlib>
#include <cmath>
#include <cstring>

using namespace std;

int main(int argc, char* argv[]) {
  if (argc != 3) {
    std::cout << "Usage: <input_file> <output_file>\n";
    return -1;
  }
  ifstream ifs(argv[1]);
  ofstream ofs(argv[2]);
  string line;
  stringstream ss;
  int T = 0;

  // get inputs
  getline(ifs, line);
  ss << line;
  ss >> T;
  ss.clear();

  // run test cases
  for (int t=1;t<=T;t++) {
    getline(ifs, line);
    ss << line;
    long long Along = 0;
    long long Blong = 0;
    ss >> Along;
    ss >> Blong;
    ss.clear();
    long long count = 0;
    set<pair<string, string> > distinct;
    for (long long nlong=Along; nlong<=Blong; nlong++) {
      string nstr;
      ss << nlong;
      ss >> nstr;
      ss.clear();
      int ndigits = nstr.length();
      for (int i=1;i<ndigits;i++) {
        string mstr;
        int j = ndigits - i;
        mstr.assign(nstr, i, j);
        string some;
        some.assign(nstr, 0, i);
        mstr += some; 
        int lzeros = 0;
        for (lzeros=0;lzeros<mstr.length();lzeros++) {
          if (mstr[lzeros] != '0')
            break;
        }
        int mdigits = mstr.length() - lzeros;
        if (mdigits != ndigits)
          continue;
        long long mlong = 0;
        ss << mstr;
        ss >> mlong;
        ss.clear();
        if (Along <= nlong &&
            nlong < mlong &&
            mlong <= Blong) {
          pair<string, string> nmpair = make_pair(nstr, mstr);
          if (distinct.find(nmpair) == distinct.end()) {
            count++;
            distinct.insert(nmpair);
          }
        }
      }
    }
    distinct.clear();
    ofs << "Case #" << t << ": ";
    cout << "Case #" << t << ": ";
    ofs << count;
    cout << count;
    ofs << std::endl;
    cout << std::endl;
  }

  ifs.close();
  ofs.close();
  return 0;
}

#include <fstream>
#include <sstream>
#include <algorithm>
#include <vector>
#include <iomanip>

using namespace std;

ifstream fin("C-large.in");
ofstream fout("file.out");

string pattern = "welcome to code jam";

int main() {
  int N = 0;
  fin >> N;
  string tmp;
  getline(fin, tmp);
  //
  for(int n = 0; n < N; n++) {
    string str;
    getline(fin, str);
    vector<int> matches;
    matches.resize(pattern.length(), 0);
    for(int i = 0; i < str.length(); i++) {
      for(int j = 0; j < matches.size(); j++) {
        matches[j] %= 1000000000;
        if(pattern[j] != str[i])
          continue;
        if(j == 0) {
          matches[j]++;
          continue;
        }
        matches[j] += matches[j-1];
      }
    }
    fout.fill('0');
    fout << "Case #" << n+1 << ": " << setw(4) << matches[matches.size()-1] % 10000 << endl;
  }
}

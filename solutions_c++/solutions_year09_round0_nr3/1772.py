#include <iostream>
#include <iomanip>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int found;
string jam = "welcome to code jam";

void search(const string& val, int jam_index, int val_index) {
  if (jam_index >= jam.length()) {
    ++found;
    // cerr << "Found! " << found << endl;
    return;
  }
  if (val_index >= val.length()) return;
  while (1) {
    char ch = jam[ jam_index ];
    // cerr << "ch = [" << ch << "], jam_index = " << jam_index << ", val_index = " << val_index << endl;
    val_index = val.find(ch, val_index);
    // cerr << "find: val_index = " << val_index << endl;
    if (val_index == string::npos) break;
    val_index++;
    search(val, jam_index + 1, val_index);
  }
}  

int main(int argc, char* argv[]) {
  ifstream is("data.in");
  
  int N;
  string line;
  is >> N;

  int n;
  for (n = 0; n < N;) {
    getline(is, line, '\n');
    if (line.empty()) continue;
    ++n;
    // cerr << "[" << line << "]" << endl;
    
    found = 0;
    search(line, 0, 0);
    cout << "Case #" << n << ": " << setw(4) << setfill('0') << (found % 10000) << endl;
  }
  
  if (n != N) {
    cerr << "n is wrong: " << n << endl;
    return 1;
  }

	return 0;
}


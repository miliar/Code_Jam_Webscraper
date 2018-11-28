
#include <fstream>
#include <iostream>
#include <vector>
#include <deque>
#include <string>
using namespace std;

string cur;
string inp;

deque<char> comb1;
deque<char> comb2;
deque<char> comb3;

deque<char> opp1;
deque<char> opp2;

void Go2(int num) {
  if (!cur.empty()) {
    for (int idx = 0; idx < comb1.size(); ++idx) {
      if ((comb1[idx] == cur[cur.size() - 1] && comb2[idx] == inp[num]) ||
	  (comb2[idx] == cur[cur.size() - 1] && comb1[idx] == inp[num])) {
	cur[cur.size() - 1] = comb3[idx];
	return;
      }
    }
  }

  for (int c = 0; c < cur.size(); ++c) {
    for (int idx = 0; idx < opp1.size(); ++idx) {
      if ((cur[c] == opp1[idx] && inp[num] == opp2[idx]) ||
	  (cur[c] == opp2[idx] && inp[num] == opp1[idx])) {
	cur.clear();
	return;
      }
    }
  }

  cur.push_back(inp[num]);
}

void Go() {
  for (int idx = 0; idx < inp.size(); ++idx) {
    Go2(idx);
  }
}

int main(int argc, char** argv) {
  ifstream fin("inp");
  ofstream fout("answer");

  int cases;
  fin >> cases;

  for (int idx = 0; idx < cases; ++idx) {
    int num;
    fin >> num;

    comb1.resize(num);
    comb2.resize(num);
    comb3.resize(num);
    for (int n = 0; n < num; ++n) {
      string str;
      fin >> str;
      comb1[n] = str[0];
      comb2[n] = str[1];
      comb3[n] = str[2];
    }

    fin >> num;
    opp1.resize(num);
    opp2.resize(num);
    for (int n = 0; n < num; ++n) {
      string str;
      fin >> str;
      opp1[n] = str[0];
      opp2[n] = str[1];
    }    

    fin >> num;
    fin >> inp;

    cur.clear();
    Go();

    fout << "Case #" << (idx + 1) << ": [";
    for (int n = 0; n < cur.size(); ++n) {
      if (n > 0) {
	fout << ", ";
      }
      fout << cur[n];
    }
    fout << "]" << endl;
  }
  
  return 0;
}

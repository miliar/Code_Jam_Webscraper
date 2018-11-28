
#include <fstream>
#include <iostream>
#include <vector>
#include <deque>
using namespace std;

deque<bool> color;
deque<int> spot;
deque<int> orange;
deque<int> blue;

int Go(int oidx, int opos, int bidx, int bpos, int btn, int step) {
  //cout << oidx << ' ' << opos << ' ' << bidx << ' ' << bpos << ' ' << btn << ' ' << step << endl;

  if (btn >= spot.size()) {
    return step;
  }

  bool inc_button = false;

  if (oidx < orange.size()) {
    if (opos > orange[oidx]) {
      --opos;
    } else if (opos < orange[oidx]) {
      ++opos;
    } else if (color[btn]) {
      // push button
      inc_button = true;
      ++oidx;
    } else {
      // wait
    }
  } else {
    // do nothing
  }

  if (bidx < blue.size()) {
    if (bpos > blue[bidx]) {
      --bpos;
    } else if (bpos < blue[bidx]) {
      ++bpos;
    } else if (!color[btn]) {
      // push button
      inc_button = true;
      ++bidx;
    } else {
      // wait
    }
  } else {
    // do nothing
  }

  if (inc_button) {
    ++btn;
  }

  return Go(oidx, opos, bidx, bpos, btn, step + 1);
}

int main(int argc, char** argv) {
  ifstream fin("inp");
  ofstream fout("answer");

  int cases;
  fin >> cases;

  for (int idx = 0; idx < cases; ++idx) {
    int num;
    fin >> num;

    color.resize(num);
    spot.resize(num);
    orange.clear();
    blue.clear();

    for (int n = 0; n < num; ++n) {
      char c;
      fin >> c;
      color[n] = (c == 'O');

      int val;
      fin >> val;
      spot[n] = val;

      if (color[n]) {
	orange.push_back(val);
      } else {
	blue.push_back(val);
      }
    }

    int res = Go(0, 1, 0, 1, 0, 0);
    fout << "Case #" << (idx + 1) << ": " << res << endl;
  }
  
  return 0;
}

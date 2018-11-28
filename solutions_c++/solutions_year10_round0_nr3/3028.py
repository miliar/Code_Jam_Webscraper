#include <string>
#include <vector>
#include <set>
#include <map>
#include <iostream>
#include <fstream>
#include <cmath>

using namespace std;

#define  DEBUG

int main() {

  ifstream inf("C-small-attempt1.in");
  // save input buffer of the stream
  streambuf* cin_buffer = cin.rdbuf();
  cin.rdbuf(inf.rdbuf());

  ofstream outf("C-small-attempt1.out");
  // save output buffer of the stream
  streambuf* cout_buffer = cout.rdbuf();
  cout.rdbuf(outf.rdbuf());

  int number_of_cases = 0;
  cin >> number_of_cases;
  int cases = 1;
  while (cases <= number_of_cases) {
    int run_times_r, capacity_k, number_of_groups_n;
    cin >> run_times_r >> capacity_k >> number_of_groups_n;
    vector<int> groups(number_of_groups_n);
    for (int i = 0; i < number_of_groups_n; ++i) {
      int tg;
      cin >> tg;
      groups[i] = tg;
    }
    int current_position = 0;
    long euros = 0;
    for (int i = 0; i < run_times_r; ++i) {
      int euros_this_time = 0;
      int first_position = current_position;
      while (capacity_k - euros_this_time >= groups[current_position]) {
	euros_this_time += groups[current_position];
	current_position++;
	if (current_position == number_of_groups_n) {
	  current_position = 0;
	}
	if (first_position == current_position)
	  break;
      } // while
      euros += euros_this_time;
    }
    cout << "Case #" << cases << ": " << euros << endl;
    ++cases;
  }
  
  cin.rdbuf(cin_buffer);
  cout.rdbuf(cout_buffer);
  return 0;
}

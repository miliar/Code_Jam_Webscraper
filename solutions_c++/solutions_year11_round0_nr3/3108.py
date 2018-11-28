#include <algorithm>
#include <cmath>
#include <iostream>
#include <fstream>
#include <map>
#include <string>
#include <vector>

using namespace std;


int int_pow(int x, int p)
{
  if (p == 0) return 1;
  if (p == 1) return x;

  int tmp = int_pow(x, p/2);
  if (p%2 == 0) return tmp * tmp;
  else return x * tmp * tmp;
}

int simple_add(const vector<int>& values) {
  int result(0);
  for(int digit(0); digit != 20; ++digit) {
    int count(0);
    int power = int_pow(2,digit);
    for(int i(0); i != values.size(); ++i) {
      count += (power & values[i]) != 0 ? 1 : 0;
    }
    if(count%2 != 0)
      result += int_pow(2,digit);
  }
  return result;
}

int correct_add(const vector<int>& values) {
  int result(0);
  for(int i(0); i != values.size(); ++i) {
    result += values[i];
  }
  return result;
}

int main(int argc, char* argv[]) {
  if(argc != 2) {
    cout << "please pass exactly one argument" << endl;
    exit(1);
  }
  ifstream input;
  input.open(argv[1]);
  int t(0);
  input >> t;
  for(int i(0); i != t; ++i) {
    cout << "Case #" << i+1 << ": ";
    int n;
    input >> n;
    vector<int> values;
    for(int j(0); j != n; ++j) {
      int temp_int;
      input >> temp_int;
      values.push_back(temp_int);
    }
    int max_val(-1);
    for(int j(1); j < int_pow(2,n) - 1; ++j) {
      vector<int> sample1;
      vector<int> sample2;
      for(int k(0); k != n; ++k) {
	if((int_pow(2,k) & j) != 0) {
	  sample1.push_back(values[k]);
	} else {
	  sample2.push_back(values[k]);
	}
      }
      int sample1_val = simple_add(sample1);
      int sample2_val = simple_add(sample2);
      int sample1_real_val = correct_add(sample1);
      if(sample1_val == sample2_val && sample1_real_val > max_val) {
	max_val = sample1_real_val;
      }
    }
    if(max_val != -1) {
      cout << max_val << endl;
    } else {
      cout << "NO" << endl;
    }
  }
  input.close();
  return 0;
}

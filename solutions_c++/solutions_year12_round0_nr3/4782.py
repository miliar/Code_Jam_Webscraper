#include <iostream>
#include <fstream>
#include <string>
#include <cstdlib>
#include <stdio.h>
#include <algorithm>
#include <vector>

using namespace std;

void shift_one_digit(string& number);

int main(int argc, char *argv[])
{
  fstream input_stream, output_stream;

  input_stream.open(argv[1], fstream::in);
  output_stream.open(argv[2], fstream::out);

  int numOfTests = 0;
  input_stream >> numOfTests;

  string left_limit, right_limit, current_number, temp;
  char buf[10];
  int count = 0;
  vector<int> generated_integers;
  for (int i = 1; i <= numOfTests; ++i) {
    input_stream >> left_limit >> right_limit;
    count = 0;

    for (int j = atoi(left_limit.c_str()); j <= atoi(right_limit.c_str()); ++j) {
      sprintf(buf, "%d", j);
      current_number = buf;

      temp = current_number;
      generated_integers.clear();
      generated_integers.reserve(temp.length());
      generated_integers.push_back(atoi(temp.c_str()));
      for (int k = 0; k < current_number.length(); ++k) {
        shift_one_digit(temp);

        vector<int>::iterator it = find(generated_integers.begin(), generated_integers.end(), atoi(temp.c_str()));

        if (it != generated_integers.end()) continue;

        generated_integers.push_back(atoi(temp.c_str()));
        
        if (atoi(temp.c_str()) > atoi(current_number.c_str()) && atoi(temp.c_str()) <= atoi(right_limit.c_str()) ) {
          count = count + 1;
        }
      } // k
    } // j
    
    output_stream << "Case #" << i << ": " << count << endl;

  } // i

  input_stream.close();
  output_stream.close();
  
  return 0;
}

void shift_one_digit(string& number)
{
  if (number.length() < 2) {
    return;
  }

  char last_char = *(number.end() - 1);
  for (string::iterator it = number.end() - 1; it != number.begin(); --it) {
    *it = *(it - 1);
  }

  *number.begin() = last_char;
}

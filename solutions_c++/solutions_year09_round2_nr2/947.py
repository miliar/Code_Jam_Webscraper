#include <iostream>
#include <string>
#include <stdlib.h>
#include <stdio.h>
#include <sstream>

using namespace std;

int main ()
{
  int N;
  string in;
  cin >> in;
  N = atoi (in.c_str());
  for (int i = 0; i < N; ++i) {
    string number;
    int numbers[10];
		numbers[0] = 50;
    for (int k = 1; k < 10; ++k) {
      numbers[k] = 0;
    }
    cin >> number;
		number = "00000" + number;
		int index = 0;
		int count = 0;
		int last = 0;
    for (int j = number.length()-1; j >= 0; --j) {
			string str = number.substr (j,1);
      int act = atoi (str.c_str ());
      for (int k = act+1; k < 10; ++k) {
				if (numbers[k] == 0)
					continue;
				index = k;
				break;
			}
			if (act != 0) {
				++numbers[act];
				++count;
			}
			if (index != 0) {
				string h;
				stringstream out;
				out << index;
				h = out.str();
				number[j] = h[0];
				--numbers[index];
				--count;
				last = j;
				break;
			}
    }
		for (int j = last+1; j < number.length (); ++j) {
			if (number.length () - j > count) {
				number[j] = '0';
				continue;
			}
			for (int k = 1; k < 10; ++k) {
				if (numbers[k] == 0)
					continue;
				--count;
				--numbers[k];
				string h;
				stringstream out;
				out << k;
				h = out.str();
				number[j] = h[0];
				break;
			}
		}
		for (int k = 0; k < 10; ++k) {
			if (number[k] != '0')
				break;
			number = number.substr(1);
			--k;
		}
    cout << "Case #" << i+1 << ": " << number << endl;
  }
}


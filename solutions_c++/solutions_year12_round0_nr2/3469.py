#include <vector>
#include <iostream>
#include <stdlib.h>
#include <algorithm>
#include <string>
#include <assert.h>
#include <map>

using namespace std;

struct Data {
  vector<int> sums;
  int surprise;
  int max;
};

int GetBestCount(Data& data) {
  int result = 0;

  int best = data.max;
  for (int i = 0; i < data.sums.size(); i++) {
    int sum = data.sums[i];
    switch(sum % 3) {
      case 0:
        if(sum / 3 >= best) {
          result++;
        } else if(sum / 3 + 1 >= best && data.surprise > 0 && sum / 3 - 1 >= 0) {
          result++;
          data.surprise--;
        }
        break;
      case 1:
        if (sum / 3 + 1 >= best) result++;
        break;
      case 2:
        if (sum / 3 + 1 >= best) 
          result++;
        else if (sum / 3 + 2 >= best && data.surprise > 0) {
          result++;
          data.surprise--;
        }
        break;
    }
  }
  return result;
}

void Input(vector< Data >& data) {
  int countOfCases;
  cin >> countOfCases;
  data.resize(countOfCases);

  string s;
  getline(cin, s);

  for (int i = 0; i < countOfCases; i++) {
    int count;
    cin >> count;

    Data& d = data[i];
    d.sums.resize(count);

    cin >> d.surprise;
    cin >> d.max;

    for (int j = 0; j < count; j++) {
      cin >> d.sums[j];
    }

    getline(cin, s);
  }
}

int main() {
  vector<Data> data;
  Input(data);

  for (int i = 0; i < data.size(); i++) {
    cout << "Case #" << i + 1 << ": " << GetBestCount(data[i]) << endl;
  }
  return 0;
}
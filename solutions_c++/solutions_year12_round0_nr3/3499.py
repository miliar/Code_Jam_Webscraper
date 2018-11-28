#include <vector>
#include <iostream>
#include <stdlib.h>
#include <algorithm>
#include <string>
#include <assert.h>
#include <map>

using namespace std;

const int READY = -1;

int MatchingParts(const string& inputString, int position, int positionInBegin) {
    
  int fixPositionInBegin = positionInBegin;  

  while (position < inputString.length()) {
    if (inputString[position] == inputString[positionInBegin]) {
      position++;
      positionInBegin++;
    }
    else {
      break;
    }
  }

  return positionInBegin - fixPositionInBegin;
}


void CalculateZFunction(const string& inputString, vector<int> &zFunctionVector) {

  if (inputString.length() == 0)
    return;

  zFunctionVector.resize(inputString.length());
  zFunctionVector[0] = inputString.length();
  int leftIndex = 0;
  int rightIndex = 0;

  int zFunctionValue;

  for (int position = 1; position < inputString.length(); ++position) {

    if (position > rightIndex) {
      zFunctionValue = MatchingParts(inputString, position, 0);
      if (zFunctionValue > 0) {
        leftIndex = position;
        rightIndex = position + zFunctionValue - 1;
      }
    }
    else {
      if (zFunctionVector[position - leftIndex] < rightIndex - position + 1) {
        zFunctionValue = zFunctionVector[position - leftIndex];
      }
      else {
        int newMatching = MatchingParts(inputString, rightIndex + 1, rightIndex - position + 1);
        
        leftIndex = position;
        rightIndex += newMatching;
        
        zFunctionValue = rightIndex - position + 1;  
      }
    }

    zFunctionVector[position] = zFunctionValue;
  }
}

struct Data {
   int first;
   int second;
};

vector<string> GetPermut(string str) {
  vector<string> res;

  vector<int> zFunctionVector;
  CalculateZFunction(str, zFunctionVector);

  int period = str.length();
  for(int i = 1; i < str.length(); i++) {
    if (str.length() % i == 0 && zFunctionVector[i] == str.length() - 1 && zFunctionVector[i] >= i) {
      period = i;
      break;
    }
  }

  for(int i = 0; i < period; i++) {
    string resStr = str;
    for(int j = 0; j < str.length(); j++) {
      resStr[j] = str[(j + i) % str.length()];
    }
    res.push_back(resStr);
  }

  return res;
}

vector<int> buildAllVariants(int sourceNumber, int min, int max, vector<int>& numbers) {
  vector<int> variants;
  if(sourceNumber == READY) return variants;

  char buffer[50];
  sprintf(buffer,"%d",sourceNumber);
  vector<string> cur = GetPermut(string(buffer));
  for( int i = 0; i < cur.size(); i++) {
    if(cur[i][0] == '0') continue;
    int number;
    sscanf(cur[i].c_str(), "%d", &number);
    if(number < min || number > max) continue;
    if(number > sourceNumber) {
      assert( numbers[number - min] == READY || numbers[number - min] == number);
      numbers[number - min] = READY;
    }
    variants.push_back(number);
  }
  std::sort(variants.begin(), variants.end());
  variants.erase(std::unique(variants.begin(), variants.end()), variants.end());
  return variants;
}




int GetCount(int min, int max) {
  int pairsCount = 0;
  vector<int> numbers;
  numbers.resize(max - min + 1);
  for(int i = 0; i < numbers.size(); i++) {
    numbers[i] = i + min;
  }

  for(int i = 0; i < numbers.size(); i++) {
    if(numbers[i] == READY) {
      continue;
    } else {
      vector<int> variants = buildAllVariants(numbers[i], min, max, numbers);
      if (variants.size() <= 1) {
        continue;
      }
      
        int k = variants.size();
        pairsCount += k * (k - 1) / 2;
    }
  }

  return pairsCount;
}

int main() {

  int cases;
  cin >> cases;
  string s;
  getline(cin, s);

  vector<Data> data(cases);

  for(int i = 0; i < cases; i++) {
    cin >> data[i].first;
    cin >> data[i].second;
    getline(cin, s);
    cout << "Case #" << i + 1 << ": " << GetCount(data[i].first, data[i].second) << endl;
  }

  return 0;
}

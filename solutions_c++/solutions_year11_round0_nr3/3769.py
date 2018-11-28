#include <iostream>
#include <string>
#include <sstream>
#include <vector> 


using std::cin;
using std::cout;
using std::endl;

using std::string;
using std::vector;


unsigned int Minimum(const vector<unsigned int> &values) {
  unsigned int min = values[0];
  for (int i = 1; i < values.size(); ++i) {
    if (values[i] < min) {
      min = values[i];
    }
  }
  return min;
}


unsigned int Sum(const vector<unsigned int> &values) {
  unsigned int sum = 0;
  for (int i = 0; i < values.size(); ++i) {
    sum += values[i];
  }
  return sum;
}


unsigned int Xor(const vector<unsigned int> &values) {
  unsigned int xor = 0;
  for (int i = 0; i < values.size(); ++i) {
    xor ^= values[i];
  }
  return xor;
}


unsigned int GetMaxSum(const vector<unsigned int> &values) {

  unsigned int xor = Xor(values);
  if (xor != 0) {
    return 0;
  }

  unsigned int sum = Sum(values);
  unsigned int min = Minimum(values);
  unsigned int result = sum - min;
  return result;
}



void Parse(const string &parameters, vector<unsigned int> &candyNumbers) {
  std::istringstream stream(parameters);

  for (int i = 0; i < candyNumbers.size(); ++i) {
    unsigned int candyNumber;
    stream >> candyNumber;
    candyNumbers[i] = candyNumber;
  }  
}


int main() {
  string parameters;
  std::getline(cin, parameters);
  
  int numberOfCases;
  std::istringstream stream(parameters);
  stream >> numberOfCases;

  for (int caseNum = 0; caseNum < numberOfCases; ++caseNum) { 
    std::getline(cin, parameters);

    int candyCount;
    stream = std::istringstream(parameters);
    stream >> candyCount;

    vector<unsigned int> candyNumbers(candyCount);
    std::getline(cin, parameters);
    Parse(parameters, candyNumbers);

    unsigned int resultSum = GetMaxSum(candyNumbers);

    cout << "Case #" << caseNum + 1 << ": ";

    if (resultSum == 0) {
      cout << "NO";
    }
    else {
      cout << resultSum;
    }
    cout << endl;
  }

  return 0;
}
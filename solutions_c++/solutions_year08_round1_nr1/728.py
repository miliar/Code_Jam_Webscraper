#include <algorithm>
#include <functional>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

void MinimumScalarProduct(int caseNumber)
{
  int vectorLength; cin >> vectorLength;

  std::vector<int> vectorX;
  for(int i=0; i < vectorLength; ++i)
  {
    vectorX.push_back(0);
    cin >> vectorX.back();
  }
  std::sort(vectorX.begin(),vectorX.end(),std::less<int>());

  std::vector<int> vectorY;
  for(int i=0; i < vectorLength; ++i)
  {
    vectorY.push_back(0);
    cin >> vectorY.back();
  }
  std::sort(vectorY.begin(),vectorY.end(),std::greater<int>());

  int result = 0;
  for(int i=0; i < vectorLength; ++i)
  {
    result += (vectorX[i]*vectorY[i]);
  }

  std::cout << "Case #" << caseNumber << ": " << result << std::endl;
}

int main()
{
  int cases; cin >> cases;
  for(int caseIndex = 1; caseIndex <= cases; ++caseIndex)
  {
    MinimumScalarProduct(caseIndex);
  }
}
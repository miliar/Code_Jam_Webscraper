#include <iostream>
#include <string>
#include <queue>
using namespace std;

int main()
{
  
  int iTestCases=0;
  cin >> iTestCases;
  for(int indexTestCase = 1;indexTestCase <= iTestCases; indexTestCase++ )
    {
      queue<int> qCoster;
  int size =0;
  int p = 0;;
  int iReqAttempts =0, iCapacity =0,iCostPerRidePerPerson =1;
  
  cin >> iReqAttempts;
  cin >> iCapacity;
  cin >> size;
  //cin >> iCostPerRidePerPerson;
  for(int i = 0; i< size;i++)
    {
      cin >> p;
      qCoster.push(p);
    }
  if(qCoster.empty())
    {
      //cout << 0 << "\n";
      cout << "Case #" << indexTestCase << ": " << 0;
      continue;
    }
  int totalMoney = 0;
  int totalAttempts =0;
  
  while(totalAttempts < iReqAttempts)
    {
      int iCurrentCapacity =0;
      int CurrentGroupSize = qCoster.front();
      int inCurrentGroups = 0;
      while(CurrentGroupSize + iCurrentCapacity <= iCapacity && inCurrentGroups < size)
	{
	  iCurrentCapacity += CurrentGroupSize;
	  qCoster.push(CurrentGroupSize);
	  qCoster.pop();
   	  CurrentGroupSize = qCoster.front();
	  inCurrentGroups++;
	}
      totalAttempts++;
      totalMoney += iCurrentCapacity * iCostPerRidePerPerson; 
    }
  cout << "Case #" << indexTestCase << ": " << totalMoney << "\n";
    }
  return 0;
}

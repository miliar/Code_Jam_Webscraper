#include "CodeJamIO.h"

CodeJamIO codeJamIO ("C-large");

void solve (vector< long long int >& caseItem);

int main ()
{
  vector< vector< long long int > > caseList = codeJamIO.read_case ();

  for (int i = 0; i < caseList.size (); ++i)
    solve (caseList[i]);

  return 0;
}


void solve (vector< long long int >& caseItem)
{
  long long int K = caseItem[caseItem.size () - 1];
  caseItem.pop_back ();
  long long int R = caseItem[caseItem.size () - 1];
  caseItem.pop_back ();

  vector< vector< long long int > > firstGroupNextRoundList;
  vector< vector< long long int > > numberOfRiderList;

  vector< long long int > firstGroupNextRound (caseItem.size ());
  vector< long long int > numberOfRider (caseItem.size ());
  
  long long int curGroup = 0;
  long long int curAmount;
  for (int startGroup = 0; startGroup < caseItem.size (); ++startGroup)
  {
    if (startGroup == 0)
      curAmount = 0;
    else
      curAmount -= caseItem[startGroup - 1];
    curAmount += caseItem[curGroup];
    while (curAmount <= K)
    {
      curGroup = (curGroup + 1) % caseItem.size ();
      curAmount += caseItem[curGroup];
      if (curGroup == startGroup)
        break;
    } 
    numberOfRider[startGroup] = curAmount = curAmount - caseItem[curGroup];
    firstGroupNextRound[startGroup] = curGroup;
  }

  firstGroupNextRoundList.push_back (firstGroupNextRound);
  numberOfRiderList.push_back (numberOfRider);

  
  for (int i = R / 2; i > 0; i /= 2)
  {
    for (int startGroup = 0; startGroup < caseItem.size (); ++startGroup)
    {
      firstGroupNextRound[startGroup] = firstGroupNextRoundList[firstGroupNextRoundList.size () - 1][firstGroupNextRoundList[firstGroupNextRoundList.size () - 1][startGroup]];
      numberOfRider[startGroup] += numberOfRiderList[firstGroupNextRoundList.size () - 1][firstGroupNextRoundList[firstGroupNextRoundList.size () - 1][startGroup]];
    }
    firstGroupNextRoundList.push_back (firstGroupNextRound);
    numberOfRiderList.push_back (numberOfRider);
  }

  long long int sum = 0;
  curGroup = 0;

  for (int i = R, j = 0; i > 0; i /= 2, ++j)
  {
    if (i % 2 != 0)
    {
      sum += numberOfRiderList[j][curGroup];
      curGroup = firstGroupNextRoundList[j][curGroup];
    }
  }

  codeJamIO.write_result (sum);

}


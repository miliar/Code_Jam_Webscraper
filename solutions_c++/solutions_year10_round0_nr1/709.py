#include "CodeJamIO.h"

#define SNAPPER_NUM 0
#define SNAP_TIMES 1

CodeJamIO codeJamIO ("A-large");

void solve (const vector< int >& caseItem);

int main ()
{
  vector< vector< int > > caseList = codeJamIO.read_case (2);

  for (int i = 0; i < caseList.size (); ++i)
    solve (caseList[i]);

  return 0;
}

void solve (const vector< int >& caseItem)
{

  int snapperNum = caseItem[SNAPPER_NUM];
  int timesOfSnap = caseItem[SNAP_TIMES] + 1;

  for (int i = 0; i < snapperNum; ++i)
  {
    if (timesOfSnap % 2 != 0)
    {
      codeJamIO.write_result ("OFF");
      return;
    }
    timesOfSnap /= 2;
  }

  codeJamIO.write_result ("ON");

}
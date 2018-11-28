#include <iostream>
#include <cstring>
#include <vector>

using namespace std;

int memo[101][1002];
int numEng, numStep;
vector<string> engines, steps;

int doit(int curEng, int step)
{
  if (step >= numStep) return 0;

  int& retVal = memo[curEng][step];
  if(retVal != -1) return retVal;
  retVal = 999999999;
  if(engines[curEng] == steps[step]) return retVal = 1000000000;

  for(int i = 0; i < numEng; i++)
    {
      retVal = min(doit(i, step + 1) + (i != curEng), retVal);
    }
  return retVal;
}

int main()
{
  int N;
  cin >> N;
  for(int z = 0; z < N; z++)
    {
      memset(memo, -1, sizeof memo);
      cin >> numEng;

      engines.clear(); steps.clear();
      cin.ignore();

      for(int i = 0; i < numEng; i++)
	{
	  string s; getline(cin, s);
	  engines.push_back(s);
	  }

      cin >> numStep;
      cin.ignore();

      for(int i = 0; i < numStep; i++)
	{
	  string s; getline(cin, s);
	  steps.push_back(s);
	  }

      int retVal = 999999999;
      for(int i = 0; i < numEng; i++)
	retVal = min(retVal, doit(i, 0));

      cout << "Case #" << z + 1 << ": " << retVal << endl;
    } 
}

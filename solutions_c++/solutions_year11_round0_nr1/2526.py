#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <vector>

using namespace std;

const int inf = 1<<30;

inline void Solve(int TestNumber)
{
  int n = 0;
  int ans = 0;
  vector< pair<int, int> > posl;
  vector<int> Orange;
  vector<int> Blue;
  
  scanf("%d", &n);
  for (int i=0; i<n; i++)
  {
    char c;
    int pos;
    
    scanf(" %c %d", &c, &pos);
    pos--;
    
    if (c == 'O')
    {
      posl.push_back(make_pair(0, pos));
      Orange.push_back(pos);
    }
    else if (c == 'B')
    {
      posl.push_back(make_pair(1, pos));
      Blue.push_back(pos);
    }
  }

  int pO = 0;
  int posO = 0;
  int posB = 0;
  int pB = 0;
  
  for (int i=0; i<n; i++)
  {
    int distO = inf;
    int distB = inf;
    
    if (pO < Orange.size())
      distO = Orange[pO] - posO;
    
    if (pB < Blue.size())
      distB = Blue[pB] - posB;
    
    if (posl[i].first == 0)
    {
      ans += abs(distO) + 1;
      pO++;
      posO = posl[i].second;
      
      if (distB != inf)
      {
	if (abs(distB) <= abs(distO) + 1)
	{
	  posB = posB + distB;
	}
	else
	{
	  int willgo = abs(distO) + 1;
	  if (distB < 0)
	    willgo *= -1;
	  
	  posB = posB + willgo;
	}
      }
    }
    else
    {
      ans += abs(distB) + 1;
      pB++;
      posB = posl[i].second;
      
      if (distO != inf)
      {
	if (abs(distO) <= abs(distB) + 1)
	{
	  posO = posO + distO;
	}
	else
	{
	  int willgo = abs(distB) + 1;
	  if (distO < 0)
	    willgo *= -1;
	  
	  posO = posO + willgo;
	}
      }
    }
  }
  
  printf("Case #%d: %d\n", TestNumber+1, ans);
}

int NumOfTests;
int main()
{
  freopen("input.txt","r", stdin);
  freopen("output.txt","w", stdout);
  
  scanf("%d\n", &NumOfTests);
  
  for (int i=0; i < NumOfTests; i++)
    Solve(i);
}
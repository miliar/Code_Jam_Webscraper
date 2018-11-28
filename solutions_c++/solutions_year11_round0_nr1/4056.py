#include <iostream>
#include <vector>
#include <string>
#include <cstdlib>
#include <cstdio>

using namespace std;

int main()
{
  int count;
  cin >> count;

  for (int i = 0; i < count; ++i)
  {
    int steps;
    cin >> steps;
    vector<int> blue;
    vector<int> orange;
    vector<int> order;

    for (int j = 0; j < steps; ++j)
    {
      int num;
      char ch;
      int pos;
      cin >> ch >> pos;

      if (ch == 'O')
      {
	orange.push_back(pos);
	order.push_back(0);
      }
      else
      {
	blue.push_back(pos);
	order.push_back(1);
      }
    }


    vector<int>::iterator it = order.begin();
    vector<int>::iterator blueIt = blue.begin();
    vector<int>::iterator orIt = orange.begin();

    int o = 1, b = 1;
    int time = 0;

    for (; it != order.end(); ++it)
    {
      int moveB = (!blue.empty() && blueIt <= blue.end()) ? abs(*blueIt - b) : (1 << 10);
      int moveO = (!orange.empty() && orIt <= orange.end()) ? abs(*orIt - o) : (1 << 10);

      if (*it) // blue
      {
	if (moveO > moveB)
	{
	  if ((1 << 10) != moveO)
	  {
	    if ((*orIt - o) == moveO)
	      o += (moveB + 1);
	    else
	      o -= (moveB + 1);
	  }
	}
	else
	{
	  o = *orIt;
	}

	time += (moveB + 1);
	b = *blueIt;
	++blueIt;

      }
      else // orange
      {
	if (moveB > moveO)
	{
	  if ((1 << 10) != moveB)
	  {
	    if ((*blueIt - b) == moveB)
	      b += (moveO + 1);
	    else
	      b -= (moveO + 1);
	  }
	}
	else
	{
	  b = *blueIt;
	}

	time += (moveO + 1);
	o = *orIt;
	++orIt;

      }
    }
    cout << "Case #" << (i + 1) << ": " << time << endl; 
  }

  return 0;
}

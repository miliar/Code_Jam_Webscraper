#include <iostream>
#include <vector>

using namespace std;

int main()
{
  int t, n, s, p;
  vector<int> totals;
  cin >> t;
  for (int i = 0; i < t; i++)
    {
      int ns=0, sp=0;
      totals.clear();
      cin >> n;
      cin >> s;
      cin >> p;
      for (int j = 0; j < n; j++)
	{
	  int temp;
	  cin >> temp;
	  if (3*p - 2 <= temp && temp >= p)
	    {
	      ns++;
	    }
	  else if(3*p - 4 <= temp && temp >= p)
	    {
	      sp++;
	    }
	}

      cout << "Case #" << i+1 << ": ";
      //cout << "ns: " << ns << "sp: " << sp << endl;
      cout << ns + min(s, sp) << endl;


    }
}

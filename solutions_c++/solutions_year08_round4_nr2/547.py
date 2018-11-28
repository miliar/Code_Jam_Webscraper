#include <iostream>
#include <vector>

using namespace std;

int main()
{
  int c; 

  cin >> c;
  int cases = 1;
  while (c-- > 0)
    {
      int n,m,a;
      cin >> n >> m >> a;
      if (n*m < a)
	{
	cout << "Case #" << cases << ": " << "IMPOSSIBLE" << endl;
	cases++;
	continue;
	}

      vector<int> lst;
      bool found = false;

      for(int i = 0; i <= n; i++)
	{
	  for(int j = 0; j <= m; j++)
	    {
	      for(int p = 0; p <= n; p++)
		{
		  for(int q = 0; q <= m; q++)
		    {
		      int area = abs(i*q-p*j);
		      //		      cout << i << " " << j << " " << p << " " << q << " " << area << endl;
                      if (area == a)
			{
			
			  			  cout << "Case #" << cases <<": 0 0 " << i << " " << j << " " << p << " " << q  << endl;
                          found = true;
			  goto done;

			}
		    }
		}
	    }
	}

    done:
   int qq= 0;
    if (found == false)
	cout << "Case #" << cases << ": " << "IMPOSSIBLE" << endl;

      cases++;

    }
}

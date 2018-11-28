#include <iostream>

using namespace std;

int main()
{
  ios_base::sync_with_stdio(0);
  int t;
  cin >> t;
  for(int j = 1; j <= t; j++)
    {
      int n, s, p;
      int sum = 0;
      cin >> n >> s >> p;
      if(p>1)
	for(int i = 0; i < n; i++)
	  {
	    int tmp;
	    cin >> tmp;
	    if(tmp>=3*p-2)
	      sum++;
	    else if(tmp>=3*p-4 && tmp<=3*p-3 && s-->0)
	      sum++;
	  }
      else
	for(int i = 0; i < n; i++)
	  {
	    int tmp;
	    cin >> tmp;
	    if(tmp>=p)
	      sum++;
	  }
      cout << "Case #" << j << ": " << sum << endl;
    }
  return 0;
}

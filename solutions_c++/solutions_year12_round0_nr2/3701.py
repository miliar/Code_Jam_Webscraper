#include <iostream>
#include <algorithm>

using namespace std;

int scores[100];

int main()
{
  int N,T,S,p;

  cin >> T;

  for (int t=0; t<T; t++)
    {
      cin >> N >> S >> p;
      int good=0;
      int good_if_surprising=0;
      int score,sol;
      for (int i=0; i<N; i++)
	{
	  cin >> score;
	  if (score % 3 == 0)
	    {
	      if (score / 3 >= p)
		good++;
	      else if (score / 3 + 1 >= p && score / 3 - 1 >= 0)
		good_if_surprising++;
	    }
	  else if (score % 3 == 1)
	    {
	      if (score / 3 + 1 >= p)
		good++;
	    }
	  else
	    {
	      if (score / 3 + 1 >= p)
		good++;
	      else if (score / 3 + 2 >= p)
		good_if_surprising++;
	    }
	}
      
      sol = good + min(good_if_surprising, S);
      //3|x
      //a a a
      //a-1 a a+1

      //x = 3y+1
      //y y y+1
      //y-1 y+1 y+1

      //x = 3y+2
      //y y+1 y+1
      //y y y+2

      cout << "Case #" << t+1 << ": " << sol << endl;
    }

  return 0;
}

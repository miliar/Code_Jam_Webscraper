#include <iostream>
#include <vector>
#include <set>
#include <string>
#include <sstream>

using namespace std;

typedef pair<int, bool> Event; // (time, type - arr.(false)/dep.(true))

pair<int, int>
min_traits(vector<Event>& A2B, 
	   vector<Event>& B2A)
{
  // sort input by time.
  sort(A2B.begin(), A2B.end());
  sort(B2A.begin(), B2A.end());

  int A_trains = 0;
  int B_trains = 0;

  int curr_A = 0; // current number of trains ready to go from A.
  int curr_B = 0; // current number of trains ready to go from B.

  vector<Event>::iterator itA = A2B.begin();
  vector<Event>::iterator itB = B2A.begin();

  while (itA != A2B.end() || itB != B2A.end())
    {
      bool a_turn = true;
      if (itA == A2B.end())
	a_turn = false;
      else if (itB == B2A.end())
	a_turn = true;
      else
	{
	  a_turn = (*itA) < (*itB) ? true : false;
	}
      
      if (a_turn)
	{
	  if (itA->second == false)
	    {
	      // arrival (to B)
	      ++curr_B;
	    }
	  else
	    {
	      // departure (from A)
	      if (curr_A > 0)
		--curr_A;
	      else
		{
		  // there is no train in A.
		  ++A_trains;
		}
	    }
	  ++itA;
	}
      else
	{
	  // b's turn
	  if (itB->second == false)
	    {
	      // arrival (to A)
	      ++curr_A;
	    }
	  else
	    {
	      // departure (from B)
	      if (curr_B > 0)
		--curr_B;
	      else
		{
		  // there is no train in B.
		  ++B_trains;
		}
	    }
	  ++itB;
	}
    }

  return make_pair(A_trains, B_trains);
}

int read_time(string& time)
{
  string hour (time, 0, 2);
  string minute (time, 3, 2);
  
  stringstream sh(hour);
  stringstream sm(minute);
  
  int h; sh >> h;
  int m; sm >> m;

  return h*60 + m;
}

int main()
{
  int N;
  cin >> N;
  
  for (int i = 0; i < N; ++i)
    {
      vector<Event> A2B;
      vector<Event> B2A;
      
      int turnaround;
      cin >> turnaround;

      int NA, NB;
      cin >> NA >> NB;

      for (int j = 0; j < NA; ++j)
	{
	  string time;
	  cin >> time;
	  int dep = read_time(time);
	  cin >> time;
	  int arr = read_time(time);
	  A2B.push_back(make_pair(dep, true));
	  A2B.push_back(make_pair(arr + turnaround, false));
	}

      for (int j = 0; j < NB; ++j)
	{
	  string time;
	  cin >> time;
	  int dep = read_time(time);
	  cin >> time;
	  int arr = read_time(time);
	  B2A.push_back(make_pair(dep, true));
	  B2A.push_back(make_pair(arr + turnaround, false));
	}

      pair<int, int> result = min_traits(A2B, B2A);
      cout << "Case #" << i + 1 << ": " << result.first << " " << 
	result.second << endl;
    }
}

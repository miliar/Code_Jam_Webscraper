#include <iostream>
#include <cmath>
#include <string>
#include <sstream>
#include <cstdlib>
#include <queue>

using namespace std;

string snapper_chain(int, int);
int run_coaster(string, string, int, queue<int>);

#define PROBLEM_1
#define PROBLEM_2
//#define PROBLEM_3

int main()
{
#ifdef PROBLEM_1
  int T, N, K, T_count = 1;
  cin >> T;
  while (T > 0)
  {
    cin >> N >> K;
    cout << "Case #" << T_count << ": " << snapper_chain(N, K) << endl;

    T_count++;
    T--;
  }
#endif

#ifdef PROBLEM_3
  int answer, case_num = 1;
  stringstream ss;
  string T, R, k, N, g;
  queue<int> passengers;

  // get input
  getline(cin,T,'\n');
  while (atoi(T.c_str()) > 0)
  {
    getline(cin,R,' ');
    getline(cin,k,' ');
    getline(cin,N,'\n');

    while (atoi(N.c_str()) > 1)
    {
      getline(cin, g, ' ');
      passengers.push(atoi(g.c_str()));
      ss << atoi(N.c_str())-1;
      N = ss.str();
      ss.str("");
    }
    getline(cin, g);
    passengers.push(atoi(g.c_str()));

    answer = run_coaster(R, k, passengers.size(), passengers);
    cout << "Case #" << case_num << ": " << answer << endl;

    case_num++;

    while(!passengers.empty())
      passengers.pop();
    ss << atoi(T.c_str()) - 1;
    T = ss.str();
    ss.str("");
  }
#endif

  return 0;
}

string snapper_chain(int N, int K)
{
  int period = pow(2.0,N);
  if ( (K % period) == period - 1 )
    return "ON";
  
  return "OFF";
}

int run_coaster(string R, string k, int N, queue<int> passengers)
{
  bool ready = false;
  int euros = 0, max_cap = atoi(k.c_str()), cap = 0, temp_N = N;
  stringstream ss;
  while (atoi(R.c_str()) > 0)
  {
    while (!ready)
    {
      cap += passengers.front();
      if (temp_N <= 0)
      {
        ready = true;
        cap -= passengers.front();
      }
      else if (cap > max_cap)
      {
        cap -= passengers.front();
        ready = true;
      }
      else
      {
        euros += passengers.front();
        passengers.push(passengers.front());
        passengers.pop();
      }
      temp_N--;
    }

    temp_N = N;
    cap = 0;
    ready = false;
    ss << atoi(R.c_str()) - 1;
    R = ss.str();
    ss.str("");
  }
  return euros;
}
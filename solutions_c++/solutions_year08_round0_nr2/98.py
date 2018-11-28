
#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <map>

using namespace std;

int gettime()
{
  int h, m;
  char colon;
  cin >> h >> colon >> m;
  return h * 60 + m;
}

void ProcessSchedule(int num, int T, map<int, int> &from, map<int, int> &to)
{
  for (int i = 1; i <= num; ++i)
  {
    --from[gettime()];
    ++to[gettime() + T];
  }
}

int MinLevel(map<int, int> &schedule)
{
  int min_level = 0, level = 0;
  for (map<int, int>::iterator iter = schedule.begin(); iter != schedule.end(); ++iter)
  {
    level += iter->second;
    if (level < min_level)
      min_level = level;
  }
  return min_level;
}

int main()
{
  int N;
  cin >> N;
  for (int n = 1; n <= N; ++n)
  {
    int T, NA, NB;
    cin >> T;
    cin >> NA >> NB;

    map<int, int> A, B;
    ProcessSchedule(NA, T, A, B);
    ProcessSchedule(NB, T, B, A);

    cout << "Case #" << n << ": " << (-MinLevel(A)) << " " << (-MinLevel(B)) << endl;
  }

  return 0;
}


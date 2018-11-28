#include <cstdlib>
#include <cmath>
#include <iostream>

using namespace std;

struct Robot
{
  int time;
  int pos;
};

int main(int argc, char ** argv)
{
  int n, t = 0;
  cin >> t;
  int buffer;
  char bfr;

  //cout << "Going to read " << t << " lines." << endl;
  for(int i = 0; i < t; i++)
  {
    Robot orange = {0, 1}, blue = {0, 1};

    cin >> n;
    //cout << "Going to read " << n << " items." << endl;
    for(int j = 0; j < n; j++)
    {
      cin >> bfr >> buffer;
      if(bfr == 'O')
      {
        orange.time = (orange.time + abs(buffer - orange.pos) > blue.time ? orange.time + abs(buffer - orange.pos) : blue.time);
        orange.time++;
        orange.pos = buffer;
      }
      else
      {
        blue.time = blue.time + abs(buffer - blue.pos) > orange.time ? blue.time + abs(buffer - blue.pos) : orange.time;
        blue.time++;
        blue.pos = buffer;
      }
    }
    cout << "Case #" << i + 1 << ": " << (orange.time > blue.time ? orange.time : blue.time) << endl;
  }
  return EXIT_SUCCESS;
}

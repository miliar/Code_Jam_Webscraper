#include <iostream>

using namespace std;

int main(int argc, char* const* argv)
{
  int testsize;
  int p;
  int googlers;
  int surprises;
  int toohigh;
  int close;
  int score;
  int high_threshold;
  int low_threshold;
  int result;

  cin >> testsize;

  for(int i = 0; i < testsize; i++)
  {
    cin >> googlers; 
    cin >> surprises;
    cin >> p;
    high_threshold = 3*p - 2;
    if(p > 1)
      low_threshold = 3*p - 4;
    else
      low_threshold = high_threshold;
    toohigh = 0;
    close = 0;
    for(int j = 0; j < googlers; j++)
    {
      cin >> score;
      if(score >= high_threshold)
        toohigh++;
      else if(score >= low_threshold)
        close++;
    }

    if(close > surprises)
      result = toohigh + surprises;
    else
      result = toohigh + close;
    cout << "Case #" << i+1 << ": " << result << endl;
  }
  return 0;
}

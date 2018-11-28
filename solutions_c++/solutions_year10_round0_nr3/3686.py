#include <iostream>
#include <fstream>
#include <algorithm>
#include <queue>

using namespace std;

int main(int argc, char *argv[])
{
  unsigned int cases; // t
  unsigned int runs; // r
  unsigned int capacity; // k
  unsigned int groups; // n

  unsigned int bufInt;
  //unsigned int caseNum = 0;
  ifstream inputFile;
  inputFile.open(argv[1]);

  if (inputFile.is_open())
    {
      inputFile >> cases;
      for (unsigned int i = 0; i < cases; ++i)
	{
          inputFile >> runs;
          inputFile >> capacity;
          inputFile >> groups;
          unsigned int tempInt, money = 0;
          queue<unsigned int> q;

          for (unsigned int j = 0; j < groups; ++j)
            {
              inputFile >> tempInt;
              q.push(tempInt);
            }
          
          for (unsigned int x = 0; x < runs; ++x)
            {
              unsigned int local = 0;
              for (unsigned int y = 0; y < groups; ++y)
                {
                  if ((q.front()+local) <= capacity)
                    {
                      local+=q.front();
                      money+=q.front();
                      q.push(q.front());
                      q.pop();
                    }
                  else
                    {
                      y = groups;
                    }
                }
            }
          cout << "Case #" << i+1 << ": " << money << endl;
        }
    }
  return 0;
}

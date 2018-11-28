#include <iostream>
#include <algorithm>

using namespace std;

int main(void)
{
  int T;
  cin >> T;
  for (int t=1;t<=T;t++)
  {
    cout << "Case #" << t << ": ";
    
    int N;
    cin >> N;

    int pos[2] = {1,1};
    int remaining[2] = {0,0};
    int result = 0;

    for(int i=0;i<N;i++)
    {
      char Ri;
      cin >> Ri;
      int Pi;
      cin >> Pi;
      int robot;
      if (Ri == 'O')
	robot = 0;
      else
	robot = 1;
      
      int time = abs(Pi-pos[robot]) + 1; 
      if (remaining[robot]<time)
      {
	time -= remaining[robot];
	remaining[robot] = 0;
	pos[robot] = Pi;
	remaining[1-robot] += time;
      }	
      else if (remaining[robot]==time)
      {
	time = 1;
	remaining[robot] = 0;
	pos[robot] = Pi;
	remaining[1-robot] += 1;
      }
      else if (remaining[robot]>time)
      {
	time = 1;
	remaining[robot] = 0;
	pos[robot] = Pi;
	remaining[1-robot] += 1;
	
      }
      result += time;
    }
    cout << result;
    cout << endl;
  }

  return 0;
}



#include <iostream>
#include <algorithm>

using namespace std;

const int xorstates = (1 << 21)-1;

int C[2000];
int d[2][xorstates+1][3];
const int dsize = 2*(xorstates+1)*3*sizeof(int);

const int patrick = 0;
const int size = 1;
const int round = 2;

// patrick add is xor

int main(void)
{
  int T;
  cin >> T;
  for (int t=1;t<=T;t++)
  {
    memset(d, -1, dsize);
    int N;
    int SUM = 0;
    int MIN = 1000001;
    cin >> N;
    for (int i=0;i<N;i++)
    {
      cin >> C[i];
      SUM += C[i];
      if(C[i]<MIN)
	MIN = C[i];
    }

    d[0][0][patrick] = C[0];
    d[0][0][size] = 0;
    d[0][0][round] = 0;

    d[0][C[0]][patrick] = 0;
    d[0][C[0]][size] = C[0];
    d[0][C[0]][round] = 0;

    for(int i=1;i<N;i++)
    {
      int curr=i%2;
      int prev=(i+1)%2;
      for(int j=0;j<=xorstates;j++)
      {
	if((d[prev][j][round]==i-1) && 
	   ((d[curr][j ^ C[i]][size] < d[prev][j][size] + C[i]) || (d[curr][j ^ C[i]][round]!=i)))
	{
	  d[curr][j ^ C[i]][patrick] = d[prev][j][patrick];
	  d[curr][j ^ C[i]][size] = d[prev][j][size] + C[i];
	  d[curr][j ^ C[i]][round] = i;
	}
	if((d[prev][j][round]==i-1) && 
	   ((d[curr][j][size] < d[prev][j][size]) || (d[curr][j][round]!=i)))
	{
	  d[curr][j][patrick] = d[prev][j][patrick] ^ C[i];
	  d[curr][j][size] = d[prev][j][size];
	  d[curr][j][round] = i;	  
	}
      }
    }

    int solution = -1;
    for(int j=0;j<=xorstates;j++)
    {
      if ((d[(N-1)%2][j][round]==N-1) && (d[(N-1)%2][j][patrick] == j) && (d[(N-1)%2][j][size] > solution))
	solution = d[(N-1)%2][j][size];
    }
    cout << "Case #" << t << ": ";
    if (solution == SUM)
      solution -= MIN;
    if (solution > -1)
      cout << solution;
    else
      cout << "NO";
    cout << endl;
  }

  return 0;
}



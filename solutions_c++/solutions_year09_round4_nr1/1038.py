#include <cassert>
#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <algorithm>
#include <string>

#define unsigned unsigned long long
#define COUT(x) cout << x << endl
#define forall(v, zero, end) for(unsigned v = zero; v < end; v++)

#define MAX 50000000
int buffer[9][MAX];


using namespace std;

void print(std::vector<unsigned>& v)
{
  for (unsigned i = 0; i < v.size(); i++)
    cout << v[i] << ", ";
  cout << endl;
}

int main(int argc, char* argv[])
{
  ifstream input(argv[1]);

  unsigned C;
  input >> C;

  forall(c, 0, C)
  {
    unsigned N; input >> N;

    std::vector<unsigned> v(N, 0);
    forall (i, 0, N)
      forall (j, 0, N)
    {
      char x;
      input >> x;
      if (x == '1') v[i] = j;
    }

    //    print(v);

    unsigned nmoves = 0;
    forall(k, 0, N)
    {
      unsigned to_move = k;
      forall(i, k, N)
      {
	if (v[i] <= k)
	{
	  to_move = i;
	  break;
	}
      }

      for (int i = to_move; i >= k+1; i--)
      {
	swap(v[i], v[i-1]);
	nmoves++;
      }
      //      print(v);

    }
    cout << "Case #" << c+1 << ": " << nmoves <<endl;

  }
}

#include <iostream>
#include <fstream>
#include <string>
#include <cassert>
#include <sstream>

using namespace std;

#define INF 999999

int tree[16384];
int pos[16384];
int minim[16384][2];

int M, V;

inline int parent(int i)
{
  assert(i != 0);
  return (i - 1) / 2;
}

inline int left(int i)
{
  return (i + 1) * 2 - 1;
}

inline int right(int i)
{
  return (i + 1) * 2;
}

inline bool isparent(int i)
{
  if (left(i) < M) {
    //    cout << i << " " << left(i) << " " << right(i) << " " << M <<  " cucucu" << endl;
    assert(right(i) < M);
  }
  return right(i) < M;
}

inline int min(int a, int b)
{
  return a < b ? a : b;
}

inline int min(int a, int b, int c)
{
  return min(min(a, b), c);
}

int main()
{
  ifstream input("input.in");
  ofstream output("out.out");

  int tests;
  input >> tests;
  for (int test = 0; test < tests; ++test) {
    string answer = "IMPOSSIBLE";
    input >> M >> V;
    for (int i = 0; i < (M - 1) / 2; ++i) {
      assert(isparent(i));
      input >> tree[i] >> pos[i];
      //      cout << i << "    " << tree[i] << " " << pos[i] << endl;
      if (pos[i] == 0) pos[i] = INF;
    }
    for (int i = (M - 1) / 2; i < M; ++i) {
      assert(!isparent(i));
      input >> tree[i];
      //      cout << i << "    " << tree[i] << endl;
      if (pos[i] == 0) pos[i] = INF;
    }
    for (int i = M - 1; i >= 0; --i) {
      //      cout << i << endl;
      if (isparent(i)) {
	if (tree[i] == 1) { // and
	  minim[i][1] = min(
			    minim[left(i)][1] + minim[right(i)][1],
			    pos[i] + minim[left(i)][0] + minim[right(i)][1],
			    pos[i] + minim[left(i)][1] + minim[right(i)][0]
			    );
	  minim[i][0] = min(
			    minim[left(i)][1] + minim[right(i)][0],
			    minim[left(i)][0] + minim[right(i)][1],
			    minim[left(i)][0] + minim[right(i)][0]
			    );
	} else { // or
	  minim[i][1] = min(
			    minim[left(i)][1] + minim[right(i)][0],
			    minim[left(i)][1] + minim[right(i)][1],
			    minim[left(i)][0] + minim[right(i)][1]
			    );
	  minim[i][0] = min(
			    minim[left(i)][0] + minim[right(i)][0],
			    pos[i] + minim[left(i)][1] + minim[right(i)][0],
			    pos[i] + minim[left(i)][0] + minim[right(i)][1]
			    );
	}
      } else {
	minim[i][tree[i]] = 0;
	minim[i][1 - tree[i]] = INF;
      }
      if (minim[i][0] > INF) minim[i][0] = INF;
      if (minim[i][1] > INF) minim[i][1] = INF;
      //      cout << "ttt " << i << " " << minim[i][0] << " " << minim[i][1] << endl;
    }
    if (minim[0][V] < INF) {
      ostringstream oss;
      oss << minim[0][V];
      answer = oss.str();
    }
    output << "Case #" << test + 1 << ": " << answer << endl;
  }
}

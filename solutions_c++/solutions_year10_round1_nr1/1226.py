#include <iostream>
#include <iomanip>
#include <string>
#include <vector>
#include <list>
#include <boost/foreach.hpp>

using namespace std;

std::string getLine()
{
  char line[4096];
  cin.getline(line, 4096);
  return line;
}

#define curr (c+l*N)
#define coord(l, c) (c+l*N)
#define currVal b[curr]
int process(int* b, int N, int K)
{
  //apply transformation: stick to left side (direction unimportant
  for (int l=0; l<N; ++l)
  {
    int cpos = N-1;
    for (int c=N-1; c>=0; --c)
    {
      if (b[curr])
      {
	b[coord(l, cpos)] = b[curr];
	--cpos;
      }
    }
      // clear remaining, we wrote to cpos
      for (int c=0; c<=cpos;++c)
	currVal = 0;
  }
  /*
  for (int l=0; l<N; ++l)
  {
    for (int c=0; c<N; ++c)
      cerr <<currVal;
    cerr << endl;
  }
  cerr << endl;
*/
  // Compute victory condition
  bool victory[2] = {false, false};
  // col
  for (int l=0; l<N; ++l)
  {
    int nsucc = 0;
    int color = 0;
    for (int c=0; c<N; ++c)
    {
      if (color && color == currVal)
      {
	nsucc++;
	if (nsucc == K)
	  victory[color-1] = true;
      }
      else
      {
	nsucc = currVal?1:0;
	color = currVal;
      }
      color = currVal;
    }
  }
  // line
  if (!victory[0] || !victory[1])
  for (int c=0; c<N; ++c)
  {
    int nsucc = 0;
    int color = 0;
    
    for (int l=0; l<N; ++l)
    {
      if (color && color == currVal)
      {
	nsucc++;
	if (nsucc == K)
	  victory[color-1] = true;
      }
      else
      {
	nsucc = currVal?1:0;
	color = currVal;
      }
      color = currVal;
    }
  }
  //diagonal downright
  if (!victory[0] || !victory[1])
  for (int sl=-N+K-1; sl<N*2-K+1; ++sl)
  {
    int c = 0;
    int l = sl;
    //startpoint
    //advance to positive sl
    if (l<0)
    {
      c+= l;
      l = 0;
    }
    if (c<0)
    {
      l-=c;
      c=0;
    }
    int nsucc = 0;
    int color = 0;
    while (l<N && l>=0 && c<N && c>=0)
    {
      if (color && color == currVal)
      {
	nsucc++;
	if (nsucc == K)
	  victory[color-1] = true;
      }
      else
      {
	nsucc = currVal?1:0;
	color = currVal;
      }
      color = currVal;
      l++;
      c++;
    }
  }
  //diagonal downleft
  if (!victory[0] || !victory[1])
  for (int sl=-N+K-1; sl<N*2-K+1; ++sl)
  {
    int c = N-1;
    int l = sl;
    //startpoint
    //advance to positive sl
    if (l<0)
    {
      c-= l;
      l = 0;
    }
    if (c<0)
    {
      l-=c;
      c=0;
    }
    int nsucc = 0;
    int color = 0;
    while (l<N && l>=0 && c<N && c>=0)
    {
      if (color && color == currVal)
      {
	nsucc++;
	if (nsucc == K)
	  victory[color-1] = true;
      }
      else
      {
	nsucc = currVal?1:0;
      }
      color = currVal;
      l++;
      c--;
    }
  }
  return (victory[0]?1:0) + (victory[1]?2:0);
}

int main()
{
  int T;
  cin >> T;
  const char* reply[4] = {"Neither", "Red", "Blue", "Both"};
  for (int t=0; t<T; ++t)
  {
    int N, K;
    cin >> N>>K;
    getLine();
    int* b = new int[N*N];
    for (int l=0; l<N;++l)
    {
      string sl = getLine();
      for (int c=0; c<N;++c)
      {
	if (sl[c] == 'R')
	  currVal = 1;
	else if (sl[c] == 'B')
	  currVal = 2;
	else
	  currVal = 0;
      }
    }
   
    int res = process(b, N, K);
  cout << "Case #" << (t+1) <<": " << reply[res] << endl;
  }
}

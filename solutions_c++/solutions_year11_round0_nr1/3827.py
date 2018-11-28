/*
   Google Code Jam - Qualification Round 2011
   Problem A. Bot Trust

   George Vafiadis
*/

#include <iostream>
#include <vector>
using namespace std;

#define ORANGE 0
#define BLUE   1
#define ABS(X, Y) ( ( (X) > (Y) ) ? ( (X) - (Y)) : ((Y) - (X)) )

struct Button
{
  Button(const char h, const int p)
  {
    if( h == 'O' )
       robot = ORANGE;
    if(h == 'B' )
      robot  = BLUE;

    pos = p;
  }

  int  robot;
  int  pos;
};

int other(const int robot)
{
  return (robot == ORANGE) ? BLUE : ORANGE;
}

int min_finish_time(vector<Button> & seq);

int main(int argc, char *argv[])
{
  int T;

  cin >> T;

  for(int i = 0; i < T; ++i)
  {
   int N;
   vector<Button> seq;

   cin >> N;

   for(int j = 0; j < N; ++j)
    {
     char h;
     int  p;

     cin >> h >> p;
     seq.push_back( Button(h, p) );
    }

   cout << "Case #" << (i+1) << ": " << min_finish_time(seq) << endl;
  }

 return 0;
}

int numMoves(int current, int target)
{
  return ABS(current, target) + 1;
}

int min_finish_time(vector<Button> & seq)
{
 const int size = seq.size();
 int loc[2]     = {1, 1};  // current robot locations
 int remTime[2] = {0, 0};  // remaining time
 int time = 0;

 for(int b = 0; b < size; ++b)
  {
    const int robot = seq[b].robot;
    const int pos   = seq[b].pos;

    int nMoves = numMoves( loc[robot], pos );

    if( remTime[robot] == 0 )
    {
      time += nMoves;
      remTime[other(robot)] += nMoves;
    }
    else if( remTime[robot] >= nMoves )
    {
      ++time;
      ++remTime[other(robot)];
    }
    else if( remTime[robot] < nMoves )
       {
         int remain = nMoves - remTime[robot];
         time += remain;
         remTime[other(robot)] += remain;
       }

   remTime[robot] = 0;
   loc[robot] = pos;
  }

 return time;
}

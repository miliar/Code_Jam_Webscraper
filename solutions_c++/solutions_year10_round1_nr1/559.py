#include <string>
#include <cstdio>
#include <algorithm>
#include <iostream>
using namespace std;
char in[51][51];
char r[51][51];
int di[] = {1, 0, 1, 1, -1, -1, -1, 0};
int dj[] = {0, 1, -1, 1, 0, 1, -1, -1};
bool win[26];
int N, K;

void falldown()
{
  while(true)
    {
      bool found = false;
      for(int i = 0 ; i < N; i++)
	for(int j = 0 ; j < N; j++)
	  {
	    if(r[i][j] != '.' && i != N-1 && r[i+1][j] == '.')
	      {
		found = true;
		while(i!= N-1 && r[i+1][j] == '.')
		  swap(r[i][j], r[i+1][j]);
	      }
	  }
      if(!found)
	break;
    }
}

void won()
{
  for(int i = 0 ; i < N; i++)
    for(int j = 0; j < N; j++){
      char c= r[i][j];
      if( c == 'R' || c == 'B')
	for(int d = 0 ; d < 8; d++){
	  bool YEA = true;
	  for(int k = 1 ; k < K; k++)
	    {
	      int ni = i + k*di[d];
	      int nj = j + k*dj[d];
	      if( ni >= 0 && ni <N && nj >=0 && nj < N){
		if( r[ni][nj] != c){
		  YEA = false;
		  break;
		}}
	      else
		YEA = false;
	    }
	  if(YEA){
	    if( c == 'R')
	      win['R' - 'A'] = true;
	    else if ( c== 'B')
	      win['B'-'A'] = true;
	  }
	  
	}
    }
}
int main()
{
  int T;
  scanf("%d", &T);
  for(int t = 0 ; t < T; t++)
    {
      win['R'-'A'] = false;
      win['B'-'A'] = false;
      scanf("%d %d", &N, &K);
      for(int i = 0 ; i < N; i++)
	scanf("%s", in[i]);
      for(int i = 0 ; i < N; i++)
	for(int j = 0 ; j < N; j++)
	  r[i][j] = in[N - j- 1][i];
      falldown();
      won();
      bool r = win['R'-'A'];
      bool b = win['B'-'A'];
      if( r && b)
	printf("Case #%d: Both\n", t+1);
      else if(r)
	printf("Case #%d: Red\n", t+1);
      else if(b)
	printf("Case #%d: Blue\n", t+1);
      else
	printf("Case #%d: Neither\n", t+1);
	  
    }
}

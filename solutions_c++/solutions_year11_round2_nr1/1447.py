#include <string>
#include <cstdio>
#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <cmath>
using namespace std;
string m[101];
double rpi[101];
int win[101];
int played[101];
double OWP[101];
double OOWP[101];
double WP[101];
int main()
{
  int T;
  cin >> T;
  int C = 1;
  while(T--)
    {
      int N;
      cin >> N;
      for(int i = 0 ; i < N; i++)
	cin >> m[i];
      fill(rpi, rpi + 101, 0);
      fill(win, win + 101, 0);
      fill(played, played + 101, 0);
      for(int i = 0 ; i < N; i++)
	for(int j = 0 ; j < N; j++)
	  {
	    if( m[i][j] != '.')
	      {
		played[i]++;
		if( m[i][j] == '1')
		  win[i]++;
	      }

	  }
      for(int i = 0 ; i < N; i++)
	{
	  WP[i] = win[i] / (played[i] + 0.0);
	}
      for(int i = 0 ; i < N; i++)
	{
	  double OWP_num = 0;
	  int OWP_den = 0;
	  for(int j = 0 ; j < N; j++)
	    {
	      if( m[i][j] != '.' )
		{
		  int top = max(0, win[j] - (m[j][i] == '1'));
		  int bot = played[j] - 1;
		  OWP_num += top / (bot + 0.0);
		  OWP_den ++;
		}
	    }
	  OWP[i] = OWP_num / (OWP_den + 0.0);
	}
      for(int i = 0 ; i < N; i++)
	{
	  double OOWP_num = 0;
	  int OOWP_den = 0;
	  for(int j = 0 ; j < N; j++)
	    {
	      if( m[i][j] != '.' )
		{
		  OOWP_num += OWP[j];
		  OOWP_den++;
		}
	    }
	  OOWP[i] = OOWP_num / OOWP_den;
	}
 
      printf("Case #%d:\n", C++);
           for(int i = 0 ; i < N; i++)
	{
	  rpi[i] = 0.25 * WP[i] + 0.5 * OWP[i] + 0.25 * OOWP[i];
	  cout<<rpi[i]<<endl;
	}
      
    }
}

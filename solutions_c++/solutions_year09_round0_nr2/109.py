#include <cstdio>
#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <queue>
#include <set>
using namespace std;

#define REP(i,n) for(int i=0;i<(n);++i)
#define ALL(c) c.begin(),c.end()
#define PB push_back
#define MP make_pair

int dx[] = { 0, -1 , 0, 0, 1 };
int dy[] = { 0, 0 , -1, 1, 0 };

int H, W;

bool valid(int x, int y)
{
  if( x >=0 && x < H && y>=0 && y< W)
    return true;
  return false;
}


int main()
{
  int tst;
  cin >> tst;
  for(int cas = 1; cas <= tst; cas++)
  {
    cin >> H >> W;
	vector < vector <int> > L(H, vector <int> (W));
	REP(i,H) REP(j,W) cin >> L[i][j];
	vector < vector <int> > T(H, vector <int> (W,80) );	
    
//	cout << "====" << endl;
	int ost = 0;
	REP(i,H) REP(j,W)
	{
	//  cout << i << " " << j << endl;
	  if( T[i][j] != 80) continue;
	  int now = ost;
	  vector < pair<int, int> > P;
	  int x = i, y = j;
	  while(true)
	  {
	      P.PB(MP(x,y));
		  int c = 0;
		  for(int k=1;k<5;k++)
		  {
			if( valid(x+dx[k],y+dy[k]) )
			{
			   if( L[x+dx[c]][y+dy[c]] > L[x+dx[k]][y+dy[k]] )
			   {
				  c = k;
			   }
			}
		  }
		if ( c == 0 ) break;
		if( T[x+dx[c]][y+dy[c]] != 80) { now = T[x+dx[c]][y+dy[c]]; break; }
		x = x+dx[c]; y +=dy[c];
	  }
	  REP(k,P.size()) T[P[k].first][P[k].second] = now;
	  
	  if( now == ost) ost++;
	}
	
	
    cout << "Case #" << cas << ":" << endl;
	REP(i,H)
	{
	  REP(j,W)
	  {
	    cout << (char)('a' + T[i][j]) << " ";
	  }
	  cout << endl;
	}
  }
	
  return 0;
}

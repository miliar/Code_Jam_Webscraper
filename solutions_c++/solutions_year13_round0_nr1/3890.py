#include <algorithm>
#include <numeric>
#include <string>
#include <cstring>
#include <set>
#include <map>
#include <vector>
#include <queue>
#include <iostream>
#include <iterator>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <sstream>
#include <cassert>

#define debug(x) cerr<<#x<<" = "<<(x)<<endl;

using namespace std;
#define ALL(c) (c).begin(), (c).end()
#define SORT(c) sort(ALL(c))
#define VAR(a,b) __typeof(b) a=(b)
#define REVERSE(c) reverse(ALL(c))
#define FOREACH(it,c) for(VAR(it,(c).begin());it!=(c).end();++it)
#define MINN(X,Y) ((X) > (Y) ? (Y) : (X))
#define MAXX(X,Y) ((X) < (Y) ? (Y) : (X))
typedef pair<int, int> PII;
typedef vector<PII> VPII;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef long long LL;

//int a[1000], b[1000];
string m[4];
void solve()
{
  
  int s=1;
  for(int j=0; j<4; j++)
    {
      cin>>m[j];
      //cout<<m[j]<<endl;
    }

  bool Xwon=false;
  bool Owon=false;
  bool empty=false;
   
  for(int i=0;i<4;i++)
    {
      int cntX=0,cntO=0;
      for(int j=0; j<4; j++)
	{
	  if(m[i][j]=='X'  || m[i][j]=='T')
	    {
	      cntX++;
	    }
	  if(m[i][j]=='O'  || m[i][j]=='T')
	    {
	      cntO++;
	    }
	  if(m[i][j]=='.')
	    empty=true;
	}
      if(cntX==4)
	Xwon=true;
      if(cntO==4)
	Owon=true;
    }
  for(int j=0;j<4;j++)
    {
      int cntX=0,cntO=0;
      for(int i=0; i<4; i++)
	{
	  if(m[i][j]=='X'  || m[i][j]=='T')
	    {
	      cntX++;
	    }
	  if(m[i][j]=='O'  || m[i][j]=='T')
	    {
	      cntO++;
	    }
	}
      if(cntX==4)
	Xwon=true;
      if(cntO==4)
	Owon=true;
    }

      int cntX=0,cntO=0;
    for(int i=0;i<4;i++)
    {

	  if(m[i][i]=='X'  || m[i][i]=='T')
	    {
	      cntX++;
	    }
	  if(m[i][i]=='O'  || m[i][i]=='T')
	    {
	      cntO++;
	    }
    }
      if(cntX==4)
	Xwon=true;
      if(cntO==4)
	Owon=true;

     cntX=0,cntO=0;
    for(int i=0;i<4;i++)
    {

	  if(m[i][3-i]=='X'  || m[i][3-i]=='T')
	    {
	      cntX++;
	    }
	  if(m[i][3-i]=='O'  || m[i][3-i]=='T')
	    {
	      cntO++;
	    }
    }
      if(cntX==4)
	Xwon=true;
      if(cntO==4)
	Owon=true;
    
      //debug(Owon);
      //debug(Xwon);
    if( Xwon && Owon)
      cout<<"Draw"<<endl;
    else if( Xwon && !Owon )
      cout<<"X won"<<endl;
    else if( !Xwon && Owon)
      cout<<"O won"<<endl;
    else 
      {
	if( empty) 
	  cout<<"Game has not completed"<<endl;
	else
	  cout<<"Draw"<<endl;
      }

  return;

}

int main()
{
  int T;
    scanf("%d", &T);
    for(int t=1; t<=T; t++)
    {
        printf("Case #%d: ", t);
	if(t>1)
	  {
	    char dum;
	    scanf("%c", &dum);
	  }
        solve();
    }
  return 0;
}

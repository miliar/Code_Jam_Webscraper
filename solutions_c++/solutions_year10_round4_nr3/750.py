#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <climits>
#include <cfloat>
#include <map>
#include <utility>
#include <set>
#include <iostream>
#include <memory>
#include <string>
#include <cstring>
#include <vector>
#include <algorithm>
#include <functional>
#include <sstream>
#include <complex>
#include <stack>
#include <queue>
#include <ctime>
using namespace std;
static const double EPS = 1e-5;
typedef long long ll;
typedef long long LL;
typedef pair<int,int>            PI;
typedef map<PI, int> MPI;
typedef vector<int>	VI;
typedef vector< vector<int> >	VII;
typedef unsigned int UINT32;
typedef unsigned short UINT16;
typedef unsigned char UINT8;

#define MAX_FIELD  100
UINT8 field[2][MAX_FIELD + 10][MAX_FIELD + 10];

int main(void)
{
  int C,c;
  cin>>C;
//cout<<"C="<<C<<endl;
  for(c=1;c<=C;c++)
  {
    int index_curr = 0;
    int index_next = 1;
    memset(field,0,sizeof(field));
    LL count = 0;
    int R,r;
    int x,y;
    cin >>R;
    for(r=0;r<R;r++)
    {
      int x1,x2,y1,y2;
      cin>>x1;
      cin>>y1;
      cin>>x2;
      cin>>y2;
      for(y=y1;y<=y2;y++)
      {
        for(x=x1;x<=x2;x++)
        {
          field[index_curr][y][x] = 1;
          count++;
        }
      }
    }
    LL result = 0;
    while(count>0)
    {
      LL count_next;
      result++;
      count_next = 0;
      for(y=1;y<=MAX_FIELD;y++)
      {
        for(x=1;x<=MAX_FIELD;x++)
        {
          field[index_next][y][x] = 0;
        }
      }
      for(y=1;y<=MAX_FIELD;y++)
      {
        for(x=1;x<=MAX_FIELD;x++)
        {
          if(field[index_curr][y][x]==1)
          {
            if((field[index_curr][y-1][x]==0)&&(field[index_curr][y][x-1]==0))
            {
              //¶‚Æã‚ª0‚Ì‚Æ‚«‚ÍŽ€‚Ê
            }
            else
            {
              field[index_next][y][x] = 1;
              count_next++;
            }
          }
        }
      }
      for(y=1;y<=MAX_FIELD;y++)
      {
        for(x=1;x<=MAX_FIELD;x++)
        {
          if(field[index_curr][y][x]==0)
          {
            if((field[index_curr][y-1][x]==1)&&(field[index_curr][y][x-1]==1))
            {
              //¶‚Æã‚ª1‚Ì‚Æ‚«‚ÍV‚½‚É¶¬
              field[index_next][y][x] = 1;
              count_next++;
            }
          }
        }
      }
      swap(index_next, index_curr);
      count = count_next;
    }
    cout<<"Case #"<<c<<": "<<result<<endl;
  }
  return 0;
}

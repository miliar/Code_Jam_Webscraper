#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <limits>
#include <cctype>

using namespace std;

char arr[10][10];
bool fre,X,O,tie;
int sx[]={1,0,1,1};
int sy[]={0,1,1,-1};

bool check(int x, int y,char c)
{
    if(x>=0 && x<4 && y>=0 && y<4 && (arr[x][y]==c || arr[x][y]=='T'))
        return 1;
    return 0;
}
bool get_answer(int x, int y , char ch)
{

    for(int d=0;d<4;d++)
    {
        int nx=x;
        int ny=y;
        int c=1;
        for(int i=0;i<3;i++)
        {
             nx+=sx[d];
             ny+=sy[d];
            if(check(nx,ny,ch))
                c++;
            else
                break;
        }

        if(c==4)
            return true;
    }

    return false;
}
int main()
{
  freopen("2.in","r",stdin);
  freopen("3.out","w",stdout);
  int tc;
  scanf("%d ",&tc);
  for(int ic=1;ic<=tc;ic++)
  {
      fre=0;
      X=0;
      O=0;

      for(int i=0;i<4;i++)
        for(int j=0;j<4;j++)
      {
          scanf("%c ",&arr[i][j]);
          if(arr[i][j]=='.')
             fre=1;
      }

      for(int i=0;i<4;i++)
        for(int j=0;j<4;j++)
        {
            if(arr[i][j]=='X')
            {
                X|=get_answer(i,j,'X');
            }
            else if(arr[i][j]=='O')
            {
                O|=get_answer(i,j,'O');
            }
            else if(arr[i][j]=='T')
            {
                 X|=get_answer(i,j,'X');
                O|=get_answer(i,j,'O');
            }
        }
        printf("Case #%d: ",ic);
        if(X)
         printf("X won\n");
        else if(O)
            printf("O won\n");
        else if(fre)
            printf("Game has not completed\n");
        else
            printf("Draw\n");


  }
}


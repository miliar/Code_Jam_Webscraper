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

vector <string> vs;

#define INE 0
#define IBO 1
#define IRE 2
#define IBL 3

string table[4] =
{
  "Neither",
  "Both",
  "Red",
  "Blue"
};

char vs_rot[101][101];

int check_xdir(char c,int N,int K)
{
  int y,x;
  for(y=0;y<N;y++)
  {
    int count = 0;
    for(x=0;x<N;x++)
    {
      if(vs_rot[y][x] == c)
      {
        count++;
        if(count==K)return 1;
      }
      else
      {
        count= 0;
      }
    }
  }
  return 0;
}
int check_ydir(char c,int N,int K)
{
  int y,x;
  for(x=0;x<N;x++)
  {
    int count = 0;
    for(y=0;y<N;y++)
    {
      if(vs_rot[y][x] == c)
      {
        count++;
        if(count==K)return 1;
      }
      else
      {
        count= 0;
      }
    }
  }
  return 0;
}

//  ／方向
int check_diag1(char c,int N,int K)
{
  int y,x;
  int xy;
  for(xy=0;xy<=(N-1)*2;xy++)
  {
    int count = 0;
    for(x=0;x<=xy;x++)
    {
      y = xy - x;
      if(vs_rot[y][x] == c)
      {
        count++;
        if(count==K)return 1;
      }
      else
      {
        count= 0;
      }
    }
  }
  return 0;
}

//  ＼方向
int check_diag2(char c,int N,int K)
{
  int y,x;
  int xy;
  for(xy=0;xy<=(N-1)*2;xy++)
  {
    int count = 0;
    for(x=0;x<=xy;x++)
    {
      y = N-1 - (xy - x);
      if(vs_rot[y][x] == c)
      {
        count++;
        if(count==K)return 1;
      }
      else
      {
        count= 0;
      }
    }
  }
  return 0;
}

int main(void)
{
  int T,t;
  cin>>T;
  for(t=1;t<=T;t++)
  {
    int N,K;
    cin>>N;
    cin>>K;
    vs.clear();
    int flagB = 0;
    int flagR = 0;
//cout<<"N="<<N<<"  K="<<K<<endl;
    int i,j;
    for(i=0;i<N;i++)
    {
      string s;
      cin>>s;
      vs.push_back(s);
    }
//for(i=0;i<N;i++)
//cout<<vs[i]<<endl;

    //rotate
    int x,y;
    memset(vs_rot, '.',sizeof(vs_rot));
    for(y=N-1;y>=0;y--)
    {
      int pos_new_x = N-1 - y;
      int pos_new_y = N-1;
      for(x=N-1;x>=0;x--)
      {
        char c = vs[y][x];
        if(c=='.')continue;
        vs_rot[pos_new_y][pos_new_x] = c;
        pos_new_y--;
//cout<<"y="<<y<<" x="<<x<<"  c="<<c<<endl;
      }
//      for(i = pos_new_y;i>=0;i--)
//        vs_rot[i][pos_new_x] = '.';
    }
//for(y=0;y<N;y++)
//{
//for(x=0;x<N;x++)
//cout<<vs_rot[y][x];
//cout<<endl;
//}
    //横チェック
    flagB = check_xdir('B',N,K);
    flagR = check_xdir('R',N,K);
    //縦チェック
    flagB += check_ydir('B',N,K);
    flagR += check_ydir('R',N,K);
    //／チェック
    flagB += check_diag1('B',N,K);
    flagR += check_diag1('R',N,K);
    //＼チェック
    flagB += check_diag2('B',N,K);
    flagR += check_diag2('R',N,K);

    int index = 0;
    if(flagB&&flagR)
    {
      index = IBO;
    }
    else if(flagB)
    {
      index = IBL;
    }
    else if(flagR)
    {
      index = IRE;
    }
    else
    {
      index = INE;
    }

    cout<<"Case #"<<t<<": "<<table[index]<<endl;
  }
  return 0;
}

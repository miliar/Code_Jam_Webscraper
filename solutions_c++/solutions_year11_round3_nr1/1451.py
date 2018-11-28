#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#define FOR(a,b,c) for(int (a) = (b), _n = (c); (a) <= _n ; (a)++)
#define FORD(a,b,c) for(int (a) = (b), _n = (c) ; (a) >= _n ; (a)--)
#define FOR_N(a,b,c,n) for(int (a) = (b), _m = (n), _n = (c) ; (a) <= _n ; (a)+= _m )
#define FORD_N(a,b,c,n) for(int (a) = (b), _m = (n), _n = (c) ; (a) >= _n ; (a)-= _m)
#define EACH(v,it) for(__typeof(v.begin()) it = v.begin(); it != v.end() ; it++)
#define INF 200000000
#define MAX 1

using namespace std;

int r,c;
string str[100];
bool doFill(int row, int col,char ch,bool b)
{
  if(row >= r || row < 0 || col >= c || col < 0) return false;
  if(str[row][col] != '#') return false;
  str[row][col] = ch;
  if(b)
  {
    return doFill(row +1,col ,'\\',false) && doFill(row,col+1,'\\',false) && doFill(row+1,col+1,'/',false);
  }
  return true;
}
int main()
{
  freopen("A-large(1).in","r",stdin);
  freopen("ALarge.out","w",stdout);
  int t;
  int res = 0;
  scanf("%d",&t);
  FOR(ca,1,t)
  {        
    scanf("%d %d",&r,&c);
    FOR(i,0,r-1)
    {
      cin >> str[i];
    }    
    bool b = true;
    FOR(i,0,r-1)
    {
      FOR(j,0,c-1)
      {
        if(str[i][j] == '#') b = b && doFill(i,j,'/',true);
      }
      //cout << str[i] << endl;
    }
    printf("Case #%d:\n",ca);
    if(!b) cout << "Impossible" << endl;
    else FOR(i,0,r-1) cout << str[i] << endl; 
  }
  return 0;
}

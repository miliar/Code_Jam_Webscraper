
//Murugan Thunai !
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <ctime>
#include <fstream>  
using namespace std;

#define pb push_back
#define mp make_pair
#define v(x) vector< x >
#define sz size()
#define FOR(i, first, last) for (int i = (first); i != (last); ++i)
#define FORZ(i,n) FOR(i,0,n)
#define FORO(i,o) FORZ(i,((o).sz))
#define FOREACH(itr, x) for(__typeof(x.begin()) itr = x.begin(); itr != x.end(); itr++)
#define ALL(a) (a).begin(),(a).end()
#define SORT(a) sort(ALL(a))
#define ss stringstream
#define dbg(x) (cerr << #x << ": " << x<<'\n')
#define GI ({int t ; scanf("%d",&t);t;})
#define CLR(x, v) memset(x, v, sizeof(x));
typedef long long ll;
typedef unsigned long long ull;
typedef v(int) vi;
typedef v(vi) vvi;
typedef v(string) vs;
typedef v(vs) vvs;
typedef pair<int,int> ii;
typedef v(ii) vii;
int vis[1000][1000];
int arr[1000][1000];
int H, W;
int dx[] = {-1, 0, 0, +1};
int dy[] = {0, -1, +1, 0};
int component;
int isok(int r, int c)
{
  return r>=0 && r < H && c>=0 && c < W;
}
int func(int row, int col)
{
  if(vis[row][col])
    return vis[row][col];
  vis[row][col] = component;
  ii flow_into(-1, -1);
  int mini = INT_MAX/2;
  FORZ(i, 4)
  {
    int nr = row + dx[i];
    int nc = col + dy[i];

    if(isok(nr, nc))
    {
      if(arr[nr][nc] < arr[row][col])
      {
        if(arr[nr][nc] < mini)
        {
          mini = arr[nr][nc];
          flow_into = ii(nr, nc);
        }
      }
    }

  }
  if(mini != INT_MAX/2)
  {
    //cout << arr[row][col] << " (" << row << " , " << col << " )flows into " << arr[flow_into.first][flow_into.second] << endl;
    vis[row][col] = func(flow_into.first, flow_into.second);
  }
  return vis[row][col];
}
int main()
{
  int N = GI;
  FORZ(testcase, N)
  {
    component = 'a';
    printf("Case #%d:\n", testcase+1);
    H = GI, W = GI;
    CLR(vis, 0);
    FORZ(i, H)
      FORZ(j, W)
        arr[i][j] = GI;
    FORZ(i, H)
      FORZ(j, W)
      {
        if(!vis[i][j])
        {
          func(i, j);
          component ++;
        }
      }
    int id = 'a';
    set<char> dic;
    int lookup[256] = {0};
    FORZ(i, H)
    {
      FORZ(j, W)
      {
        char ans;
        if(!dic.count(vis[i][j]))
        {
          dic.insert(vis[i][j]);
          lookup[vis[i][j]] = id++;
        }
        printf("%c", lookup[vis[i][j]]);
        if(j != W-1)
          printf(" ");
      }
      printf("\n");
    }

  }
	return 0;
}
//Powered by Siddharth

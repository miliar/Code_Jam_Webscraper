
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
int bpos = 1, opos = 1;
int bindex = 0, oindex = 0;
vi B, O;
int arr_index = 0;
vector<pair<char, int> > arr;
int button_pushed = 0;
void move(char c)
{
  if(arr_index >= arr.size())return;
  int dir[] = {-1, 0, 1};
  if(c == 'B')
  {
    if(bindex == B.size())return;
    if(arr[arr_index].first == 'B' && bpos == arr[arr_index].second && !button_pushed)
    {
      //push button
      button_pushed = 1;
      arr_index++;
      bindex++;
      //cout << "B pushed button!----------------------------------" << endl;
      return;
    }
    int dis = INT_MAX/2, d;
    for(int i=0;i<3;i++)
    {
      int pos = bpos + dir[i];
      if(pos == 0) continue;
      int tmp = abs(pos - B[bindex]);
      if(tmp < dis)
        dis = tmp, d = dir[i];
    }
    if(dis != INT_MAX/2)
    {
      bpos += d;
      //cout << "B moves " << d << endl;
    }
  }
  else
  {
    if(oindex == O.size())return;
    if(arr[arr_index].first == 'O' && opos == arr[arr_index].second && !button_pushed)
    {
      //push button
      button_pushed = 1;
      arr_index++;
      oindex++;
      //cout << "O pushed button!----------------------------------" << endl;
      return;
    }
    int dis = INT_MAX/2, d;
    for(int i=0;i<3;i++)
    {
      int pos = opos + dir[i];
      if(pos == 0) continue;
      int tmp = abs(pos - O[oindex]);
      if(tmp < dis)
        dis = tmp, d = dir[i];
    }
    if(dis != INT_MAX/2)
    {
      opos += d;
      //cout << "O moves " << d << endl;
    }
  }
}

int main()
{
  int T = GI;
  FOR(testcase, 1 , T+1)
  {
    int N = GI;
    arr_index = 0;
    B.clear(); O.clear();arr.clear(); 
    button_pushed = 0;
    FORZ(i, N)
    {
      string color;
      int pos;
      cin >> color >> pos;
      if(color[0] == 'B')
        B.push_back(pos);
      if(color[0] == 'O')
        O.push_back(pos);
      arr.push_back(mp(color[0], pos));
    }
    bpos = 1, opos = 1;
    bindex = 0, oindex = 0;
    int ans = 0;
    while(1)
    {
      button_pushed = 0;
      ans++;
      if(arr_index == arr.size())break;
      move('B');
      if(arr_index == arr.size())break;
      move('O');
      if(arr_index == arr.size())break;
      //dbg(ans);getchar();
    }
    printf("Case #%d: %d\n", testcase, ans);
  }
	return 0;
}
//Powered by Siddharth

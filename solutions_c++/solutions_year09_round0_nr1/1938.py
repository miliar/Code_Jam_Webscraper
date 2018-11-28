
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
int cnt = 0;
set<string> dic;
void func(int row, vs& arr, string cur)
{
  if(!dic.count(cur))
  {
    return;
  }
  if(row == arr.size())
  {
    //dbg(cur);
    if(dic.count(cur))
    {
      //cout << cur << endl;
      cnt++;
    }
    return;
  }
  FORZ(i, arr[row].size())
  {
    func(row + 1, arr, cur + arr[row][i]);
  }
}
int main()
{
  int L, N, D;
  L = GI, D = GI, N = GI;
  dic.insert("");
  //dbg(L);dbg(D);dbg(N);
  FORZ(i, D)
  {
    string str;
    cin >> str;
    for(int i=1; i<=str.size();i++)
      dic.insert(str.substr(0, i));
  }
  FORZ(testcase, N)
  {
    dbg(testcase);
    printf("Case #%d: ", testcase + 1);
    string str;
    cin >> str;
    vs arr;
    int open = 0;
    string toBeAdded = "";
    FORO(i, str)
    {
      if(str[i] == '(')
      {
        open = 1;
      }
      else if(str[i] == ')')
      {
        open = 0;
        arr.push_back(toBeAdded);
        toBeAdded = "";
      }
      else
      {
        if(open)
          toBeAdded += string(1, str[i]);
        else
          arr.push_back(string(1, str[i]));
      }
    }
    //FORO(i, arr)
    //  dbg(arr[i]);
    cnt = 0;
    func(0, arr, "");
    cout << cnt << endl;
  }
	return 0;
}
//Powered by Siddharth

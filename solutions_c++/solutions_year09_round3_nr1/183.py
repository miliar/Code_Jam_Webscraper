
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
int main()
{
  int T = GI;
  FORZ(testcase, T)
  {
    int base;
    dbg(testcase);
    printf("Case #%d: ", testcase+1);
    string str;
    cin >> str;
    set<char> arr(ALL(str));

    if(arr.size() == 1)
    {
      base = 2;
      cout << (1LL << str.size()) - 1 << endl;
    }
    else
    {
      base = arr.size();
      dbg(base);
      map<char, int>dic;
      set<char>s;
      int allocated[100] = {0};
      dic[str[0]] = 1;
      s.insert(str[0]);
      allocated[1] = 1;
      for(int i=1;i<str.size();i++)
      {
        if(s.count(str[i]))continue;
        for(int j=0;j<100;j++)
          if(!allocated[j])
          {
            dic[str[i]] = j;
            s.insert(str[i]);
            allocated[j] = 1;
            break;
          }
      }
      ll sum = 0;
      ll powb = 1;
      for(int i = str.size() - 1; i>=0;i--)
      {
        sum = dic[str[i]] * powb + sum;
        powb *= base;
      }
      cout << sum << endl;
    }
  }
	return 0;
}
//Powered by Siddharth


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
  int T=GI;
  FOR(testcase, 1, T+1)
  {
    int C=GI;
    vs oppose;
    map<string, char> combine;
    FORZ(i, C)
    {
      string t; cin >> t;
      string str1 = ""; str1 += t[0]; str1 += t[1];
      string str2 = ""; str2 += t[1]; str2 += t[0];
      combine[str1] = t[2];
      combine[str2] = t[2];
    }
    int D=GI;
    FORZ(i, D)
    {
      string t; cin >> t; oppose.push_back(t);reverse(ALL(t));oppose.push_back(t);
    }
    int N=GI;
    string str;
    cin >> str;
    vector<char> arr;
    FORO(i, str)
    {
      char ch = str[i];
      if(arr.size() == 0)
      {
        arr.push_back(ch);
        continue;
      }
      char last = arr[arr.size() - 1];
      string str1 = ""; str1 += last; str1 += ch;
      string str2 = ""; str2 += ch; str2 += last;
      char val1 = combine[str1];
      char val2 =  combine[str2];

      if(val1 != 0 || val2 != 0)
      {
        arr.pop_back();
        arr.push_back(val1);
        continue;
      }

      int cleared = 0;
      FORO(j, oppose)
      {
        if(oppose[j][0] == ch && find(ALL(arr), oppose[j][1])!=arr.end())
        {
          arr.clear();
          cleared = 1;
          break;
        }
      }
      if(!cleared)
        arr.push_back(ch);
    }
    printf("Case #%d: [", testcase);
    if(arr.size() == 0)
      cout << "]" << endl;
    else
    {
      FORO(i, arr)
      {
        cout << arr[i];
        if(i != arr.size()-1)
          cout << ", ";
        else
          cout << "]" << endl;
      }
    }
  }
	return 0;
}
//Powered by Siddharth

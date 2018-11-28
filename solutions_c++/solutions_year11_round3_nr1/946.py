
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
  FOR(test, 1, T+1)
  {
    int R = GI, C = GI;
    vector<string> arr(R);
    FORO(i, arr)
      cin >> arr[i];
    FOR(i, 0, arr.size() - 1)
    {
      for(int j=0;j<arr[i].size() - 1; j ++)
      {
        if(arr[i][j] == '#' && arr[i][j+1] == '#' && arr[i+1][j] == '#' && arr[i+1][j+1] == '#')
        {
          arr[i][j] = '/';
          arr[i][j+1] = '\\';
          arr[i+1][j] = '\\';
          arr[i+1][j+1] = '/';
        }
      }
    }
    int valid = 1;
    FORO(i, arr)
      FORO(j, arr[i])
        if(arr[i][j] == '#')
        {
          valid = 0;
          goto end;
        }
end:
    if(!valid)
    {
      printf("Case #%d:\nImpossible\n", test);
    }
    else
    {
      printf("Case #%d:\n", test);
      FORO(i, arr)cout<<arr[i]<<endl;
    }
  }
	return 0;
}
//Powered by Siddharth

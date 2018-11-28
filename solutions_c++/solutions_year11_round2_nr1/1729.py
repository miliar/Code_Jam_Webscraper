
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
#define MAX 1000
double wp[MAX], owp[MAX], oowp[MAX];
double WP(vector<string>& arr, int pos)
{
  int n = 0, d = 0;
  for(int i=0;i<arr[0].size();i++)
  {
    if(arr[pos][i] == '0' || arr[pos][i] == '1')
      d++, n += arr[pos][i] == '1';
  }
  return (n+0.) / (d+0.);
}
double OWP(vector<string>& arr, int pos)
{
  double sum = 0.;
  int dd = 0;
  for(int i=0;i<arr.size();i++)
  {
    if(i == pos || arr[pos][i] == '.') continue;
    dd++;
    int n = 0, d = 0;
    for(int j=0;j<arr.size();j++)
    {
      if(j == pos) continue;
      if(arr[i][j] == '0' || arr[i][j] == '1')
      {
        d++, n += arr[i][j] == '1';
      }
    }
    sum += (n+0.)/(d+0.);
  }
  return sum / (dd+0.);
}
double OOWP(vector<string> & arr, int pos)
{
  double sum = 0.;
  int d = 0;
  for(int i=0;i<arr.size();i++)
  {
    if(i == pos || arr[i][pos] == '.') 
    {
      continue;
    }
    sum += owp[i];
    d++;
  }
  return sum / (d+0.);
}
int main()
{
  int T = GI;
  for(int test = 1; test <= T; test++)
  {
    printf("Case #%d:\n", test);
    int N=GI;
    vector<string> arr(N);
    FORO(i, arr)
      cin >> arr[i];
    for(int i=0;i<N;i++)
    {
      wp[i] = WP(arr, i);
      owp[i] = OWP(arr, i);
    }
    for(int i=0;i<N;i++)
    {
      
      oowp[i] = OOWP(arr, i);
      double rpi = 0.25*wp[i] + 0.5*owp[i] + 0.25*oowp[i];
      cout << rpi << endl;
    }
  }
	return 0;
}
//Powered by Siddharth

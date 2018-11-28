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

typedef pair<int,int> pii;

pii data[110];
double wp[110];
double owp[110];
double oowp[110];
string state[110];
int n;

int main()
{
  freopen("A-large(1).in","r",stdin);
  freopen("ALarge.out","w",stdout);
  int t;
  cin >> t;  
  FOR(ca,1,t)
  {
    cout << "Case #" << ca << ":" << endl;
    scanf("%d",&n);
    FOR(i,0,n-1)
    {
      cin >> state[i];
      string & str = state[i];
      int win = 0 , lose = 0;
      FOR(j,0,str.length()-1)
      {
        if(str[j] == '.') continue;      
        if(str[j] == '0') lose++;
        else win++;
      }
      data[i] = pii(win,lose);
      wp[i] = (double) win / (double)(win + lose);        
    }  
    FOR(i,0,n-1)
    {
      string & str = state[i];
      owp[i] = 0.0f;
      int cnt = 0;
      FOR(j,0,str.length()-1)
      {
        if(str[j] != '.') 
        {
          int win = data[j].first;
          int lose = data[j].second;
          if(str[j] == '1') lose--; 
          else win--;
          owp[i] += (double)(win) /(double)(win + lose);
          cnt++;
        }
      }
      owp[i] = owp[i]/ (double)cnt;
    }
    FOR(i,0,n-1)
    {
      string & str = state[i];
      oowp[i] = 0.0f;
      int cnt = 0;
      FOR(j,0,str.length()-1)
      {
        if(str[j] != '.') 
        {
          oowp[i] += owp[j];
          cnt++;
        }
      }
      oowp[i] = oowp[i] / (double)cnt;
    }
    FOR(i,0,n-1)
    {
      double  RPI = 0.25 * wp[i] + 0.50 * owp[i] + 0.25 * oowp[i];
      cout.precision(12);
      cout << RPI << endl;
    }
  }
  return 0;
}

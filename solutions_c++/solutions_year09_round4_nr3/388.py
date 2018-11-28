#include <algorithm> 
#include <string> 
#include <set> 
#include <map> 
#include <vector> 
#include <queue> 
#include <iostream> 
#include <iterator> 
#include <sstream> 
#include <cmath> 
#include <cstdio> 
#include <cstdlib> 
#include <numeric>
#include <memory.h> 

using namespace std; 

#define FOR(i,a,b) for (int _n(b), i(a); i < _n; i++) 
#define REP(i,n) FOR(i,0,n) 
#define pb push_back 
#define sz size() 

#define ALL(c) (c).begin(), (c).end() 
#define SORT(c) sort(ALL(c))
#define UNIQUE(c) SORT((c)), (c).erase(unique(ALL((c))), (c).end())
#define INF 2147483647
#define MAX(a,b) (((a) > (b)) ? (a) : (b))
#define MIN(a,b) (((a) < (b)) ? (a) : (b))
#define MP(a,b)	 make_pair((a), (b))
#define X first
#define Y second

typedef pair<int,int> ii;
typedef vector<int > vi;
typedef vector<vi > vvi;
typedef vector<ii  > vii;
typedef vector<vii  > vvii;
typedef long long ll;

string filename = "C-small-attempt0";

int mem[20][20];


int res = 100;

int dp[1<<17];
int valid[1<<17];

int n, k;

int isValid(int mask)
{
   if (valid[mask] != -1)
      return valid[mask];

   REP(i, n)
   {
      if (mask & (1<<i))
      {
         FOR(j, i+1, n)
            if (mask & (1<<j))
               if (mem[i][j])
               {
                  valid[mask] = 0;
                  return 0;
               }
      }
   }
   valid[mask] = 1;
   return 1;
}


int go(int left)
{
   if (dp[left] != -1)
      return dp[left];

   int& ret = dp[left];

   if (left == 0)
   {
      ret = 0;
      return ret;
   }

   ret = n;
   for (unsigned int mask = left; mask >= 0; mask = (mask - 1) & left)
	{
      if (mask == 0)
         break;
		if (isValid(mask))
      {
         int rr = go(left ^ mask) + 1;
         if (ret > rr)
            ret = rr;
      }
	}

   return ret;
}


int main()
{	
	string str_fin = filename + ".in", str_fout = filename + ".out";
	freopen(str_fin.c_str(), "r", stdin);		
	freopen(str_fout.c_str(), "w", stdout);

	int T;
	cin>>T;
	REP(t, T)
	{
      vector<vector<int> > v;
      cin>>n>>k;
      REP(i, n)
      {
         vector<int> vv;
         REP(j, k)
         {
            int x;
            cin>>x;
            vv.pb(x);
         }
         v.pb(vv);
      }
      memset(mem, 0, sizeof(mem));
      REP(i, n)
      {
         FOR(j, i + 1, n)
         {
            bool fl = false;
            if (v[i][0] == v[j][0])
               fl = true;
            FOR(l, 1, k)   
            {
               if (v[i][l] == v[j][l])
               {
                  fl = true;
                  break;
               }
               int c1 = 1, c2 = 1;
               if (v[i][l-1] > v[j][l-1])
                  c1 = -1;
               if (v[i][l] > v[j][l])
                  c2 = -1;
               if (c1*c2 < 0)
               {
                  fl = true;
                  break;
               }
            }
            mem[i][j] = mem[j][i] = (fl ? 1 : 0);
         }
      }

      memset(dp, -1, sizeof(dp));
      memset(valid, -1, sizeof(valid));
      int res = go((1<<n) - 1);

      cout<<"Case #"<<t+1<<": "<<res<<endl;
	}

	return 0;
}
#include <vector>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <fstream>
#include <deque>
#include <set>

using namespace std;

const double EPS = 1e-10;
const double PI = 3.14159265358979323846264338328;

#define PB push_back
#define FOR(a,start,end) for(int a = int(start); a < int(end); a++)
#define INF INT_MAX
#define MSG(a) cout << #a << " = " << a << endl;
#define SORT(a) sort(a.begin(),a.end())

#define MOD 10007


int main()
{
   ofstream fout;
   fout.open("outputDsmall.txt");
//   ifstream fin("input.txt");
 ifstream fin("D-small-attempt0.in");

    
   int N;
   fin >> N;
   
   FOR(k,1,N+1)
   {
		int H,W,R;
		fin >> H >> W >> R;
		H--;
		W--;
		vector<int> x;
		vector<int> y;
		FOR(m,0,R)
		{
			int tmp1, tmp2;
			fin >> tmp1 >> tmp2;
			x.PB(tmp1-1);
			y.PB(tmp2-1);
		}
		
		long long dp[105][105];
		FOR(i,0,105) FOR(j,0,105) dp[i][j] = 0;
		
		dp[0][0] = 1;
		
		FOR(i,1,H+1)
		FOR(j,1,W+1)
		{
			int bad = 0;
			FOR(t,0,x.size())
				if(x[t] == i && y[t] == j) { bad = 1; break; }
			if(bad == 1) continue;
			if(i-1 >= 0 && j-2 >= 0) dp[i][j] += dp[i-1][j-2];
			if(i-2 >= 0 && j-1 >= 0) dp[i][j] += dp[i-2][j-1];
			dp[i][j] %= MOD;
		}
			
		fout << "Case #" << k << ": " << dp[H][W]%MOD << endl;
				
      
   }
   
   return 0; 
    
    
    
    
    
    
}


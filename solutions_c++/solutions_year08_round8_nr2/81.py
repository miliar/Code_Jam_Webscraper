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
#include <map>

using namespace std;

const double EPS = 1e-10;
const double PI = 3.14159265358979323846264338328;

#define PB push_back
#define FOR(a,start,end) for(int a = int(start); a < int(end); a++)
#define INF INT_MAX
#define MSG(a) cout << #a << " = " << a << endl;
#define SORT(a) sort(a.begin(),a.end())


int main()
{
   ofstream fout;
   fout.open("outputBsmall3.txt");
//   ifstream fin("input.txt");
 ifstream fin("B-small-attempt2.in");

    
   int N;
   fin >> N;
   
   FOR(ttt,1,N+1)
   {
		cout << ttt << endl;
		int offers;
		fin >> offers;
		
		map<string,int> M;
		
		vector<string> colors;
		vector<int> start;
		vector<int> end;
		
		FOR(p,0,offers)
		{
			string a;
			int b,c;
			fin >> a >> b >> c;
			colors.PB(a);
			start.PB(b);
			end.PB(c);
		}
		
		int best = INF;
		
		FOR(k,1,(1<<offers))
		{
			set<string> SS;
			
			bool dp[10005];
			memset(dp,0,sizeof dp);
			
			int cntt = 0;
			
			FOR(t,0,offers)
				if((k>>t)%2 == 1)
				{
					SS.insert(colors[t]);
					cntt++;
				}
			if(SS.size() > 3)
				continue;
			if(cntt >= best) continue;
			
			FOR(t,0,offers)
				if((k>>t)%2 == 1)
				{
					FOR(pp,start[t],end[t]+1)
						dp[pp] = 1;
				}
			
			int bad = 0;
			FOR(t,1,10001)
				if(dp[t] == 0)
				{
					bad = 1;
					break;
				}
			if(bad == 1) continue;	
			
			best <?= cntt;
		}
			
		
				
		if(best == INF)
		{
			fout << "Case #" << ttt << ": " << "IMPOSSIBLE" << endl;
		}
		else
		{
			fout << "Case #" << ttt << ": " << best << endl;
		}



   }
				
			
		
   
   return 0; 
    
    
    
    
    
    
}


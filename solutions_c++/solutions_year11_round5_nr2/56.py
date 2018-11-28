#include <iostream>
#include <iomanip>
#include <cmath>
#include <fstream>
#include <cstdlib>
#include <set>
#include <map>
#include <vector>
#include <cstdio>
#include <algorithm>
#include <deque>
#include <cstring>
#include <ctime>
#include <complex>

using namespace std;

#define MSG(a) cout << #a << " = " << a << endl;
#define FOR(a,start,end) for(int a = int(start); a < int(end); a++)
#define PB push_back

int main()
{
// 	ifstream fin("B-sample.in");
// 	ofstream fout("B-sample.out");
	ifstream fin("B-small-attempt0.in");
	ofstream fout("B-small-attempt0.out");
//	ifstream fin("B-large.in");
//	ofstream fout("B-large.out");

	int T;
	fin >> T;
	for(int trz = 0; trz < T; trz++)
	{
		fout << "Case #" << trz+1 << ": ";
		
		vector<int> repV;
		int N;
		fin >> N;
		FOR(i,0,N)
		{
			int tmp;
			fin >> tmp;
			repV.PB(tmp);
		}
		
		sort(repV.begin(),repV.end());
		
		int ans = 0;
		
		FOR(i,1,N+1)
		{
			//try to make straights of length i
			
			vector<int> V = repV;
			
			vector<int> last;
			
			int bad = 0;
			
			while(V.size() > 0)
			{
				int curr = V[0];
				int cnter = 0;
				
				FOR(p,0,V.size())
				if(V[p] == curr+cnter)
				{
					cnter++;
					if(cnter == i) break;
				}
				
				if(cnter != i)
				{
					int er = 0;
					FOR(p,0,last.size())
					if(last[p] == V[0]-1)
					{
						last[p]++;
						V.erase(V.begin());
						er = 1;
						break;
					}
					if(er) continue;
					else 
					{
						bad = 1;
						break;
					}
				}
				
				cnter = 0;
				FOR(p,0,V.size())
				if(V[p] == curr+cnter)
				{
					V.erase(V.begin() + p);
					p--;
					cnter++;
					if(cnter == i) break;
				}
				last.PB(curr+cnter-1);
			}
			
			if(bad) break;
			ans = i;
		}
				
				fout << ans << endl;





	}
	return 0;
}







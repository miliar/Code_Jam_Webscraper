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
   fout.open("outputDsmall.txt");
   ifstream fin("D-small-attempt0.in");
    
   int N;
   fin >> N;
   
   FOR(i,1,N+1)
   {
		int k;
		fin >> k;
		string s;
		fin >> s;
		
		vector<int> perm;
		FOR(t,0,k)
		perm.PB(t);
		
		int best = INF;
		
		vector<int> done = perm;
		do
		{
			string tmp = s;
			string newOne;
			while(tmp.size() > 0)
			{
				string tt = tmp.substr(0,k);
				tmp = tmp.substr(k);
				FOR(t,0,k)
					newOne += tt[perm[t]];
			}
			
			int cnt = 0;
			FOR(t,0,newOne.size()-1)
				if(newOne[t] == newOne[t+1])
				{
					newOne.erase(t,1);
					t--;
				}
				else cnt++;
			
			best <?= (int)newOne.size();
			
			next_permutation(perm.begin(),perm.end());
			
		} while(done != perm);
		
		 

      fout << "Case #" << i << ": " << best << endl;
   }
   
   return 0; 
    
    
    
    
    
    
}


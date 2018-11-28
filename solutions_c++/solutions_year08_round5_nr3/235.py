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


int tester[2200];

int bitCnt(int mask) 
{
  return (mask==0 ? 0 : bitCnt(mask & (mask - 1)) + 1);
}



int main()
{
   ofstream fout;
   fout.open("outputCsmall.txt");
//   ifstream fin("input.txt");
 ifstream fin("C-small-attempt0.in");

	FOR(k,0,2100)
	{
		//1 is bad
		int tmp = k;
		int bad = 0;
		while(tmp > 0)
		{
			if(tmp%4 == 3)
			{
				bad = 1;
				break;
			}
			tmp /= 2;
		}
		if(bad == 1) tester[k] = 1;
		else tester[k] = 0;
	}
		
	
		
	

    
   int K;
   fin >> K;
   
   FOR(z,1,K+1)
   {
		int M,N;
		fin >> M >> N;
		
		vector<int> bad;
		FOR(k,0,M)
		{
			int val = 0;
			char tmp;
			FOR(l,0,N)
			{
				fin >> tmp;
				if(tmp == 'x')
					val += (1 << l);
			}
			bad.PB(val);
		}	
		
		long long dp[15][2000];
		FOR(k,0,M)
		FOR(l,0,(1 << N))
			dp[k][l] = 0;

		long long best = 0;

		FOR(k,0,M)
		FOR(l,0,(1 << N))
		if((l & bad[k]) == 0 && tester[l] == 0)
		{
			if(k == 0)
			{
				dp[k][l] >?= bitCnt(l);
				best >?= dp[k][l];
				continue;
			}
			
			FOR(m,0,(1 << N))
			{
				if(((m >> 1) & l) == 0 && ((m << 1)&l) == 0)
					dp[k][l] >?= dp[k-1][m] + bitCnt(l);
			}
			best >?= dp[k][l];
		}		

      fout << "Case #" << z << ": " << best << endl;
   }
   
   return 0; 
    
    
    
    
    
    
}


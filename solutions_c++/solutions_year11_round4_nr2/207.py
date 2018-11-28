#include <iostream>
#include <cmath>
#include <fstream>
#include <cstdlib>
#include <set>
#include <map>
#include <vector>
#include <cstdio>
#include <algorithm>
#include <deque>

using namespace std;

#define MSG(a) cout << #a << " = " << a << endl;
#define FOR(a,start,end) for(int a = int(start); a < int(end); a++)
#define PB push_back

const double PI = 3.14159265358979;
const double EPS = 1e-12;

double G[505][505];


int main()
{
	ifstream fin("B-small-attempt0.in");
	ofstream fout("B-small-attempt0.out");
	
	int T;
	fin >> T;
	for(int ta = 0; ta < T; ta++)
	{
		fout << "Case #" << ta+1 << ": ";
		int R, C, D;
		fin >> R >> C >> D;
		char tmp;
		FOR(i,0,R)
		FOR(j,0,C)
		{
			fin >> tmp;
			G[i][j] = tmp-'0'+D;
		}
		
		int best = 0;
		FOR(a,0,R)
		FOR(b,0,C)
		FOR(k,3,11)
		{
			if(a + k > R || b + k > C) continue;
			double sumx = 0;
			double mass = 0;
			double sumy = 0;
			
			FOR(m,a,a+k)
			FOR(n,b,b+k)
			{
				if(m == a && n == b) continue;
				if(m == a+k-1 && n == b) continue;
				if(m == a && n == b+k-1) continue;
				if(m == a+k-1 && n == b+k-1) continue;
				sumx += (n-b)*G[m][n], mass += G[m][n];
				sumy += (m-a)*G[m][n];
			}
			
			sumx /= mass, sumy /= mass;
			double targetx = ((double)k-1)/2;
			double targety = ((double)k-1)/2;
						
			if(fabs(sumx-targetx) < 1e-9 && fabs(sumy-targety) < 1e-9)
			{
				best = max(best,k);
			}
		}
		if(best == 0) fout << "IMPOSSIBLE\n";
		else fout << best << endl;
	}
	return 0;
}
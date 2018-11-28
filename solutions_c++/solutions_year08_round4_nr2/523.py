#include <vector>#include <algorithm>
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
   fout.open("output.txt");
   ifstream fin("B-small-attempt0.in");
    
   int C;
   fin >> C;
   
   FOR(k,1,C+1)
   {
		int N,M,A;
		fin >> N >> M >> A;
		
		fout << "Case #" << k << ": ";
		
		int done = 0;
		
		FOR(x1,0,N+1)
		FOR(y1,0,M+1)
		FOR(x2,0,N+1)
		FOR(y2,0,M+1)
		{
			if(done == 1) break;
			
			if(abs((long long)x1*y2-(long long)x2*y1) == A)
			{
				fout << "0 0 " << x1 << " " << y1 << " " << x2 << " " << y2 << endl;
				done = 1;
				break;
			}
		}
		
		if(done == 0)
			fout << "IMPOSSIBLE\n";
	}
	
   return 0; 
    
    
    
    
    
    
}


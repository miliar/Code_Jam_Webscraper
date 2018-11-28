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
   fout.open("outputAlarge.txt");
   ifstream fin("A-large.in");
    
   int N;
   fin >> N;
   
   FOR(k,1,N+1)
   {
		long long n,A,B,C,D,x0,y0,M;
		fin >> n >> A >> B >> C >> D >> x0 >> y0 >> M;

		long long a[3][3];
		FOR(t,0,3)
		FOR(u,0,3)
			a[t][u] = 0;

		long long X = x0, Y = y0;
		a[X%3][Y%3]++;
		FOR(i,1,n)
		{
			X = (A*X+B)%M; Y = (C*Y+D)%M;
			a[X%3][Y%3]++;
//			fout << X << " " << Y << endl;
		}

		long long ans = 0;

		FOR(t,0,3)
		FOR(u,0,3)
			ans += a[t][u]*(a[t][u]-1)*(a[t][u]-2)/6;
		
		FOR(t,0,3)
			ans += a[t][0]*a[t][1]*a[t][2];
		FOR(u,0,3)
			ans += a[0][u]*a[1][u]*a[2][u];
		
		long long sub = 0;
		
		FOR(t,0,3)
		FOR(u,0,3)
		FOR(v,0,3)
		FOR(w,0,3)
		FOR(x,0,3)
		FOR(y,0,3)
			if(t != u && u != v && v != t && w != x && w != y && x != y)
				sub += a[t][w]*a[u][x]*a[v][y];

	ans += sub/6;
			
		fout << "Case #" << k << ": " << ans << endl;



      
   }
   
   return 0; 
    
    
    
    
    
    
}


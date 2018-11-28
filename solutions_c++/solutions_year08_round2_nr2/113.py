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


int isPrime(int n) 
{
if(n <= 1) return 0;
if(n == 2) return 1;
if(n % 2 == 0) return 0;
for(int t = 3; (long long)t*(long long)t <= n; t += 2)
	if(n % t == 0) return 0;
return 1;
}



int gcd(int n1, int n2)
{
	return n2 == 0 ? n1 : gcd(n2, n1%n2);
}

long long A,B,P;
int visited[1005];

void dfs(int i)
{
	if(visited[i] == 1) return;
	
	visited[i] = 1;
	
	FOR(t,A,B+1)
	{
		if(visited[t] == 0)
		{
			int g = gcd(t,i);
			int ok = 0;
			FOR(u,P,g+1)
				if(isPrime(u) == 1 && g%u == 0)
				{
					ok = 1;
					break;
				}
			if(ok == 1)
				dfs(t);
		}
	}
	return;
}			
			
			


int main()
{
   ofstream fout;
   fout.open("outputBsmall.txt");
   ifstream fin("B-small-attempt0.in");
    
   int N;
   fin >> N;
   
   
   
   FOR(k,1,N+1)
   {
		fin >> A >> B >> P;
		
		FOR(t,0,1005)
			visited[t] = 0;
		
		int ans = 0;
		FOR(i,A,B+1)	
		{
			if(visited[i] == 1) continue;
			
			ans++;
			
			dfs(i);
		}		

	fout << "Case #" << k << ": " << ans << endl;
				

      
   }
   
   return 0; 
    
    
    
    
    
    
}


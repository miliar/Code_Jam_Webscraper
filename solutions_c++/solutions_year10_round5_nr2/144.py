#include <iostream>
#include <sstream>
#include <cstring>
#include <fstream>
#include <string>
#include <vector>
#include <cmath>
#include <cstdlib>
#include <map>
#include <deque>
#include <set>
#include <iomanip>
#include <algorithm>
#include <cstdio>
#include <climits>
using namespace std;

double PI = 3.14159265358979323846264338328;
double EPS = 1e-10;

#define PB push_back
#define FOR(a,start,end) for(int a = int(start); a < int(end); a++)
#define MSG(a) cout << #a << " = " << a << endl;
#define ITOA(a) char c[500];  sprintf(c,"%d",a);  string s(c);
#define SORT(a) sort(a.begin(),a.end())
#define REV(a) reverse(a.begin(),a.end())

long long dp[1000000];

int main(int argc, char** argv)
{	
	string name(argv[1]);
	ifstream fin((name+".in").c_str());
	ofstream fout((name+".out").c_str());
	
	int T;
	fin >> T;

	for(int tt = 0; tt < T; tt++)
	{
		fout << "Case #" << tt+1 << ": ";
		
		long long L, N;
		fin >> L >> N;
		long long len[105];
		FOR(t,0,N)
			fin >> len[t];
		sort(len,len+N);
		
		memset(dp,0,sizeof dp);
		FOR(p,0,1000000)
			dp[p] = 2099999999999999999LL;
		dp[0] = 0;
		
		FOR(p,0,N)
		{
			FOR(t,0,1000000)
			{
				if(t >= len[p])
				{
					dp[t] = min(dp[t],dp[t-len[p]]+1);
				}
			}
		}
		
		long long ans = 2099999999999999999LL;
		
		int t = L%len[N-1];
		
		cout << t << " " << len[N-1] << " " << L << endl;
		while(t <= L && t < 1000000)
		{
			if(dp[t] < ans)
				ans = min(ans, dp[t] + (L-t)/len[N-1]);
			t += len[N-1];
		}
			
		if(ans < 2099999999999999999LL)
			fout << ans << endl;
		else fout << "IMPOSSIBLE\n";
	}
	
	return 0;
}
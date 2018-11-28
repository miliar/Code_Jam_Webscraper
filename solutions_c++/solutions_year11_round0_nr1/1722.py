#include <iostream>
#include <string>
#include <fstream>
#include <cmath>

using namespace std;

#define TEST 
#ifdef TEST
ifstream fin("A-large.in");
ofstream fout("a.out");
#else
#define fin cin
#endif

int main()
{
	int T;
	int cases = 0;
	int N;
	fin >> T;
	while (T--)
	{
		fin >> N;
		
		int pos[2] = {1,1};
		int steps = 0;
		char nowc = 'O';
		int now = 0;
		int ans = 0;

		for (int i=0; i<N; i++)
		{
			string s;
			int p;
			fin >> s >> p;
			
			if (nowc == s[0])
			{
				steps += abs(pos[now]-p)+1;
				pos[now] = p;
			}
			else
			{
				int ksteps = abs(pos[1-now] - p);
				ans += steps;
				steps = max(ksteps-steps+1,1);
				now = 1-now;
				pos[now] = p;
				nowc=s[0];
			}
		}
		ans += steps;

		fout << "Case #" << ++cases << ": " << ans << endl;
	}
	return 0;
}
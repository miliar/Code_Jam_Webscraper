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

using namespace std;

#define MSG(a) cout << #a << " = " << a << endl;
#define FOR(a,start,end) for(int a = int(start); a < int(end); a++)
#define PB push_back

int main()
{
	ifstream fin("A-large.in");
	ofstream fout("A-large.out");
	
	int T;
	fin >> T;
	for(int ta = 0; ta < T; ta++)
	{
		fout << "Case #" << ta+1 << ": ";
		
		double lengths[1003];
		double speeds[1003];
		
		long long X, S, R, t, N;
		fin >> X >> S >> R >> t >> N;
		double s = S, r = R;
		double lenTot = X;
		FOR(i,0,N)
		{
			double Bi, Ei, Wi;
			fin >> Bi >> Ei >> Wi;
			lengths[i] = Ei-Bi;
			speeds[i] = Wi;
			lenTot -= lengths[i];
		}
		
		lengths[N] = lenTot;
		speeds[N] = 0;
		N++;
		
		FOR(i,0,N)
		FOR(j,0,i)
		if(speeds[j] > speeds[i])
			swap(speeds[i],speeds[j]), swap(lengths[i],lengths[j]);
		
		double timeLeftToRun = t;
		double ans = 0;
		FOR(i,0,N)
		{
			double runnableLength = min(timeLeftToRun*(speeds[i]+r), lengths[i]);
			timeLeftToRun -= runnableLength/(speeds[i]+r);
			ans += runnableLength/(speeds[i]+r) + (lengths[i]-runnableLength)/(speeds[i]+s);
		}
		fout << setprecision(10) << fixed << ans << endl;
	}
	return 0;
}







#include <iostream>
#include <iomanip>
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
#include <algorithm>

using namespace std;

double x[50], y[50], r[50];

double dist(int a, int b)
{
	return sqrt((x[a]-x[b])*(x[a]-x[b])+(y[a]-y[b])*(y[a]-y[b]));
}

int main()
{
	ofstream fout("D-small.out");
	ifstream fin("D-small-attempt0.in");
	
	int T;
	fin >> T;
	for(int tt = 0; tt < T; tt++)
	{
		int N;
		fin >> N;
		for(int p = 0; p < N; p++)
			fin >> x[p] >> y[p] >> r[p];
		
		double ans = 0;
		if(N == 1)
			ans = r[0];
		else if(N == 2)
			ans = max(r[0],r[1]);
		else if(N == 3)
		{
			double a1 = max(r[0],(r[1]+r[2]+dist(1,2))/2);
			double a2 = max(r[1],(r[0]+r[2]+dist(0,2))/2);
			double a3 = max(r[2],(r[1]+r[0]+dist(1,0))/2);
			ans = min(a1,a2);
			ans = min(ans,a3);
		}
		
		fout << "Case #" << tt+1 << ": " << fixed << setprecision(8) << ans << endl;
	}
		
		

	return 0;
}
		

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
#include <algorithm>
#include <stdio.h>

using namespace std;

long long lower[1000005];
long long upper[1000005];

int main()
{	
	ofstream fout("C-large.txt");
	
	ifstream fin("C-large.in");
	
	double phiinv = 2.0/(1.0+sqrt(5.0));
	double phi = (1.0+sqrt(5.0))/2.0;
	for(int n = 1; n <= 1000000; n++)
		lower[n] = ceil(phiinv*n), upper[n] = floor(phi*n);
	
	for(int t = 1; t <= 30; t++)
		cout << lower[t] << " " << upper[t] << endl;
	
	int T;
	fin >> T;
			
	for(int i = 0; i < T; i++)
	{
		long long cnt = 0;
		long long A1, A2, B1, B2;
		fin >> A1 >> A2 >> B1 >> B2;
		for(int a = A1; a <= A2; a++)
		{
			long long l = B1, h = B2;
			l = max(l, lower[a]), h = min(h, upper[a]);
			cnt += max(0LL, h-l+1);
		}
		
		fout << "Case #" << i+1 << ": " << (A2-A1+1)*(B2-B1+1)-cnt << endl;
	}
	
	return 0;
}
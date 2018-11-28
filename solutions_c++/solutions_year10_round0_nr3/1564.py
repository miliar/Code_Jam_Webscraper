#include <string>
#include <vector>
#include <map>
#include <math.h>
#include <algorithm>
#include <iostream>
#include <sstream>

using namespace std;

void func(int casen);

int main()
{
	int cases;
	cin >> cases;

	for(int i=0;i<cases;i++)
	  func(i+1);	
}

void func(int casen)
{
	long long r, k, t;
	int n, i, j;
	long long sum=0, taken;
	

	cin >> r >> k >> n;

	vector<long long> g(n, 0);
	vector<long long> take(n, 0);
	vector<long long> poses(n, 0);

	for(i=0;i<n;i++)
		cin >> g[i];


	int pos=0, prev=n;

	for(pos=0;pos<n;pos++)
	{
		prev = pos+n;
		taken = 0;
		for(i=pos;i<prev && taken+g[i%n]<=k;i++)
			taken += g[i%n];

		take[pos] = taken;
		poses[pos] = i%n;
	}


	for(j=0, pos = 0;j<r;j++)
	{
		sum += take[pos];
		pos = poses[pos];
	}


     cout << "Case #" << casen << ": " << sum << endl;

}
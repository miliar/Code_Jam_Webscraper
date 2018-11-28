#include <fstream>
#include <string>
#include <iostream>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <cmath>
#include <cstring>
#include <numeric>
using namespace std;

#include <time.h>

#define sz(a) a.size()
#define vi vector<int>
#define vs vector<string>
#define vii vector< pair<int,int> >
#define all(a) a.begin(),a.end()
#define pb push_back

int main()
{
	ifstream in("C-large.in");
	ofstream out("candy_SHIT_large.out");

	int t,c;

	in>>t;
	for(int i=1;i<=t;i++)
	{
		in>>c;
		long long x=0,minX=10000000, sum = 0, xor=0;
		for(int j=0;j<c;j++)
		{
			in>>x;
			sum+=x;
			xor^=x;
			minX = min(minX, x);
		}

		if(xor==0)
		{
			out<<"Case #"<<i<<": "<<sum-minX<<endl;
			continue;
		}
		out<<"Case #"<<i<<": "<<"NO"<<endl;
	}

	in.close();
	out.close();
	return 0;
}
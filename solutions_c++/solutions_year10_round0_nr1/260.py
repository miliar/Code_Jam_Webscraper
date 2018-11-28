#include <fstream>
#include <vector>
#include <string>
#include <cmath>
#include <algorithm>

#define ll long long

using namespace std;

int main()
{
	ifstream dat("input.txt");
	ofstream sol("output.txt");
	int t,n,k;
	dat >> t;
	for(int i=0;i<t;i++)
	{
		dat >> n >> k;
		sol << "Case #" << i+1 << ": ";
		if ((k+1)%(1<<n)==0) sol << "ON\n";
		else sol << "OFF\n";
	}
	return 0;
}
